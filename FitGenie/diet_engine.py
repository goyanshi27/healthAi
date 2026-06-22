# diet_engine.py – Rule-based AI Diet Recommendation Engine

GOAL_MAP = {
    "Weight Loss": "weight_loss",
    "Fat Loss":    "weight_loss",
    "Weight Gain": "weight_gain",
    "Muscle Building": "muscle_building",
    "General Fitness": "general_fitness",
}

# ──────────────────────────────────────────────────────────
# MEAL TEMPLATES  (food_pref → region → budget → goal)
# ──────────────────────────────────────────────────────────
MEAL_DB = {}

# ── VEGETARIAN ────────────────────────────────────────────
MEAL_DB["vegetarian"] = {
    "indian": {
        "low": {
            "weight_loss": {
                "breakfast": {"item":"Oats porridge + banana","calories":280,"protein":8,"carbs":52,"fats":5},
                "lunch":     {"item":"Brown rice + dal + sabzi + salad","calories":450,"protein":16,"carbs":75,"fats":8},
                "dinner":    {"item":"1 Roti + palak dal + salad","calories":320,"protein":14,"carbs":50,"fats":6},
                "snacks":    {"item":"Makhana (fox nuts) roasted","calories":100,"protein":4,"carbs":18,"fats":1},
            },
            "weight_gain": {
                "breakfast": {"item":"Moong dal chilla (3) + curd + banana","calories":480,"protein":22,"carbs":70,"fats":10},
                "lunch":     {"item":"4 Roti + dal makhani + paneer sabzi","calories":750,"protein":30,"carbs":100,"fats":18},
                "dinner":    {"item":"Rice + rajma + ghee + papad","calories":620,"protein":22,"carbs":98,"fats":14},
                "snacks":    {"item":"Peanut butter on bread + milk","calories":320,"protein":14,"carbs":30,"fats":14},
            },
            "muscle_building": {
                "breakfast": {"item":"Besan chilla (3) + curd","calories":420,"protein":24,"carbs":45,"fats":12},
                "lunch":     {"item":"Brown rice + soya chunk curry + salad","calories":560,"protein":32,"carbs":78,"fats":10},
                "dinner":    {"item":"2 Roti + paneer bhurji + dal","calories":520,"protein":28,"carbs":60,"fats":15},
                "snacks":    {"item":"Roasted chana + buttermilk","calories":180,"protein":10,"carbs":24,"fats":3},
            },
            "general_fitness": {
                "breakfast": {"item":"Poha with peas & peanuts","calories":300,"protein":9,"carbs":50,"fats":7},
                "lunch":     {"item":"2 Roti + mixed veg + curd","calories":430,"protein":14,"carbs":70,"fats":9},
                "dinner":    {"item":"Khichdi + salad","calories":360,"protein":12,"carbs":62,"fats":6},
                "snacks":    {"item":"Banana + chai (no sugar)","calories":110,"protein":2,"carbs":26,"fats":1},
            },
        },
        "medium": {
            "weight_loss": {
                "breakfast": {"item":"Vegetable upma + boiled egg (skip) + green tea","calories":300,"protein":9,"carbs":55,"fats":5},
                "lunch":     {"item":"2 Roti + chana masala + raita + salad","calories":480,"protein":18,"carbs":78,"fats":9},
                "dinner":    {"item":"Grilled paneer salad + 1 roti","calories":380,"protein":20,"carbs":42,"fats":14},
                "snacks":    {"item":"Sprouts chaat","calories":130,"protein":8,"carbs":20,"fats":2},
            },
            "muscle_building": {
                "breakfast": {"item":"Paneer paratha (2) + curd","calories":540,"protein":26,"carbs":62,"fats":18},
                "lunch":     {"item":"Brown rice + paneer curry + dal + salad","calories":680,"protein":36,"carbs":85,"fats":18},
                "dinner":    {"item":"3 Roti + egg curry (veg: tofu) + dal","calories":600,"protein":30,"carbs":75,"fats":16},
                "snacks":    {"item":"Paneer cubes + roasted nuts","calories":250,"protein":16,"carbs":6,"fats":18},
            },
            "weight_gain": {
                "breakfast": {"item":"Paratha (3) + curd + fruit bowl","calories":680,"protein":20,"carbs":100,"fats":20},
                "lunch":     {"item":"Rice + dal makhani + paneer + roti","calories":820,"protein":32,"carbs":115,"fats":22},
                "dinner":    {"item":"3 Roti + mix veg + milk (1 glass)","calories":700,"protein":24,"carbs":105,"fats":16},
                "snacks":    {"item":"Banana shake (milk + banana + sugar)","calories":340,"protein":8,"carbs":60,"fats":6},
            },
            "general_fitness": {
                "breakfast": {"item":"Idli (4) + sambar + chutney","calories":380,"protein":12,"carbs":70,"fats":5},
                "lunch":     {"item":"2 Roti + dal + sabzi + curd","calories":480,"protein":16,"carbs":78,"fats":10},
                "dinner":    {"item":"Brown rice + sambhar + raita","calories":420,"protein":14,"carbs":72,"fats":7},
                "snacks":    {"item":"Mixed fruit bowl","calories":120,"protein":2,"carbs":28,"fats":1},
            },
        },
        "high": {
            "weight_loss": {
                "breakfast": {"item":"Greek yogurt parfait + berries + granola","calories":310,"protein":18,"carbs":40,"fats":8},
                "lunch":     {"item":"Quinoa salad + paneer tikka + green smoothie","calories":490,"protein":28,"carbs":55,"fats":14},
                "dinner":    {"item":"Grilled tofu + roasted veggies + 1 roti","calories":380,"protein":22,"carbs":40,"fats":12},
                "snacks":    {"item":"Almonds (handful) + green tea","calories":120,"protein":4,"carbs":4,"fats":10},
            },
            "muscle_building": {
                "breakfast": {"item":"Paneer scramble + multigrain toast + protein shake","calories":600,"protein":40,"carbs":50,"fats":18},
                "lunch":     {"item":"Brown rice + grilled paneer + dal + salad","calories":720,"protein":42,"carbs":82,"fats":18},
                "dinner":    {"item":"Tofu stir fry + quinoa + soup","calories":550,"protein":34,"carbs":58,"fats":15},
                "snacks":    {"item":"Whey protein smoothie (veg) + nuts","calories":280,"protein":24,"carbs":20,"fats":8},
            },
            "weight_gain": {
                "breakfast": {"item":"Smoothie bowl + granola + paneer toast","calories":750,"protein":28,"carbs":105,"fats":22},
                "lunch":     {"item":"Brown rice + dal makhani + paneer + roti (3)","calories":900,"protein":38,"carbs":120,"fats":25},
                "dinner":    {"item":"Paneer tikka masala + naan (2) + raita","calories":820,"protein":34,"carbs":98,"fats":28},
                "snacks":    {"item":"Dry fruits mix + full fat milk","calories":420,"protein":12,"carbs":55,"fats":18},
            },
            "general_fitness": {
                "breakfast": {"item":"Avocado toast + boiled egg (skip for veg: sprouts) + juice","calories":420,"protein":16,"carbs":48,"fats":16},
                "lunch":     {"item":"Quinoa bowl + roasted chickpeas + salad","calories":520,"protein":22,"carbs":72,"fats":12},
                "dinner":    {"item":"Palak paneer + 2 roti + soup","calories":500,"protein":22,"carbs":58,"fats":16},
                "snacks":    {"item":"Fruit salad + nut butter","calories":200,"protein":5,"carbs":32,"fats":8},
            },
        },
    },
}

