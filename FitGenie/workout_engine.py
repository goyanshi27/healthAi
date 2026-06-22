# workout_engine.py – Rule-based AI Workout Recommendation Engine

WORKOUT_DB = {
    "weight_loss": {
        "home": {
            "none": {
                "beginner": [
                    {"exercise": "Jumping Jacks",       "sets": 3, "reps": "30 sec", "rest": "15 sec", "calories": 8},
                    {"exercise": "Bodyweight Squats",   "sets": 3, "reps": 15,       "rest": "30 sec", "calories": 6},
                    {"exercise": "Push-ups (knee)",     "sets": 3, "reps": 10,       "rest": "30 sec", "calories": 5},
                    {"exercise": "Mountain Climbers",   "sets": 3, "reps": "20 sec", "rest": "20 sec", "calories": 7},
                    {"exercise": "Plank",               "sets": 3, "reps": "20 sec", "rest": "20 sec", "calories": 4},
                    {"exercise": "High Knees",          "sets": 3, "reps": "30 sec", "rest": "15 sec", "calories": 8},
                ],
                "intermediate": [
                    {"exercise": "Burpees",             "sets": 4, "reps": 12,       "rest": "30 sec", "calories": 12},
                    {"exercise": "Jump Squats",         "sets": 4, "reps": 15,       "rest": "30 sec", "calories": 10},
                    {"exercise": "Push-ups",            "sets": 4, "reps": 15,       "rest": "30 sec", "calories": 7},
                    {"exercise": "Mountain Climbers",   "sets": 4, "reps": "30 sec", "rest": "20 sec", "calories": 10},
                    {"exercise": "Plank",               "sets": 3, "reps": "45 sec", "rest": "20 sec", "calories": 5},
                    {"exercise": "Lunge Jumps",         "sets": 3, "reps": 12,       "rest": "30 sec", "calories": 9},
                ],
            },
            "dumbbells": {
                "beginner": [
                    {"exercise": "DB Goblet Squat",     "sets": 3, "reps": 12, "rest": "45 sec", "calories": 7},
                    {"exercise": "DB Shoulder Press",   "sets": 3, "reps": 10, "rest": "45 sec", "calories": 6},
                    {"exercise": "DB Romanian Deadlift","sets": 3, "reps": 10, "rest": "45 sec", "calories": 7},
                    {"exercise": "DB Bent-Over Row",    "sets": 3, "reps": 10, "rest": "45 sec", "calories": 6},
                    {"exercise": "Jumping Jacks",       "sets": 3, "reps": "30 sec", "rest": "15 sec", "calories": 8},
                    {"exercise": "Plank",               "sets": 3, "reps": "30 sec", "rest": "20 sec", "calories": 4},
                ],
                "intermediate": [
                    {"exercise": "DB Thruster",         "sets": 4, "reps": 12, "rest": "45 sec", "calories": 12},
                    {"exercise": "DB Renegade Row",     "sets": 4, "reps": 10, "rest": "45 sec", "calories": 10},
                    {"exercise": "DB Lunge",            "sets": 4, "reps": 12, "rest": "30 sec", "calories": 9},
                    {"exercise": "DB Chest Press",      "sets": 4, "reps": 12, "rest": "45 sec", "calories": 8},
                    {"exercise": "Burpees",             "sets": 3, "reps": 10, "rest": "30 sec", "calories": 12},
                    {"exercise": "DB Lateral Raise",    "sets": 3, "reps": 15, "rest": "30 sec", "calories": 5},
                ],
            },
            "resistance_bands": {
                "beginner": [
                    {"exercise": "Band Squat",          "sets": 3, "reps": 15, "rest": "30 sec", "calories": 7},
                    {"exercise": "Band Pull-Apart",     "sets": 3, "reps": 15, "rest": "30 sec", "calories": 5},
                    {"exercise": "Band Glute Bridge",   "sets": 3, "reps": 15, "rest": "30 sec", "calories": 6},
                    {"exercise": "Band Row",            "sets": 3, "reps": 12, "rest": "30 sec", "calories": 6},
                    {"exercise": "Band Overhead Press", "sets": 3, "reps": 12, "rest": "30 sec", "calories": 5},
                    {"exercise": "High Knees",          "sets": 3, "reps": "30 sec", "rest": "15 sec", "calories": 8},
                ],
                "intermediate": [
                    {"exercise": "Band Jump Squat",     "sets": 4, "reps": 15, "rest": "30 sec", "calories": 10},
                    {"exercise": "Band Deadlift",       "sets": 4, "reps": 12, "rest": "45 sec", "calories": 9},
                    {"exercise": "Band Chest Press",    "sets": 4, "reps": 12, "rest": "30 sec", "calories": 8},
                    {"exercise": "Band Lat Pulldown",   "sets": 3, "reps": 12, "rest": "30 sec", "calories": 7},
                    {"exercise": "Mountain Climbers",   "sets": 3, "reps": "30 sec", "rest": "20 sec", "calories": 10},
                    {"exercise": "Band Bicycle Crunch", "sets": 3, "reps": 20, "rest": "20 sec", "calories": 6},
                ],
            },
        },
        "gym": {
            "full_gym": {
                "beginner": [
                    {"exercise": "Treadmill Walk/Jog",  "sets": 1, "reps": "20 min", "rest": "—",    "calories": 150},
                    {"exercise": "Leg Press",           "sets": 3, "reps": 12,       "rest": "60 sec","calories": 10},
                    {"exercise": "Lat Pulldown",        "sets": 3, "reps": 10,       "rest": "60 sec","calories": 8},
                    {"exercise": "Cable Row",           "sets": 3, "reps": 10,       "rest": "60 sec","calories": 8},
                    {"exercise": "Chest Press Machine", "sets": 3, "reps": 12,       "rest": "60 sec","calories": 7},
                    {"exercise": "Plank",               "sets": 3, "reps": "30 sec", "rest": "20 sec","calories": 4},
                ],
                "intermediate": [
                    {"exercise": "Treadmill HIIT",      "sets": 1, "reps": "25 min", "rest": "—",    "calories": 250},
                    {"exercise": "Barbell Squat",       "sets": 4, "reps": 10,       "rest": "90 sec","calories": 14},
                    {"exercise": "Bench Press",         "sets": 4, "reps": 10,       "rest": "90 sec","calories": 12},
                    {"exercise": "Deadlift",            "sets": 3, "reps": 8,        "rest": "90 sec","calories": 15},
                    {"exercise": "Pull-ups",            "sets": 3, "reps": 8,        "rest": "60 sec","calories": 10},
                    {"exercise": "Cable Crunch",        "sets": 3, "reps": 15,       "rest": "30 sec","calories": 6},
                ],
            },
        },
    },
    "muscle_building": {
        "home": {
            "none": {
                "beginner": [
                    {"exercise": "Push-ups",            "sets": 4, "reps": 12, "rest": "60 sec", "calories": 6},
                    {"exercise": "Bodyweight Squat",    "sets": 4, "reps": 15, "rest": "60 sec", "calories": 7},
                    {"exercise": "Glute Bridge",        "sets": 3, "reps": 15, "rest": "45 sec", "calories": 5},
                    {"exercise": "Pike Push-up",        "sets": 3, "reps": 10, "rest": "60 sec", "calories": 5},
                    {"exercise": "Diamond Push-up",     "sets": 3, "reps": 8,  "rest": "60 sec", "calories": 5},
                    {"exercise": "Plank",               "sets": 3, "reps": "40 sec", "rest": "20 sec", "calories": 4},
                ],
                "intermediate": [
                    {"exercise": "Archer Push-up",      "sets": 4, "reps": 8,  "rest": "60 sec", "calories": 7},
                    {"exercise": "Pistol Squat",        "sets": 3, "reps": 6,  "rest": "90 sec", "calories": 8},
                    {"exercise": "Pike Push-up",        "sets": 4, "reps": 12, "rest": "60 sec", "calories": 6},
                    {"exercise": "Bulgarian Split Squat","sets": 4, "reps": 10, "rest": "60 sec","calories": 9},
                    {"exercise": "Decline Push-up",     "sets": 4, "reps": 12, "rest": "60 sec", "calories": 6},
                    {"exercise": "L-sit Hold",          "sets": 3, "reps": "15 sec", "rest": "45 sec", "calories": 4},
                ],
            },
            "dumbbells": {
                "beginner": [
                    {"exercise": "DB Bicep Curl",       "sets": 3, "reps": 12, "rest": "60 sec", "calories": 5},
                    {"exercise": "DB Tricep Extension", "sets": 3, "reps": 12, "rest": "60 sec", "calories": 5},
                    {"exercise": "DB Shoulder Press",   "sets": 3, "reps": 10, "rest": "60 sec", "calories": 6},
                    {"exercise": "DB Chest Press",      "sets": 4, "reps": 12, "rest": "60 sec", "calories": 8},
                    {"exercise": "DB Romanian Deadlift","sets": 3, "reps": 10, "rest": "60 sec", "calories": 8},
                    {"exercise": "DB Lateral Raise",    "sets": 3, "reps": 12, "rest": "45 sec", "calories": 5},
                ],
                "intermediate": [
                    {"exercise": "DB Arnold Press",     "sets": 4, "reps": 12, "rest": "60 sec", "calories": 8},
                    {"exercise": "DB Incline Press",    "sets": 4, "reps": 10, "rest": "75 sec", "calories": 9},
                    {"exercise": "DB Hammer Curl",      "sets": 4, "reps": 12, "rest": "60 sec", "calories": 6},
                    {"exercise": "DB Skull Crusher",    "sets": 4, "reps": 10, "rest": "60 sec", "calories": 6},
                    {"exercise": "DB Goblet Squat",     "sets": 4, "reps": 12, "rest": "75 sec", "calories": 8},
                    {"exercise": "DB Bent-Over Row",    "sets": 4, "reps": 10, "rest": "75 sec", "calories": 8},
                ],
            },
        },
        "gym": {
            "full_gym": {
                "beginner": [
                    {"exercise": "Barbell Squat",       "sets": 4, "reps": 8,  "rest": "90 sec", "calories": 14},
                    {"exercise": "Bench Press",         "sets": 4, "reps": 8,  "rest": "90 sec", "calories": 12},
                    {"exercise": "Lat Pulldown",        "sets": 4, "reps": 10, "rest": "75 sec", "calories": 10},
                    {"exercise": "Shoulder Press",      "sets": 3, "reps": 10, "rest": "75 sec", "calories": 8},
                    {"exercise": "Barbell Curl",        "sets": 3, "reps": 12, "rest": "60 sec", "calories": 6},
                    {"exercise": "Tricep Pushdown",     "sets": 3, "reps": 12, "rest": "60 sec", "calories": 5},
                ],
                "intermediate": [
                    {"exercise": "Deadlift",            "sets": 4, "reps": 6,  "rest": "120 sec","calories": 16},
                    {"exercise": "Barbell Squat",       "sets": 5, "reps": 5,  "rest": "120 sec","calories": 15},
                    {"exercise": "Incline Bench Press", "sets": 4, "reps": 8,  "rest": "90 sec", "calories": 13},
                    {"exercise": "Pull-ups",            "sets": 4, "reps": 8,  "rest": "90 sec", "calories": 10},
                    {"exercise": "Barbell Row",         "sets": 4, "reps": 8,  "rest": "90 sec", "calories": 11},
                    {"exercise": "Military Press",      "sets": 4, "reps": 8,  "rest": "90 sec", "calories": 9},
                ],
            },
        },
    },
    "general_fitness": {
        "home": {
            "none": {
                "beginner": [
                    {"exercise": "Brisk Walk",          "sets": 1, "reps": "20 min", "rest": "—",    "calories": 80},
                    {"exercise": "Bodyweight Squat",    "sets": 3, "reps": 12, "rest": "30 sec", "calories": 6},
                    {"exercise": "Push-ups",            "sets": 3, "reps": 10, "rest": "30 sec", "calories": 5},
                    {"exercise": "Plank",               "sets": 3, "reps": "20 sec", "rest": "20 sec", "calories": 4},
                    {"exercise": "Jumping Jacks",       "sets": 3, "reps": "30 sec", "rest": "15 sec", "calories": 8},
                    {"exercise": "Glute Bridge",        "sets": 3, "reps": 12, "rest": "30 sec", "calories": 5},
                ],
                "intermediate": [
                    {"exercise": "Jump Rope (simulated)","sets": 3, "reps": "2 min", "rest": "30 sec","calories": 20},
                    {"exercise": "Push-ups",            "sets": 4, "reps": 15, "rest": "30 sec", "calories": 7},
                    {"exercise": "Bodyweight Squat",    "sets": 4, "reps": 15, "rest": "30 sec", "calories": 7},
                    {"exercise": "Reverse Lunge",       "sets": 3, "reps": 12, "rest": "30 sec", "calories": 7},
                    {"exercise": "Superman Hold",       "sets": 3, "reps": "30 sec", "rest": "20 sec", "calories": 4},
                    {"exercise": "Bicycle Crunch",      "sets": 3, "reps": 20, "rest": "20 sec", "calories": 6},
                ],
            },
            "dumbbells": {
                "beginner": [
                    {"exercise": "DB Squat",            "sets": 3, "reps": 12, "rest": "45 sec", "calories": 7},
                    {"exercise": "DB Chest Press",      "sets": 3, "reps": 12, "rest": "45 sec", "calories": 7},
                    {"exercise": "DB Bent-Over Row",    "sets": 3, "reps": 10, "rest": "45 sec", "calories": 6},
                    {"exercise": "DB Bicep Curl",       "sets": 3, "reps": 12, "rest": "30 sec", "calories": 5},
                    {"exercise": "DB Shoulder Press",   "sets": 3, "reps": 10, "rest": "45 sec", "calories": 6},
                    {"exercise": "Plank",               "sets": 3, "reps": "30 sec", "rest": "20 sec", "calories": 4},
                ],
                "intermediate": [
                    {"exercise": "DB Circuit (full body)","sets": 4, "reps": 12, "rest": "45 sec","calories": 12},
                    {"exercise": "DB Lunge",            "sets": 4, "reps": 10, "rest": "45 sec", "calories": 9},
                    {"exercise": "DB Renegade Row",     "sets": 3, "reps": 10, "rest": "60 sec", "calories": 10},
                    {"exercise": "DB Thruster",         "sets": 3, "reps": 12, "rest": "45 sec", "calories": 11},
                    {"exercise": "DB Lateral Raise",    "sets": 3, "reps": 12, "rest": "30 sec", "calories": 5},
                    {"exercise": "DB Russian Twist",    "sets": 3, "reps": 20, "rest": "20 sec", "calories": 6},
                ],
            },
        },
        "gym": {
            "full_gym": {
                "beginner": [
                    {"exercise": "Elliptical",          "sets": 1, "reps": "20 min", "rest": "—",    "calories": 160},
                    {"exercise": "Leg Press",           "sets": 3, "reps": 12, "rest": "60 sec", "calories": 10},
                    {"exercise": "Cable Row",           "sets": 3, "reps": 12, "rest": "60 sec", "calories": 8},
                    {"exercise": "Chest Fly Machine",   "sets": 3, "reps": 12, "rest": "60 sec", "calories": 7},
                    {"exercise": "Shoulder Press Machine","sets": 3,"reps": 10, "rest": "60 sec","calories": 7},
                    {"exercise": "Ab Crunch Machine",   "sets": 3, "reps": 15, "rest": "30 sec", "calories": 5},
                ],
                "intermediate": [
                    {"exercise": "Treadmill Run",       "sets": 1, "reps": "25 min", "rest": "—",    "calories": 220},
                    {"exercise": "Barbell Squat",       "sets": 4, "reps": 10, "rest": "90 sec", "calories": 14},
                    {"exercise": "Bench Press",         "sets": 4, "reps": 10, "rest": "90 sec", "calories": 12},
                    {"exercise": "Pull-ups",            "sets": 4, "reps": 8,  "rest": "75 sec", "calories": 10},
                    {"exercise": "Overhead Press",      "sets": 3, "reps": 10, "rest": "75 sec", "calories": 9},
                    {"exercise": "Plank",               "sets": 3, "reps": "45 sec", "rest": "20 sec","calories": 5},
                ],
            },
        },
    },
}

