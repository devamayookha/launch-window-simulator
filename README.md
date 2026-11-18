# 🚀 Launch Window Simulator

A visual tool to simulate Earth's rotation and calculate launch windows for orbital mechanics.

**Live Demo:** [your-render-link-here](https://your-render-link-here)

---

## Why This Project?

Launch windows are critical in spaceflight — they determine when a rocket can launch to reach a specific orbit. This simulator visually demonstrates how Earth's rotation creates these windows by aligning a launch site with a target orbital plane.

Built to:
- Visualize orbital mechanics concepts (latitude, inclination, RAAN)
- Provide a hands-on tool for aerospace and astrodynamics students
- Practice full-stack development with Python, Flask, SVG, and JavaScript

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| Backend | Python 3, Flask | Lightweight server, window calculations |
| Frontend | HTML5, CSS3 | Responsive UI |
| Animation | SVG + JavaScript | Smooth 2D visualization |

---

## 🎮 How It Works

1. Enter your launch site latitude and target orbit inclination
2. Click Calculate Windows
3. Watch the animation — yellow dot (launch site) moves with Earth's rotation
4. Dot turns **red** when it aligns with the orbital plane — that's your window
5. Results panel shows next 3 launch windows in UTC

---

## Key Visuals

- **Earth** — Blue circle with dashed equator line
- **Orbital Plane** — Red line tilted by inclination angle
- **Launch Site** — Yellow dot at latitude height, turns red on alignment
- **Results Panel** — Lists next 3 windows + explanation

---

## Example Usage

| Latitude | Inclination | Result |
|---|---|---|
| 28.5° | 28.5° | ✅ Windows every ~23h 56m |
| 0° | 51.6° | ✅ Equatorial site, ISS orbit |
| 28.5° | 0° | ❌ Cannot reach equatorial orbit |

---

## 🚀 How to Run Locally

**1. Clone the repository**

```bash
git clone https://github.com/devamayookha/launch-window-simulator.git
cd launch-window-simulator
```

**2. Install dependencies**

```bash
pip install flask gunicorn
```

**3. Run the server**

```bash
python app.py
```

**4. Open your browser**

```
http://localhost:5000
```

---

## Screenshots

*(Coming soon)*

---

## Version 2 Roadmap

- Date range picker for specific window calculations
- Realistic window duration (not just instantaneous alignment)
- Pre-loaded coordinates for Kennedy Space Center, Baikonur, Sriharikota
- 3D globe view using Three.js
- Export results as CSV

---

## About

Built as part of an AI × Space Technology portfolio series by a 2nd year B.Tech AI & Data Science student.

---

## 👤 Author

**B R Devamayookha**
AI & Data Science Student
[GitHub](https://github.com/devamayookha) · [LinkedIn](https://linkedin.com/in/b-r-devamayookha-627305375)

---

## About This Experiment

This application is part of a series of seven small space-tech experiments I created in 2026 to explore different AI coding assistants. Each experiment uses a different project idea and AI tool, following the same prompting approach.

**AI coding assistant used:** Mistral

I directed the project, tested the application and worked through its deployment, while much of the code was AI-generated. The purpose of this series is to learn the tools, explore the underlying technical concepts and understand AI-assisted development workflows — not to present these builds as proof of independent programming proficiency.