# ── NON-VEGETARIAN ────────────────────────────────────────
MEAL_DB["non_vegetarian"] = {
    "indian": {
        "low": {
            "weight_loss": {
                "breakfast": {"item":"Boiled eggs (2) + poha","calories":310,"protein":18,"carbs":40,"fats":10},
                "lunch":     {"item":"Rice + egg curry + salad","calories":470,"protein":24,"carbs":65,"fats":10},
                "dinner":    {"item":"2 Roti + chicken stew (light)","calories":420,"protein":28,"carbs":48,"fats":10},
                "snacks":    {"item":"Boiled egg + buttermilk","calories":110,"protein":9,"carbs":5,"fats":5},
            },
            "muscle_building": {
                "breakfast": {"item":"Egg omelette (3 eggs) + 2 toast + milk","calories":520,"protein":34,"carbs":40,"fats":18},
                "lunch":     {"item":"Rice + chicken curry + dal + salad","calories":650,"protein":42,"carbs":72,"fats":14},
                "dinner":    {"item":"3 Roti + egg bhurji + dal","calories":580,"protein":36,"carbs":68,"fats":14},
                "snacks":    {"item":"Boiled eggs (2) + roasted chana","calories":210,"protein":16,"carbs":14,"fats":8},
            },
            "weight_gain": {
                "breakfast": {"item":"4-egg omelette + paratha (2) + milk","calories":700,"protein":40,"carbs":80,"fats":22},
                "lunch":     {"item":"Rice (large) + mutton curry + dal + roti","calories":900,"protein":50,"carbs":105,"fats":25},
                "dinner":    {"item":"4 Roti + chicken masala + curd","calories":780,"protein":46,"carbs":92,"fats":20},
                "snacks":    {"item":"Chicken sandwich + banana shake","calories":460,"protein":28,"carbs":55,"fats":14},
            },
            "general_fitness": {
                "breakfast": {"item":"Boiled eggs (2) + upma","calories":360,"protein":18,"carbs":48,"fats":10},
                "lunch":     {"item":"2 Roti + chicken sabzi + curd","calories":520,"protein":30,"carbs":60,"fats":12},
                "dinner":    {"item":"Rice + egg curry + salad","calories":440,"protein":24,"carbs":60,"fats":10},
                "snacks":    {"item":"Boiled egg + fruit","calories":130,"protein":8,"carbs":14,"fats":5},
            },
        },
        "medium": {
            "weight_loss": {
                "breakfast": {"item":"Egg white omelette (4 whites) + multigrain toast","calories":280,"protein":22,"carbs":28,"fats":5},
                "lunch":     {"item":"Grilled chicken (150g) + brown rice + salad","calories":500,"protein":40,"carbs":58,"fats":8},
                "dinner":    {"item":"Grilled fish + 1 roti + vegetable soup","calories":380,"protein":32,"carbs":32,"fats":9},
                "snacks":    {"item":"Greek yogurt + berries","calories":120,"protein":10,"carbs":14,"fats":2},
            },
            "muscle_building": {
                "breakfast": {"item":"3-egg omelette + paneer + toast (2)","calories":560,"protein":40,"carbs":38,"fats":22},
                "lunch":     {"item":"Chicken breast (200g) + brown rice + dal","calories":700,"protein":52,"carbs":78,"fats":14},
                "dinner":    {"item":"Fish curry + 3 roti + salad","calories":620,"protein":42,"carbs":70,"fats":16},
                "snacks":    {"item":"Boiled eggs (3) + almonds","calories":280,"protein":22,"carbs":5,"fats":18},
            },
            "weight_gain": {
                "breakfast": {"item":"5-egg omelette + paratha (2) + full milk","calories":820,"protein":50,"carbs":88,"fats":28},
                "lunch":     {"item":"Chicken biryani (large) + raita + salad","calories":980,"protein":52,"carbs":115,"fats":28},
                "dinner":    {"item":"4 Roti + mutton curry + curd + dal","calories":860,"protein":50,"carbs":100,"fats":24},
                "snacks":    {"item":"Peanut butter sandwich + banana shake","calories":480,"protein":20,"carbs":65,"fats":16},
            },
            "general_fitness": {
                "breakfast": {"item":"Egg paratha + curd","calories":460,"protein":22,"carbs":58,"fats":14},
                "lunch":     {"item":"Chicken rice bowl + salad + buttermilk","calories":580,"protein":34,"carbs":68,"fats":12},
                "dinner":    {"item":"2 Roti + fish curry + salad","calories":490,"protein":30,"carbs":52,"fats":13},
                "snacks":    {"item":"Boiled egg + fruit salad","calories":150,"protein":8,"carbs":16,"fats":5},
            },
        },
        "high": {
            "weight_loss": {
                "breakfast": {"item":"Egg white omelette (5 whites) + avocado toast","calories":340,"protein":30,"carbs":30,"fats":10},
                "lunch":     {"item":"Grilled salmon + quinoa + roasted veggies","calories":520,"protein":44,"carbs":48,"fats":14},
                "dinner":    {"item":"Grilled chicken breast + steamed veggies + soup","calories":380,"protein":38,"carbs":20,"fats":10},
                "snacks":    {"item":"Greek yogurt + protein shake","calories":200,"protein":22,"carbs":14,"fats":4},
            },
            "muscle_building": {
                "breakfast": {"item":"4-egg omelette + smoked salmon + multigrain toast","calories":620,"protein":50,"carbs":40,"fats":24},
                "lunch":     {"item":"Grilled chicken (250g) + brown rice + salad + protein shake","calories":820,"protein":70,"carbs":82,"fats":16},
                "dinner":    {"item":"Steak / grilled fish + sweet potato + broccoli","calories":680,"protein":56,"carbs":58,"fats":18},
                "snacks":    {"item":"Whey protein + nuts + banana","calories":340,"protein":30,"carbs":32,"fats":10},
            },
            "weight_gain": {
                "breakfast": {"item":"Full breakfast: eggs (4) + sausage + toast + juice","calories":900,"protein":52,"carbs":95,"fats":32},
                "lunch":     {"item":"Grilled chicken + biryani rice + dal + naan","calories":1050,"protein":58,"carbs":125,"fats":30},
                "dinner":    {"item":"Grilled fish / mutton + 3 roti + paneer side + dessert","calories":920,"protein":54,"carbs":105,"fats":30},
                "snacks":    {"item":"Mass gainer shake + dry fruits","calories":550,"protein":30,"carbs":80,"fats":12},
            },
            "general_fitness": {
                "breakfast": {"item":"Salmon omelette + multigrain toast + OJ","calories":520,"protein":36,"carbs":48,"fats":18},
                "lunch":     {"item":"Grilled chicken salad bowl + whole grain roti","calories":580,"protein":40,"carbs":55,"fats":14},
                "dinner":    {"item":"Baked fish + roasted veggies + brown rice","calories":520,"protein":38,"carbs":52,"fats":12},
                "snacks":    {"item":"Protein bar + fruit","calories":220,"protein":16,"carbs":28,"fats":6},
            },
        },
    },
}