# Map goals to DB keys
GOAL_MAP = {
    "Weight Loss":    "weight_loss",
    "Fat Loss":       "weight_loss",
    "Weight Gain":    "muscle_building",
    "Muscle Building":"muscle_building",
    "General Fitness":"general_fitness",
}

EQUIPMENT_MAP = {
    "None":             "none",
    "Dumbbells":        "dumbbells",
    "Resistance Bands": "resistance_bands",
    "Full Gym":         "full_gym",
}

LOCATION_MAP = {
    "Home": "home",
    "Gym":  "gym",
}

DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

REST_DAY = [{"exercise": "Active Rest", "sets": "—", "reps": "Light Walk / Stretching / Yoga", "rest": "—", "calories": 30}]

WEEKLY_SPLIT = {
    "weight_loss": {
        "days": [0, 1, 2, 3, 4, 5],   # 6 workout days, 1 rest
        "rest": [6],
    },
    "muscle_building": {
        "days": [0, 1, 2, 4, 5],       # 5 workout days, 2 rest
        "rest": [3, 6],
    },
    "general_fitness": {
        "days": [0, 1, 2, 3, 4],       # 5 workout days, 2 rest
        "rest": [5, 6],
    },
}


def _determine_level(activity_level: str) -> str:
    if activity_level in ("Sedentary", "Lightly Active"):
        return "beginner"
    return "intermediate"


