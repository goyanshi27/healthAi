# 💪 FitGenie AI – Personalized Workout & Diet Planner

> AI-powered fitness planning app built with Streamlit & Python.  
> No API keys. No database. 100% offline. One-command deployment.

---

## 🚀 Quick Start

```bash
# 1. Clone / download the project
cd FitGenie

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run app.py
```

The app opens at **http://localhost:8501** in your browser.

---

## 📁 Project Structure

```
FitGenie/
├── app.py              ← Main Streamlit application (all 6 pages)
├── workout_engine.py   ← Rule-based workout recommendation engine
├── diet_engine.py      ← Personalized meal planning engine
├── bmi.py              ← BMI calculator, scoring & recommendations
├── progress.py         ← CSV-based weight progress tracker
├── data/
│   └── progress.csv    ← Auto-created progress log file
├── requirements.txt    ← Python dependencies (4 libraries only)
└── README.md           ← This file
```

---

## ✨ Features

| Feature | Details |
|---|---|
| 🏠 Home Dashboard | BMI, TDEE, calorie target, fitness scores, daily tip |
| 💪 Workout Planner | 7-day personalized schedule with sets/reps/rest/calories |
| 🥗 Diet Planner | Breakfast/lunch/dinner/snacks with macros, water intake |
| ⚖️ BMI Calculator | Gauge chart, BMI vs weight graph, ideal weight range |
| 📈 Progress Tracker | Log weight daily, view trends with Plotly charts |
| ℹ️ About Project | Stack info, deployment guide, project structure |

---

## 🎯 Personalization Options

- **Goals:** Weight Loss, Weight Gain, Muscle Building, General Fitness, Fat Loss  
- **Activity:** Sedentary → Very Active  
- **Location:** Home / Gym  
- **Equipment:** None, Dumbbells, Resistance Bands, Full Gym  
- **Food:** Vegetarian, Non-Vegetarian, Vegan  
- **Budget:** Low, Medium, High  
- **Region:** Indian, South Indian, North Indian, Odia, Bengali, General  

---

## ☁️ Deploy to Streamlit Cloud (Free)

1. Push this folder to a GitHub repository  
2. Go to [share.streamlit.io](https://share.streamlit.io)  
3. Click **New app** → connect your GitHub repo  
4. Set **Main file path:** `app.py`  
5. Click **Deploy** – done in ~2 minutes!

> No environment variables or secrets needed.

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit + Custom CSS (dark fitness theme)
- **Backend:** Pure Python, rule-based AI engine
- **Charts:** Plotly (gauge, bar, line, pie)
- **Storage:** CSV file (no database required)
- **Dependencies:** streamlit, pandas, numpy, plotly

---

## 📋 Requirements

```
streamlit>=1.28.0
pandas>=1.5.0
numpy>=1.23.0
plotly>=5.15.0
```

---

## 🤖 AI Logic (No External API)

The recommendation engine uses:
- **BMI calculation** (weight ÷ height²)
- **Harris-Benedict equation** for TDEE/BMR
- **Rule-based lookup tables** for workout & diet plans
- **Macro split algorithms** based on fitness goals
- **Activity-adjusted** water intake & calorie targets

---

Built with ❤️ for hackathons, student projects, and fitness enthusiasts.