# ── VEGAN ────────────────────────────────────────────────
MEAL_DB["vegan"] = {
    "indian": {
        "low": {
            "weight_loss": {
                "breakfast": {"item":"Oats with almond milk + banana","calories":280,"protein":8,"carbs":52,"fats":5},
                "lunch":     {"item":"Brown rice + chana dal + mixed veg","calories":430,"protein":18,"carbs":72,"fats":6},
                "dinner":    {"item":"1 Roti + soya sabzi + salad","calories":320,"protein":16,"carbs":44,"fats":6},
                "snacks":    {"item":"Roasted chana + cucumber","calories":110,"protein":7,"carbs":16,"fats":2},
            },
            "muscle_building": {
                "breakfast": {"item":"Soya milk smoothie + 2 toast + peanut butter","calories":480,"protein":28,"carbs":52,"fats":16},
                "lunch":     {"item":"Brown rice + soya chunk curry + dal","calories":600,"protein":36,"carbs":80,"fats":10},
                "dinner":    {"item":"3 Roti + tofu bhurji + dal","calories":560,"protein":32,"carbs":68,"fats":12},
                "snacks":    {"item":"Peanuts + soya milk","calories":220,"protein":14,"carbs":18,"fats":10},
            },
            "weight_gain": {
                "breakfast": {"item":"Peanut butter paratha (2) + soya milk","calories":640,"protein":24,"carbs":88,"fats":22},
                "lunch":     {"item":"Rice (large) + rajma + roti + pickle","calories":800,"protein":28,"carbs":120,"fats":14},
                "dinner":    {"item":"4 Roti + soya curry + dal + oil","calories":720,"protein":28,"carbs":105,"fats":18},
                "snacks":    {"item":"Banana + peanut butter + dates","calories":340,"protein":8,"carbs":60,"fats":8},
            },
            "general_fitness": {
                "breakfast": {"item":"Poha + peanuts","calories":290,"protein":8,"carbs":48,"fats":7},
                "lunch":     {"item":"2 Roti + dal + mixed veg","calories":420,"protein":14,"carbs":68,"fats":8},
                "dinner":    {"item":"Khichdi + roasted papad","calories":360,"protein":12,"carbs":62,"fats":6},
                "snacks":    {"item":"Fruit salad","calories":100,"protein":2,"carbs":24,"fats":0},
            },
        },
        "medium": {
            "weight_loss": {
                "breakfast": {"item":"Smoothie (soya milk + spinach + banana)","calories":290,"protein":12,"carbs":46,"fats":5},
                "lunch":     {"item":"Quinoa + chickpea salad + lemon dressing","calories":440,"protein":20,"carbs":62,"fats":10},
                "dinner":    {"item":"Tofu stir-fry + 1 roti","calories":360,"protein":20,"carbs":38,"fats":12},
                "snacks":    {"item":"Sprouts salad","calories":120,"protein":8,"carbs":18,"fats":2},
            },
            "muscle_building": {
                "breakfast": {"item":"Tofu scramble + multigrain toast (2) + OJ","calories":520,"protein":32,"carbs":55,"fats":16},
                "lunch":     {"item":"Brown rice + tofu curry + lentil soup","calories":660,"protein":38,"carbs":82,"fats":14},
                "dinner":    {"item":"3 Roti + soya-tofu curry + dal","calories":600,"protein":36,"carbs":72,"fats":14},
                "snacks":    {"item":"Roasted edamame + peanut butter on apple","calories":260,"protein":16,"carbs":24,"fats":10},
            },
            "weight_gain": {
                "breakfast": {"item":"Granola + coconut yogurt + fruits + nuts","calories":680,"protein":18,"carbs":102,"fats":22},
                "lunch":     {"item":"Rice + dal makhani (vegan) + tofu + roti","calories":860,"protein":34,"carbs":118,"fats":22},
                "dinner":    {"item":"Chickpea curry + 3 roti + coconut milk kheer","calories":820,"protein":28,"carbs":120,"fats":22},
                "snacks":    {"item":"Trail mix + banana + soya shake","calories":460,"protein":16,"carbs":72,"fats":14},
            },
            "general_fitness": {
                "breakfast": {"item":"Idli (4) + sambar (no ghee)","calories":340,"protein":10,"carbs":64,"fats":4},
                "lunch":     {"item":"Brown rice + sambhar + poriyal","calories":450,"protein":14,"carbs":76,"fats":8},
                "dinner":    {"item":"2 Roti + tofu matar + salad","calories":400,"protein":18,"carbs":54,"fats":10},
                "snacks":    {"item":"Coconut water + roasted makhana","calories":110,"protein":4,"carbs":20,"fats":2},
            },
        },
        "high": {
            "weight_loss": {
                "breakfast": {"item":"Acai bowl + chia seeds + granola","calories":320,"protein":8,"carbs":55,"fats":8},
                "lunch":     {"item":"Buddha bowl (quinoa + chickpeas + avocado + greens)","calories":490,"protein":20,"carbs":62,"fats":16},
                "dinner":    {"item":"Lentil soup + grilled tofu + 1 roti","calories":380,"protein":24,"carbs":42,"fats":10},
                "snacks":    {"item":"Mixed nuts + green tea","calories":140,"protein":5,"carbs":6,"fats":12},
            },
            "muscle_building": {
                "breakfast": {"item":"Protein smoothie (soya protein + oats + banana + PB)","calories":620,"protein":40,"carbs":72,"fats":16},
                "lunch":     {"item":"Tempeh + brown rice + edamame + miso soup","calories":720,"protein":50,"carbs":80,"fats":18},
                "dinner":    {"item":"Tofu tikka + quinoa + roasted veggies","calories":600,"protein":38,"carbs":62,"fats":16},
                "snacks":    {"item":"Vegan protein bar + almond milk","calories":300,"protein":25,"carbs":30,"fats":8},
            },
            "weight_gain": {
                "breakfast": {"item":"Smoothie bowl + nut butter + seeds + granola + soya milk","calories":780,"protein":24,"carbs":110,"fats":26},
                "lunch":     {"item":"Chickpea biryani + tofu curry + coconut raita","calories":920,"protein":36,"carbs":128,"fats":28},
                "dinner":    {"item":"Jackfruit curry + 3 roti + coconut kheer","calories":850,"protein":28,"carbs":122,"fats":26},
                "snacks":    {"item":"Vegan mass gainer + dry fruits + dates","calories":520,"protein":24,"carbs":85,"fats":14},
            },
            "general_fitness": {
                "breakfast": {"item":"Overnight oats (oat milk) + berries + chia","calories":380,"protein":12,"carbs":62,"fats":10},
                "lunch":     {"item":"Quinoa salad + roasted chickpeas + lemon tahini","calories":520,"protein":22,"carbs":68,"fats":14},
                "dinner":    {"item":"Lentil dal + roti (2) + roasted cauliflower","calories":460,"protein":20,"carbs":62,"fats":10},
                "snacks":    {"item":"Fruit & nut bar + coconut water","calories":190,"protein":5,"carbs":36,"fats":5},
            },
        },
    },
}

