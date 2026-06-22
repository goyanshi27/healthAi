# -*- coding: utf-8 -*-
# app.py – FitGenie AI: Personalized Workout & Diet Planner
# Run: streamlit run app.py

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import random
from datetime import datetime

from workout_engine import generate_weekly_plan, estimate_calories_burned, get_fitness_tips
from diet_engine import (get_meal_plan, calculate_tdee, get_calorie_target,
                          get_macros, water_intake, get_diet_tips)
from bmi import (calculate_bmi, get_bmi_category, get_bmi_color,
                  get_ideal_weight_range, get_bmi_recommendations, fitness_score,
                  sleep_recommendation)
from progress import save_progress, load_progress, get_stats

# ─────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="FitGenie AI",
    page_icon="💪",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─────────────────────────────────────────────
# GLOBAL CSS
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&display=swap');

html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

.hero {
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
    border-radius: 20px; padding: 50px 40px; text-align: center;
    margin-bottom: 30px; border: 1px solid #e94560;
    box-shadow: 0 20px 60px rgba(233,69,96,0.2);
}
.hero h1 { font-size: 3em; font-weight: 800; color: #ffffff; margin: 0; }
.hero p  { font-size: 1.2em; color: #a8b2d8; margin-top: 10px; }
.hero .badge {
    display: inline-block; background: #e94560;
    color: white; padding: 6px 18px; border-radius: 20px;
    font-size: 0.85em; font-weight: 600; margin-bottom: 15px;
}

.feature-card {
    background: linear-gradient(135deg, #1e2a3a, #2d3e50);
    border-radius: 15px; padding: 25px 20px; text-align: center;
    border: 1px solid #344a60; transition: transform .2s;
    height: 100%;
}
.feature-card:hover { transform: translateY(-4px); }
.feature-card .icon { font-size: 2.5em; margin-bottom: 12px; }
.feature-card h3    { color: #e94560; font-size: 1.1em; margin: 0 0 8px; }
.feature-card p     { color: #8892b0; font-size: 0.9em; margin: 0; }

.stat-card {
    background: linear-gradient(135deg, #1e2a3a, #2d3e50);
    border-radius: 12px; padding: 20px; text-align: center;
    border-left: 4px solid #e94560;
}
.stat-card .value { font-size: 2em; font-weight: 700; color: #e94560; }
.stat-card .label { font-size: 0.85em; color: #8892b0; margin-top: 4px; }

.meal-card {
    background: #1e2a3a; border-radius: 12px; padding: 16px;
    border-left: 4px solid #e94560; margin-bottom: 12px;
}
.meal-card .meal-title { font-weight: 700; color: #e94560; font-size: 1em; }
.meal-card .meal-item  { color: #ccd6f6; font-size: 0.95em; margin: 4px 0; }
.meal-card .macros     { color: #8892b0; font-size: 0.82em; margin-top: 6px; }

.exercise-card {
    background: #1e2a3a; border-radius: 10px; padding: 14px;
    border-left: 4px solid #00d2ff; margin-bottom: 8px;
}
.exercise-card .ex-name  { color: #00d2ff; font-weight: 600; }
.exercise-card .ex-meta  { color: #8892b0; font-size: 0.85em; margin-top: 4px; }

.quote-card {
    background: linear-gradient(135deg, #e94560, #c62a47);
    border-radius: 15px; padding: 25px; text-align: center;
    margin: 20px 0;
}
.quote-card .quote  { font-size: 1.15em; font-weight: 600; color: white; }
.quote-card .author { font-size: 0.9em; color: rgba(255,255,255,0.75); margin-top: 8px; }

.score-badge {
    background: #1e2a3a; border-radius: 12px; padding: 18px;
    text-align: center; border: 2px solid #e94560;
}
.score-badge .score { font-size: 2.5em; font-weight: 800; color: #e94560; }
.score-badge .lbl   { font-size: 0.8em; color: #8892b0; }

.tip-box {
    background: #1e2a3a; border-radius: 10px; padding: 14px 18px;
    border-left: 4px solid #f0b429; color: #ccd6f6;
    font-size: 0.92em; margin: 6px 0;
}
.section-title {
    font-size: 1.6em; font-weight: 700; color: #e94560;
    border-bottom: 2px solid #e94560; padding-bottom: 8px;
    margin: 25px 0 18px;
}
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# CONSTANTS
# ─────────────────────────────────────────────
QUOTES = [
    ("The body achieves what the mind believes.", "Napoleon Hill"),
    ("Take care of your body. It's the only place you have to live.", "Jim Rohn"),
    ("An early morning walk is a blessing for the whole day.", "Henry Thoreau"),
    ("A one-hour workout is 4% of your day. No excuses.", "Unknown"),
    ("Your health is an investment, not an expense.", "Unknown"),
    ("Fitness is not about being better than someone else. It's about being better than you used to be.", "Khloe Kardashian"),
    ("The groundwork of all happiness is health.", "Leigh Hunt"),
    ("To keep the body in good health is a duty, otherwise we shall not be able to keep our mind strong.", "Buddha"),
    ("Physical fitness is the first requisite of happiness.", "Joseph Pilates"),
    ("Champions aren't made in gyms. They are made from something deep inside them.", "Muhammad Ali"),
]

DAILY_TIPS = [
    "🚶 Aim for 8,000–10,000 steps daily.",
    "💧 Drink a glass of water first thing in the morning.",
    "🥗 Fill half your plate with vegetables at every meal.",
    "😴 Poor sleep increases cortisol and promotes fat storage.",
    "🧘 5 minutes of deep breathing lowers cortisol levels.",
    "🏃 A 30-min walk burns ~150 kcal and improves mood.",
    "🍌 Banana + peanut butter is a perfect pre-workout snack.",
    "📵 Avoid screens 1 hour before bed for better sleep quality.",
    "🥚 Eggs are one of nature's most complete protein sources.",
    "⏰ Eat your largest meal earlier in the day when possible.",
]

PAGES = ["🏠 Home", "💪 Workout Planner", "🥗 Diet Planner",
         "⚖️ BMI Calculator", "📈 Progress Tracker"]

# ─────────────────────────────────────────────
# SIDEBAR  –  User profile + navigation
# ─────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 💪 FitGenie AI")
    st.markdown("---")

    page = st.radio("Navigate", PAGES, label_visibility="collapsed")

    st.markdown("---")
    st.markdown("### 👤 Your Profile")

    name   = st.text_input("Name", value="Athlete", key="sb_name")
    age    = st.number_input("Age", 10, 80, 22, key="sb_age")
    gender = st.selectbox("Gender", ["Male", "Female", "Other"], key="sb_gender")
    height = st.number_input("Height (cm)", 100, 250, 170, key="sb_height")
    weight = st.number_input("Weight (kg)", 30, 200, 65, key="sb_weight")

    st.markdown("---")
    st.markdown("### 🎯 Fitness Details")

    goal = st.selectbox("Fitness Goal",
        ["Weight Loss","Weight Gain","Muscle Building","General Fitness","Fat Loss"],
        key="sb_goal")
    activity = st.selectbox("Activity Level",
        ["Sedentary","Lightly Active","Moderately Active","Very Active"],
        key="sb_activity")
    location  = st.selectbox("Workout Location", ["Home","Gym"], key="sb_location")
    equipment = st.selectbox("Available Equipment",
        ["None","Dumbbells","Resistance Bands","Full Gym"], key="sb_equipment")

    st.markdown("---")
    st.markdown("### 🍽️ Diet Preferences")

    food_pref = st.selectbox("Food Preference",
        ["Vegetarian","Non-Vegetarian","Vegan"], key="sb_food")
    budget = st.selectbox("Budget", ["Low","Medium","High"], key="sb_budget")
    region = st.selectbox("Region / Culture",
        ["Indian","South Indian","North Indian","Odia","Bengali","General"],
        key="sb_region")

    st.markdown("---")
    bmi_val  = calculate_bmi(weight, height)
    bmi_cat  = get_bmi_category(bmi_val)
    bmi_col  = get_bmi_color(bmi_cat)
    st.markdown(f"**BMI:** <span style='color:{bmi_col};font-weight:700'>{bmi_val} ({bmi_cat})</span>",
                unsafe_allow_html=True)
    st.markdown(f"**TDEE:** {calculate_tdee(weight,height,age,gender,activity):,} kcal/day")

# ─────────────────────────────────────────────
# PAGE: HOME
# ─────────────────────────────────────────────
if page == "🏠 Home":
    quote, author = random.choice(QUOTES)
    tip = random.choice(DAILY_TIPS)

    st.markdown(f"""
    <div class="hero">
        <div class="badge">✨ AI-Powered • 100% Offline</div>
        <h1>💪 FitGenie AI</h1>
        <p>Your Personalized Workout & Diet Planner – built for students, beginners & fitness enthusiasts</p>
    </div>""", unsafe_allow_html=True)

    tdee = calculate_tdee(weight, height, age, gender, activity)
    target_cal = get_calorie_target(tdee, goal)
    scores = fitness_score(bmi_val, activity, goal, age)
    ideal_low, ideal_high = get_ideal_weight_range(height)

    st.markdown('<div class="section-title">📊 Your Dashboard</div>', unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown(f"""<div class="stat-card">
            <div class="value">{bmi_val}</div>
            <div class="label">BMI ({bmi_cat})</div></div>""", unsafe_allow_html=True)
    with c2:
        st.markdown(f"""<div class="stat-card">
            <div class="value">{tdee:,}</div>
            <div class="label">TDEE (kcal/day)</div></div>""", unsafe_allow_html=True)
    with c3:
        st.markdown(f"""<div class="stat-card">
            <div class="value">{target_cal:,}</div>
            <div class="label">Target Calories</div></div>""", unsafe_allow_html=True)
    with c4:
        wi = water_intake(weight, activity)
        st.markdown(f"""<div class="stat-card">
            <div class="value">{wi} L</div>
            <div class="label">Daily Water Goal</div></div>""", unsafe_allow_html=True)

    st.markdown("")
    st.markdown('<div class="section-title">🌟 AI Fitness Scores</div>', unsafe_allow_html=True)
    sc1, sc2, sc3 = st.columns(3)
    with sc1:
        st.markdown(f"""<div class="score-badge">
            <div class="score">{scores['fitness_score']}</div>
            <div class="lbl">Fitness Score / 100</div></div>""", unsafe_allow_html=True)
    with sc2:
        st.markdown(f"""<div class="score-badge">
            <div class="score">{scores['diet_score']}</div>
            <div class="lbl">Diet Quality / 100</div></div>""", unsafe_allow_html=True)
    with sc3:
        st.markdown(f"""<div class="score-badge">
            <div class="score">{scores['consistency_score']}</div>
            <div class="lbl">Consistency / 100</div></div>""", unsafe_allow_html=True)

    st.markdown("")
    st.markdown('<div class="section-title">🚀 Features</div>', unsafe_allow_html=True)
    fc = st.columns(3)
    features = [
        ("🏋️", "Workout Planner", "7-day personalized plans based on your goal, location & equipment"),
        ("🥗", "Diet Planner", "Region-aware meal plans with calories, macros & budget options"),
        ("⚖️", "BMI Calculator", "Instant BMI, category, ideal weight range & health tips"),
        ("📈", "Progress Tracker", "Log weight daily, visualize trends with interactive charts"),
        ("🎯", "AI Scoring", "Get fitness, diet quality and consistency scores out of 100"),
        ("💡", "Daily Tips", "Fresh fitness & nutrition tips to keep you motivated"),
    ]
    for i, (icon, title, desc) in enumerate(features):
        with fc[i % 3]:
            st.markdown(f"""<div class="feature-card">
                <div class="icon">{icon}</div>
                <h3>{title}</h3>
                <p>{desc}</p></div>""", unsafe_allow_html=True)
            st.markdown("")

    st.markdown(f"""
    <div class="quote-card">
        <div class="quote">"{quote}"</div>
        <div class="author">— {author}</div>
    </div>""", unsafe_allow_html=True)

    col_t, col_r = st.columns([2, 1])
    with col_t:
        st.markdown('<div class="section-title">💡 Daily Tip</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="tip-box">{tip}</div>', unsafe_allow_html=True)
    with col_r:
        st.markdown('<div class="section-title">😴 Sleep Goal</div>', unsafe_allow_html=True)
        st.info(f"**{sleep_recommendation(age)}**\nFor age {age}")

    st.markdown('<div class="section-title">📏 Ideal Weight Range</div>', unsafe_allow_html=True)
    st.markdown(f"For your height **{height} cm**, your ideal weight range is **{ideal_low} – {ideal_high} kg** (BMI 18.5–24.9).")

# ─────────────────────────────────────────────
# PAGE: WORKOUT PLANNER
# ─────────────────────────────────────────────
elif page == "💪 Workout Planner":
    st.markdown('<div class="hero" style="padding:30px"><h1 style="font-size:2em">💪 Workout Planner</h1><p>Your personalized weekly workout schedule</p></div>', unsafe_allow_html=True)

    plan_data = generate_weekly_plan(goal, activity, location, equipment)
    weekly    = plan_data["weekly_plan"]
    level     = plan_data["level"].capitalize()

    col1, col2, col3 = st.columns(3)
    with col1: st.info(f"**Goal:** {goal}")
    with col2: st.info(f"**Level:** {level}")
    with col3: st.info(f"**Location:** {location} | **Equipment:** {equipment}")

    st.markdown('<div class="section-title">📅 Weekly Schedule</div>', unsafe_allow_html=True)

    for day, day_data in weekly.items():
        is_rest = day_data["type"] == "rest"
        exercises = day_data["exercises"]
        total_cal = estimate_calories_burned(exercises, weight)

        with st.expander(f"{'🛌' if is_rest else '🔥'} {day} {'– Active Rest' if is_rest else f'– ~{total_cal} kcal'}"):
            if is_rest:
                st.markdown("### 🛌 Rest & Recovery Day")
                st.markdown("**Activities:** Light walk, stretching, yoga, foam rolling")
                st.markdown("Rest is when your muscles actually grow. Don't skip it!")
            else:
                for ex in exercises:
                    reps_val = ex.get("reps", "—")
                    rest_val = ex.get("rest", "—")
                    cal_val  = ex.get("calories", 0)
                    st.markdown(f"""<div class="exercise-card">
                        <span class="ex-name">🏋️ {ex['exercise']}</span>
                        <div class="ex-meta">
                            Sets: <b>{ex.get('sets','—')}</b> &nbsp;|&nbsp;
                            Reps/Time: <b>{reps_val}</b> &nbsp;|&nbsp;
                            Rest: <b>{rest_val}</b> &nbsp;|&nbsp;
                            ~<b>{cal_val} kcal</b>
                        </div></div>""", unsafe_allow_html=True)
                st.markdown(f"**Estimated Total Burn:** ~{total_cal} kcal")

    # Weekly calorie chart
    st.markdown('<div class="section-title">📊 Weekly Calorie Burn Estimate</div>', unsafe_allow_html=True)
    days_list = list(weekly.keys())
    cals_list = [
        estimate_calories_burned(d["exercises"], weight) if d["type"] == "workout" else 30
        for d in weekly.values()
    ]
    colors_list = ["#e94560" if d["type"] == "workout" else "#344a60" for d in weekly.values()]

    fig = go.Figure(go.Bar(
        x=days_list, y=cals_list,
        marker_color=colors_list,
        text=[f"{c} kcal" for c in cals_list],
        textposition="outside",
    ))
    fig.update_layout(
        plot_bgcolor="#0f1923", paper_bgcolor="#0f1923",
        font_color="#ccd6f6", height=380,
        xaxis=dict(gridcolor="#1e2a3a"), yaxis=dict(gridcolor="#1e2a3a"),
        margin=dict(t=30, b=20),
    )
    st.plotly_chart(fig, use_container_width=True)

    # Fitness tips
    st.markdown('<div class="section-title">💡 Workout Tips for Your Goal</div>', unsafe_allow_html=True)
    for tip in get_fitness_tips(goal):
        st.markdown(f'<div class="tip-box">✅ {tip}</div>', unsafe_allow_html=True)

# ─────────────────────────────────────────────
# PAGE: DIET PLANNER
# ─────────────────────────────────────────────
elif page == "🥗 Diet Planner":
    st.markdown('<div class="hero" style="padding:30px"><h1 style="font-size:2em">🥗 Diet Planner</h1><p>Personalized nutrition plan tailored to your culture & budget</p></div>', unsafe_allow_html=True)

    meal_plan    = get_meal_plan(goal, food_pref, budget, region)
    tdee         = calculate_tdee(weight, height, age, gender, activity)
    target_cal   = get_calorie_target(tdee, goal)
    macros       = get_macros(target_cal, goal)
    water        = water_intake(weight, activity)

    # Stats row
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.metric("Target Calories", f"{target_cal:,} kcal")
    with c2: st.metric("Protein", f"{macros['protein_g']} g")
    with c3: st.metric("Carbs",   f"{macros['carbs_g']} g")
    with c4: st.metric("Fats",    f"{macros['fats_g']} g")

    st.markdown('<div class="section-title">🍽️ Today\'s Meal Plan</div>', unsafe_allow_html=True)

    meal_icons = {"breakfast": "🌅", "lunch": "☀️", "dinner": "🌙", "snacks": "🍎"}
    meal_names = {"breakfast": "Breakfast", "lunch": "Lunch", "dinner": "Dinner", "snacks": "Snacks"}
    total_cal_meals = 0

    col_a, col_b = st.columns(2)
    meal_list = list(meal_plan.items())
    for idx, (meal_key, meal_info) in enumerate(meal_list):
        container = col_a if idx % 2 == 0 else col_b
        with container:
            cal  = meal_info.get("calories", 0)
            prot = meal_info.get("protein", 0)
            carb = meal_info.get("carbs", 0)
            fat  = meal_info.get("fats", 0)
            total_cal_meals += cal
            st.markdown(f"""<div class="meal-card">
                <div class="meal-title">{meal_icons.get(meal_key,'🍽️')} {meal_names.get(meal_key, meal_key.capitalize())}</div>
                <div class="meal-item">🍛 {meal_info.get('item','—')}</div>
                <div class="macros">
                    🔥 {cal} kcal &nbsp;|&nbsp;
                    💪 Protein: {prot}g &nbsp;|&nbsp;
                    🌾 Carbs: {carb}g &nbsp;|&nbsp;
                    🥑 Fats: {fat}g
                </div></div>""", unsafe_allow_html=True)

    st.markdown(f"**Total Meal Calories:** {total_cal_meals} kcal &nbsp;|&nbsp; **Target:** {target_cal:,} kcal")

    # Macro pie chart
    st.markdown('<div class="section-title">📊 Macronutrient Distribution</div>', unsafe_allow_html=True)
    pie_col, water_col = st.columns([2, 1])
    with pie_col:
        fig_pie = go.Figure(go.Pie(
            labels=["Protein", "Carbohydrates", "Fats"],
            values=[macros["protein_g"] * 4, macros["carbs_g"] * 4, macros["fats_g"] * 9],
            hole=0.45,
            marker_colors=["#e94560", "#00d2ff", "#f0b429"],
        ))
        fig_pie.update_layout(
            plot_bgcolor="#0f1923", paper_bgcolor="#0f1923",
            font_color="#ccd6f6", height=300,
            legend=dict(bgcolor="#0f1923"),
            margin=dict(t=20, b=20),
        )
        st.plotly_chart(fig_pie, use_container_width=True)
    with water_col:
        st.markdown('<div class="section-title">💧 Water</div>', unsafe_allow_html=True)
        st.markdown(f"""<div class="score-badge" style="margin-top:10px">
            <div class="score">{water} L</div>
            <div class="lbl">Daily Water Intake Goal</div></div>""", unsafe_allow_html=True)
        st.markdown(f"""<div class="tip-box" style="margin-top:12px">
            🥛 Spread {water} L across the day.<br>
            Start with 1 glass of water on waking.<br>
            Drink a glass before each meal.</div>""", unsafe_allow_html=True)

    # Diet tips
    st.markdown('<div class="section-title">💡 Nutrition Tips</div>', unsafe_allow_html=True)
    for tip in get_diet_tips(goal, food_pref):
        st.markdown(f'<div class="tip-box">🥦 {tip}</div>', unsafe_allow_html=True)

# ─────────────────────────────────────────────
# PAGE: BMI CALCULATOR
# ─────────────────────────────────────────────
elif page == "⚖️ BMI Calculator":
    st.markdown('<div class="hero" style="padding:30px"><h1 style="font-size:2em">⚖️ BMI Calculator</h1><p>Know your Body Mass Index and what it means for your health</p></div>', unsafe_allow_html=True)

    st.markdown('<div class="section-title">📐 Calculate BMI</div>', unsafe_allow_html=True)
    cc1, cc2 = st.columns(2)
    with cc1:
        c_weight = st.number_input("Weight (kg)", 30.0, 200.0, float(weight), 0.1, key="bmi_w")
    with cc2:
        c_height = st.number_input("Height (cm)", 100.0, 250.0, float(height), 0.1, key="bmi_h")

    c_bmi  = calculate_bmi(c_weight, c_height)
    c_cat  = get_bmi_category(c_bmi)
    c_col  = get_bmi_color(c_cat)
    il, ih = get_ideal_weight_range(c_height)
    recs   = get_bmi_recommendations(c_cat, goal)

    r1, r2, r3 = st.columns(3)
    with r1:
        st.markdown(f"""<div class="stat-card">
            <div class="value" style="color:{c_col}">{c_bmi}</div>
            <div class="label">Your BMI</div></div>""", unsafe_allow_html=True)
    with r2:
        st.markdown(f"""<div class="stat-card">
            <div class="value" style="color:{c_col}">{c_cat}</div>
            <div class="label">BMI Category</div></div>""", unsafe_allow_html=True)
    with r3:
        st.markdown(f"""<div class="stat-card">
            <div class="value">{il}–{ih}</div>
            <div class="label">Ideal Weight Range (kg)</div></div>""", unsafe_allow_html=True)

    # BMI Gauge
    st.markdown('<div class="section-title">🎯 BMI Gauge</div>', unsafe_allow_html=True)
    fig_gauge = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=c_bmi,
        delta={"reference": 22, "increasing": {"color": "#e74c3c"}, "decreasing": {"color": "#2ecc71"}},
        gauge={
            "axis": {"range": [10, 45], "tickcolor": "#ccd6f6"},
            "bar":  {"color": c_col},
            "steps": [
                {"range": [10, 18.5], "color": "#3498db"},
                {"range": [18.5, 25], "color": "#2ecc71"},
                {"range": [25, 30],   "color": "#f39c12"},
                {"range": [30, 45],   "color": "#e74c3c"},
            ],
            "threshold": {"line": {"color": "white", "width": 3}, "value": c_bmi},
        },
        title={"text": "BMI Value", "font": {"color": "#ccd6f6"}},
        number={"font": {"color": c_col}},
    ))
    fig_gauge.update_layout(
        paper_bgcolor="#1e2a3a", font_color="#ccd6f6", height=340,
        margin=dict(t=40, b=20),
    )
    st.plotly_chart(fig_gauge, use_container_width=True)

    # BMI reference table
    st.markdown('<div class="section-title">📋 BMI Reference Table</div>', unsafe_allow_html=True)
    bmi_table = pd.DataFrame({
        "Category":   ["Underweight", "Normal Weight", "Overweight", "Obese"],
        "BMI Range":  ["< 18.5", "18.5 – 24.9", "25.0 – 29.9", "≥ 30.0"],
        "Risk Level": ["Low (nutritional risk)", "Minimal", "Moderate", "High"],
    })
    st.dataframe(bmi_table, use_container_width=True, hide_index=True)

    st.markdown('<div class="section-title">💊 Health Recommendations</div>', unsafe_allow_html=True)
    for rec in recs:
        st.markdown(f'<div class="tip-box">✅ {rec}</div>', unsafe_allow_html=True)

    # BMI across weight range chart
    st.markdown('<div class="section-title">📈 BMI vs Weight Chart (Your Height)</div>', unsafe_allow_html=True)
    weights_range = np.arange(max(30, il - 20), ih + 25, 1)
    bmis_range    = [calculate_bmi(w, c_height) for w in weights_range]
    fig_line = px.line(x=weights_range, y=bmis_range, labels={"x": "Weight (kg)", "y": "BMI"},
                       color_discrete_sequence=["#00d2ff"])
    fig_line.add_hline(y=18.5, line_dash="dash", line_color="#3498db",  annotation_text="Underweight ↑")
    fig_line.add_hline(y=25.0, line_dash="dash", line_color="#f39c12",  annotation_text="Overweight ↑")
    fig_line.add_hline(y=30.0, line_dash="dash", line_color="#e74c3c",  annotation_text="Obese ↑")
    fig_line.add_vline(x=c_weight, line_dash="dot", line_color="white",  annotation_text=f"You ({c_weight}kg)")
    fig_line.update_layout(
        plot_bgcolor="#0f1923", paper_bgcolor="#0f1923",
        font_color="#ccd6f6", height=350,
        xaxis=dict(gridcolor="#1e2a3a"), yaxis=dict(gridcolor="#1e2a3a"),
        margin=dict(t=30, b=20),
    )
    st.plotly_chart(fig_line, use_container_width=True)

# ─────────────────────────────────────────────
# PAGE: PROGRESS TRACKER
# ─────────────────────────────────────────────
elif page == "📈 Progress Tracker":
    st.markdown('<div class="hero" style="padding:30px"><h1 style="font-size:2em">📈 Progress Tracker</h1><p>Log your weight, track your journey, celebrate your wins</p></div>', unsafe_allow_html=True)

    st.markdown('<div class="section-title">➕ Log Today\'s Progress</div>', unsafe_allow_html=True)
    with st.form("log_form"):
        lc1, lc2 = st.columns(2)
        with lc1:
            log_name   = st.text_input("Your Name", value=name)
            log_weight = st.number_input("Current Weight (kg)", 30.0, 200.0, float(weight), 0.1)
        with lc2:
            log_bmi   = calculate_bmi(log_weight, height)
            st.metric("Calculated BMI", f"{log_bmi}")
            log_notes = st.text_input("Notes (optional)", placeholder="Feeling great today!")
        submitted = st.form_submit_button("💾 Save Progress", use_container_width=True)

    if submitted:
        ok = save_progress(log_name, log_weight, log_bmi, log_notes)
        if ok:
            st.success(f"✅ Progress saved! Weight: {log_weight} kg | BMI: {log_bmi}")
        else:
            st.error("❌ Failed to save. Please try again.")

    st.markdown('<div class="section-title">📊 Progress History</div>', unsafe_allow_html=True)

    filter_name = st.text_input("Filter by name (leave blank for all)", value=name, key="filter_name")
    df = load_progress(filter_name)

    if df.empty:
        st.info("No progress logged yet. Use the form above to start tracking!")
    else:
        df["weight"] = pd.to_numeric(df["weight"], errors="coerce")
        df["bmi"]    = pd.to_numeric(df["bmi"],    errors="coerce")
        stats = get_stats(df)

        # Stats
        s1, s2, s3, s4 = st.columns(4)
        with s1:
            st.markdown(f"""<div class="stat-card">
                <div class="value">{stats.get('entries',0)}</div>
                <div class="label">Total Entries</div></div>""", unsafe_allow_html=True)
        with s2:
            ch = stats.get('change', 0)
            ch_col = "#2ecc71" if ch < 0 else "#e74c3c" if ch > 0 else "#8892b0"
            st.markdown(f"""<div class="stat-card">
                <div class="value" style="color:{ch_col}">{'+' if ch>0 else ''}{ch} kg</div>
                <div class="label">Total Change</div></div>""", unsafe_allow_html=True)
        with s3:
            st.markdown(f"""<div class="stat-card">
                <div class="value">{stats.get('min_weight','—')}</div>
                <div class="label">Lowest Weight (kg)</div></div>""", unsafe_allow_html=True)
        with s4:
            st.markdown(f"""<div class="stat-card">
                <div class="value">{stats.get('current_weight','—')}</div>
                <div class="label">Latest Weight (kg)</div></div>""", unsafe_allow_html=True)

        # Weight chart
        st.markdown('<div class="section-title">📉 Weight Over Time</div>', unsafe_allow_html=True)
        fig_wt = go.Figure()
        fig_wt.add_trace(go.Scatter(
            x=df["date"], y=df["weight"],
            mode="lines+markers",
            line=dict(color="#e94560", width=3),
            marker=dict(size=8, color="#e94560"),
            fill="tozeroy",
            fillcolor="rgba(233,69,96,0.1)",
            name="Weight (kg)",
        ))
        fig_wt.update_layout(
            plot_bgcolor="#0f1923", paper_bgcolor="#0f1923",
            font_color="#ccd6f6", height=360,
            xaxis=dict(gridcolor="#1e2a3a", title="Date"),
            yaxis=dict(gridcolor="#1e2a3a", title="Weight (kg)"),
            margin=dict(t=20, b=20),
        )
        st.plotly_chart(fig_wt, use_container_width=True)

        # BMI chart
        if "bmi" in df.columns and df["bmi"].notna().any():
            st.markdown('<div class="section-title">📊 BMI Over Time</div>', unsafe_allow_html=True)
            fig_bmi = go.Figure()
            fig_bmi.add_trace(go.Scatter(
                x=df["date"], y=df["bmi"],
                mode="lines+markers",
                line=dict(color="#00d2ff", width=3),
                marker=dict(size=8, color="#00d2ff"),
                name="BMI",
            ))
            fig_bmi.add_hline(y=18.5, line_dash="dash", line_color="#3498db", annotation_text="Underweight limit")
            fig_bmi.add_hline(y=25.0, line_dash="dash", line_color="#f39c12", annotation_text="Normal limit")
            fig_bmi.add_hline(y=30.0, line_dash="dash", line_color="#e74c3c", annotation_text="Overweight limit")
            fig_bmi.update_layout(
                plot_bgcolor="#0f1923", paper_bgcolor="#0f1923",
                font_color="#ccd6f6", height=340,
                xaxis=dict(gridcolor="#1e2a3a", title="Date"),
                yaxis=dict(gridcolor="#1e2a3a", title="BMI"),
                margin=dict(t=20, b=20),
            )
            st.plotly_chart(fig_bmi, use_container_width=True)

        # Raw data
        with st.expander("📄 View Raw Data Table"):
            st.dataframe(df, use_container_width=True, hide_index=True)
