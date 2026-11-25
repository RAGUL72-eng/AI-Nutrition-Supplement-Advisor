ACTIVITY_FACTORS = {
    "Sedentary": 1.2,
    "Lightly active": 1.375,
    "Moderately active": 1.55,
    "Very active": 1.725,
    "Extra active": 1.9,
}

def calculate_targets(profile):
    """Estimate calorie and macro targets using Mifflin-St Jeor."""
    weight = float(profile["weight_kg"])
    height = float(profile["height_cm"])
    age = int(profile["age"])

    if profile["sex"] == "Male":
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161

    maintenance = bmr * ACTIVITY_FACTORS.get(profile["activity"], 1.2)
    goal = profile.get("goal", "Maintain weight")
    if goal == "Lose weight":
        calories = maintenance - 300
    elif goal == "Gain weight":
        calories = maintenance + 250
    else:
        calories = maintenance

    calories = max(1200, round(calories))
    # General starting estimate: 1.6 g protein/kg, 25% calories from fat.
    protein_g = round(weight * 1.6)
    fat_g = round((calories * 0.25) / 9)
    carbs_g = round(max(0, calories - protein_g * 4 - fat_g * 9) / 4)

    return {
        "bmr": round(bmr),
        "maintenance_calories": round(maintenance),
        "calories": calories,
        "protein_g": protein_g,
        "carbs_g": carbs_g,
        "fat_g": fat_g,
    }