# ── Add "general" region as alias for "indian" ────────────
for pref in list(MEAL_DB.keys()):
    MEAL_DB[pref]["general"]       = MEAL_DB[pref]["indian"]
    MEAL_DB[pref]["south_indian"]  = MEAL_DB[pref]["indian"]
    MEAL_DB[pref]["north_indian"]  = MEAL_DB[pref]["indian"]
    MEAL_DB[pref]["odia"]          = MEAL_DB[pref]["indian"]
    MEAL_DB[pref]["bengali"]       = MEAL_DB[pref]["indian"]

# key normalisation maps
FOOD_MAP = {
    "Vegetarian":     "vegetarian",
    "Non-Vegetarian": "non_vegetarian",
    "Vegan":          "vegan",
}
REGION_MAP = {
    "Indian":       "indian",
    "South Indian": "south_indian",
    "North Indian": "north_indian",
    "Odia":         "odia",
    "Bengali":      "bengali",
    "General":      "general",
}
BUDGET_MAP = {
    "Low":    "low",
    "Medium": "medium",
    "High":   "high",
}


def get_meal_plan(goal: str, food_pref: str, budget: str, region: str) -> dict:
    """Return a full day meal plan dict with breakfast/lunch/dinner/snacks."""
    gk = GOAL_MAP.get(goal, "general_fitness")
    fk = FOOD_MAP.get(food_pref, "vegetarian")
    bk = BUDGET_MAP.get(budget, "low")
    rk = REGION_MAP.get(region, "indian")

    try:
        plan = MEAL_DB[fk][rk][bk][gk]
    except KeyError:
        # fallback chain
        try:
            plan = MEAL_DB[fk]["indian"]["low"]["general_fitness"]
        except Exception:
            plan = {
                "breakfast": {"item":"Oats + milk","calories":250,"protein":8,"carbs":45,"fats":4},
                "lunch":     {"item":"Rice + dal + sabzi","calories":420,"protein":14,"carbs":72,"fats":7},
                "dinner":    {"item":"2 Roti + dal + salad","calories":320,"protein":12,"carbs":50,"fats":6},
                "snacks":    {"item":"Banana + tea","calories":100,"protein":2,"carbs":24,"fats":1},
            }
    return plan


