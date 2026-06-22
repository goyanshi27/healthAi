# bmi.py – BMI calculation and health recommendations

def calculate_bmi(weight_kg: float, height_cm: float) -> float:
    height_m = height_cm / 100
    return round(weight_kg / (height_m ** 2), 1)


def get_bmi_category(bmi: float) -> str:
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25.0:
        return "Normal"
    elif bmi < 30.0:
        return "Overweight"
    else:
        return "Obese"


def get_bmi_color(category: str) -> str:
    colors = {
        "Underweight": "#3498db",
        "Normal":      "#2ecc71",
        "Overweight":  "#f39c12",
        "Obese":       "#e74c3c",
    }
    return colors.get(category, "#95a5a6")


def get_ideal_weight_range(height_cm: float) -> tuple:
    h = height_cm / 100
    low  = round(18.5 * h * h, 1)
    high = round(24.9 * h * h, 1)
    return low, high


def get_bmi_recommendations(category: str, goal: str) -> list:
    base = {
        "Underweight": [
            "Increase caloric intake by 300-500 kcal/day.",
            "Focus on nutrient-dense foods: nuts, dairy, legumes.",
            "Strength training 3-4x/week to build muscle mass.",
            "Eat 5-6 smaller meals throughout the day.",
            "Consult a doctor if BMI is below 16.",
        ],
        "Normal": [
            "Maintain your healthy lifestyle – you're doing great!",
            "Balance cardio and strength training.",
            "Focus on body composition rather than just weight.",
            "Stay hydrated and sleep 7-8 hours nightly.",
            "Annual health check-ups are still important.",
        ],
        "Overweight": [
            "Aim for a moderate caloric deficit of 300-400 kcal/day.",
            "Incorporate 150+ minutes of moderate cardio weekly.",
            "Reduce processed foods, sugar, and liquid calories.",
            "Strength training preserves muscle during weight loss.",
            "Gradual loss of 0.5-1 kg/week is sustainable.",
        ],
        "Obese": [
            "Consult a healthcare professional before starting a program.",
            "Begin with low-impact exercise: walking, swimming, cycling.",
            "Focus on sustainable dietary changes, not crash diets.",
            "Aim for 5-10% body weight reduction as first milestone.",
            "Track meals and activity for accountability.",
        ],
    }
    return base.get(category, base["Normal"])


def fitness_score(bmi: float, activity_level: str, goal: str,
                  age: int, sleep_hrs: float = 7.0) -> dict:
    """Generate fitness, diet-quality, and consistency scores (0–100)."""
    # BMI sub-score
    if 18.5 <= bmi <= 24.9:
        bmi_score = 100
    elif 17 <= bmi < 18.5 or 25 <= bmi < 27:
        bmi_score = 80
    elif 15 <= bmi < 17 or 27 <= bmi < 30:
        bmi_score = 60
    else:
        bmi_score = 40

    # Activity sub-score
    act_scores = {
        "Sedentary":         40,
        "Lightly Active":    60,
        "Moderately Active": 80,
        "Very Active":       100,
    }
    act_score = act_scores.get(activity_level, 60)

    # Sleep sub-score
    if 7 <= sleep_hrs <= 9:
        sleep_score = 100
    elif 6 <= sleep_hrs < 7 or 9 < sleep_hrs <= 10:
        sleep_score = 75
    else:
        sleep_score = 50

    fitness   = round((bmi_score * 0.4) + (act_score * 0.6))
    diet_qual = round((bmi_score * 0.5) + (sleep_score * 0.5))
    consistency = act_score  # proxy for workout consistency

    return {
        "fitness_score":     min(fitness, 100),
        "diet_score":        min(diet_qual, 100),
        "consistency_score": min(consistency, 100),
    }


def sleep_recommendation(age: int) -> str:
    if age < 18:
        return "8–10 hours per night"
    elif age < 65:
        return "7–9 hours per night"
    else:
        return "7–8 hours per night"