def _get_exercises(goal_key: str, location_key: str, equipment_key: str, level: str):
    goal_db = WORKOUT_DB.get(goal_key, WORKOUT_DB["general_fitness"])
    loc_db  = goal_db.get(location_key, goal_db.get("home", {}))

    # Try requested equipment, fall back gracefully
    if equipment_key in loc_db:
        equip_db = loc_db[equipment_key]
    elif "none" in loc_db:
        equip_db = loc_db["none"]
    else:
        equip_db = list(loc_db.values())[0]

    exercises = equip_db.get(level, equip_db.get("beginner", []))
    return exercises


def generate_weekly_plan(goal: str, activity_level: str, location: str, equipment: str) -> dict:
    goal_key      = GOAL_MAP.get(goal, "general_fitness")
    location_key  = LOCATION_MAP.get(location, "home")
    equipment_key = EQUIPMENT_MAP.get(equipment, "none")
    level         = _determine_level(activity_level)

    exercises = _get_exercises(goal_key, location_key, equipment_key, level)
    split     = WEEKLY_SPLIT.get(goal_key, WEEKLY_SPLIT["general_fitness"])

    weekly_plan = {}
    for i, day in enumerate(DAYS):
        if i in split["rest"]:
            weekly_plan[day] = {"type": "rest", "exercises": REST_DAY}
        else:
            weekly_plan[day] = {"type": "workout", "exercises": exercises}

    return {
        "weekly_plan": weekly_plan,
        "level":       level,
        "goal_key":    goal_key,
        "location":    location,
        "equipment":   equipment,
    }