def calculate_tdee(weight_kg: float, height_cm: float, age: int,
                   gender: str, activity_level: str) -> int:
    """Harris-Benedict BMR × activity multiplier."""
    if gender == "Male":
        bmr = 88.36 + (13.4 * weight_kg) + (4.8 * height_cm) - (5.7 * age)
    else:
        bmr = 447.6 + (9.2 * weight_kg) + (3.1 * height_cm) - (4.3 * age)

    multipliers = {
        "Sedentary":         1.2,
        "Lightly Active":    1.375,
        "Moderately Active": 1.55,
        "Very Active":       1.725,
    }
    return int(bmr * multipliers.get(activity_level, 1.375))


def get_calorie_target(tdee: int, goal: str) -> int:
    adjustments = {
        "Weight Loss":    -400,
        "Fat Loss":       -300,
        "Weight Gain":    +400,
        "Muscle Building":+200,
        "General Fitness": 0,
    }
    return tdee + adjustments.get(goal, 0)


def get_macros(calorie_target: int, goal: str) -> dict:
    """Return protein/carb/fat grams based on goal."""
    splits = {
        "Weight Loss":    {"protein": 0.35, "carbs": 0.40, "fats": 0.25},
        "Fat Loss":       {"protein": 0.38, "carbs": 0.37, "fats": 0.25},
        "Muscle Building":{"protein": 0.30, "carbs": 0.45, "fats": 0.25},
        "Weight Gain":    {"protein": 0.25, "carbs": 0.50, "fats": 0.25},
        "General Fitness":{"protein": 0.25, "carbs": 0.50, "fats": 0.25},
    }
    s = splits.get(goal, splits["General Fitness"])
    return {
        "protein_g": round(calorie_target * s["protein"] / 4),
        "carbs_g":   round(calorie_target * s["carbs"]   / 4),
        "fats_g":    round(calorie_target * s["fats"]    / 9),
    }


