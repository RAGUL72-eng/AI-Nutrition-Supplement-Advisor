def build_meal_plan(calories, dietary="No preference"):
    """Return a flexible example meal plan; portions should be adjusted."""
    if dietary == "Vegan":
        meals = {
            "Breakfast": ["Oats with soy milk", "Banana", "Chia seeds"],
            "Lunch": ["Lentil or chickpea bowl", "Brown rice", "Mixed vegetables"],
            "Snack": ["Fruit", "Roasted chickpeas"],
            "Dinner": ["Tofu or beans", "Whole-grain roti", "Vegetable curry"],
        }
    elif dietary == "Vegetarian":
        meals = {
            "Breakfast": ["Oats or idli", "Milk or curd", "Fruit"],
            "Lunch": ["Dal", "Rice or roti", "Vegetables", "Curd"],
            "Snack": ["Fruit", "Nuts or yogurt"],
            "Dinner": ["Paneer/tofu", "Roti", "Vegetable side"],
        }
    elif dietary == "Eggetarian":
        meals = {
            "Breakfast": ["Eggs", "Whole-grain toast or dosa", "Fruit"],
            "Lunch": ["Dal", "Rice or roti", "Vegetables", "Curd"],
            "Snack": ["Yogurt", "Fruit"],
            "Dinner": ["Egg curry or paneer", "Roti", "Vegetables"],
        }
    else:
        meals = {
            "Breakfast": ["Eggs or yogurt", "Oats or whole-grain toast", "Fruit"],
            "Lunch": ["Chicken, fish, beans, or tofu", "Rice or roti", "Vegetables"],
            "Snack": ["Fruit", "Nuts or yogurt"],
            "Dinner": ["Lean protein", "Potato/rice/roti", "Vegetables"],
        }

    # Keep calories as a planning reference rather than claim exact meal calories.
    meals["Daily target"] = [f"Approximate target: {int(calories):,} kcal/day; adjust portion sizes to fit."]
    return meals
