from flask import Flask, request, jsonify, render_template
from datetime import datetime, timedelta, timezone

app = Flask(__name__)

SIDEREAL_DAY = 86164  # seconds
FIRST_WINDOW_OFFSET = 21541  # 90° / ω (seconds)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate_windows():
    try:
        # Check if JSON data exists
        if not request.is_json:
            return jsonify({'error': 'Request must be JSON'}), 400

        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400

        # Check required fields
        latitude = data.get('latitude')
        inclination = data.get('inclination')
        if latitude is None or inclination is None:
            return jsonify({'error': 'Latitude and inclination are required'}), 400

        # Convert to float (handles strings like "28.5" or "abc")
        try:
            latitude = float(latitude)
            inclination = float(inclination)
        except (TypeError, ValueError):
            return jsonify({'error': 'Latitude and inclination must be numbers'}), 400

        # Validate ranges
        if not (-90 <= latitude <= 90):
            return jsonify({
                'error': 'Latitude must be between -90° and 90°',
                'explanation': 'Latitude ranges from -90° (South Pole) to +90° (North Pole).'
            }), 400

        if not (0 <= inclination <= 90):
            return jsonify({
                'error': 'Inclination must be between 0° and 90°',
                'explanation': 'Inclination is measured from the equator (0°) to polar (90°).'
            }), 400

        # Check feasibility
        if abs(latitude) > inclination:
            return jsonify({
                'error': f'No windows: |{latitude}°| > {inclination}°',
                'explanation': 'A launch site cannot directly reach an orbit with inclination less than its latitude. Example: Kennedy Space Center (28.5°N) cannot launch into a 0° equatorial orbit without a dogleg maneuver.'
            }), 400

        # Calculate windows (UTC)
        now = datetime.now(timezone.utc)
        windows = []
        first_window = now + timedelta(seconds=FIRST_WINDOW_OFFSET)
        windows.append(first_window.strftime('%Y-%m-%d %H:%M:%S UTC'))

        for i in range(1, 3):
            next_window = first_window + timedelta(seconds=SIDEREAL_DAY * i)
            windows.append(next_window.strftime('%Y-%m-%d %H:%M:%S UTC'))

        return jsonify({
            'windows': windows,
            'explanation': 'Launch windows occur every ~23h56m (sidereal day) when Earth\'s rotation aligns the site with the orbital plane.'
        })

    except Exception as e:
        # Catch-all for unexpected errors (e.g., datetime issues)
        return jsonify({'error': f'An unexpected error occurred: {str(e)}'}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=False)