def water_intake(weight_kg: float, activity_level: str) -> float:
    base = weight_kg * 0.033
    if activity_level in ("Moderately Active", "Very Active"):
        base += 0.5
    return round(base, 1)


def get_diet_tips(goal: str, food_pref: str) -> list:
    tips = {
        "Weight Loss": [
            "Eat slowly – it takes 20 min for your brain to register fullness.",
            "Fill half your plate with vegetables at every meal.",
            "Avoid fried snacks – roast or air-fry instead.",
            "Never skip meals; it leads to overeating later.",
            "Keep healthy snacks (fruits, roasted chana) handy.",
        ],
        "Muscle Building": [
            "Aim for 1.6–2.2 g protein per kg bodyweight daily.",
            "Eat within 30–45 min post-workout for muscle repair.",
            "Include a protein source in every meal.",
            "Carbs are not your enemy – they fuel your workouts.",
            "Sleep 7–8 hours – most muscle grows while you sleep.",
        ],
        "Weight Gain": [
            "Eat calorie-dense foods: nuts, dairy, legumes.",
            "Add healthy fats like ghee, peanut butter, avocado.",
            "Have 5–6 meals a day instead of 3 big ones.",
            "Liquid calories (milk, shakes) are easy extra calories.",
            "Don't skip breakfast – it sets your eating tone for the day.",
        ],
        "General Fitness": [
            "Follow the 80/20 rule – eat healthy 80% of the time.",
            "Cook meals at home when possible.",
            "Read food labels; avoid hidden sugars.",
            "Include a rainbow of vegetables throughout the week.",
            "Stay hydrated – dehydration masquerades as hunger.",
        ],
    }
    base = tips.get(goal, tips["General Fitness"])
    veg_tip = "Combine rice/roti with dal/legumes for complete protein." if food_pref != "Non-Vegetarian" else "Prioritise lean meats – chicken breast, fish over red meat."
    base.append(veg_tip)
    return base