def estimate_calories_burned(exercises: list, weight_kg: float) -> float:
    base = sum(e.get("calories", 0) for e in exercises)
    # Scale by body weight (reference = 70 kg)
    return round(base * (weight_kg / 70), 1)


def get_fitness_tips(goal: str) -> list:
    tips = {
        "Weight Loss": [
            "Stay in a caloric deficit of 300–500 kcal/day.",
            "Incorporate 30 min of cardio 5x per week.",
            "Drink water before meals to reduce hunger.",
            "Sleep 7–8 hours to regulate hunger hormones.",
            "Track your food intake honestly.",
        ],
        "Fat Loss": [
            "Combine strength training with cardio for best results.",
            "Prioritize protein to preserve muscle while losing fat.",
            "Avoid liquid calories — they add up fast.",
            "HIIT workouts burn more fat in less time.",
            "Consistency beats intensity.",
        ],
        "Muscle Building": [
            "Eat in a slight caloric surplus (200–300 kcal).",
            "Prioritize compound lifts — squat, bench, deadlift.",
            "Get 1.6–2.2 g of protein per kg of bodyweight.",
            "Allow 48 hours recovery between muscle groups.",
            "Progressive overload is key — add weight weekly.",
        ],
        "Weight Gain": [
            "Eat calorie-dense whole foods like nuts and dairy.",
            "Have 5–6 smaller meals throughout the day.",
            "Lift heavy to ensure weight gain is muscle, not just fat.",
            "Drink whole milk or a homemade mass gainer.",
            "Don't skip breakfast.",
        ],
        "General Fitness": [
            "Aim for 150 min of moderate exercise per week.",
            "Mix cardio and strength training.",
            "Stretch daily to improve flexibility.",
            "Stay consistent — progress beats perfection.",
            "Walk more — 10,000 steps a day makes a difference.",
        ],
    }
    return tips.get(goal, tips["General Fitness"])
