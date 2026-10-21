MEALS = {
    "vegetarian": {"breakfast":"Oats with fruit and nuts", "lunch":"Dal, rice and seasonal vegetables", "dinner":"Paneer or tofu with vegetable roti wrap", "snack":"Roasted chana or seasonal fruit"},
    "vegan": {"breakfast":"Oats with soy milk and fruit", "lunch":"Chickpea curry, rice and vegetables", "dinner":"Tofu and vegetable roti wrap", "snack":"Roasted chana or seasonal fruit"},
    "non-vegetarian": {"breakfast":"Eggs with whole-grain toast and fruit", "lunch":"Rice, vegetables and chicken or beans", "dinner":"Vegetable bowl with fish, chicken or tofu", "snack":"Yogurt or seasonal fruit"}
}

def build_meal_plan(goal: str, diet: str, allergies: list[str], disliked_foods: list[str]) -> dict:
    meals = MEALS.get(diet.strip().lower(), MEALS["vegetarian"]).copy()
    excluded = {x.strip().lower() for x in allergies + disliked_foods}
    for slot, meal in meals.items():
        if any(x and x in meal.lower() for x in excluded): meals[slot] = "Choose an alternative excluding your listed allergy/disliked foods."
    return {"module":"meal-planner", "goal":goal, "diet":diet, "meals":meals, "disclaimer":"General meal ideas only, not medical nutrition advice. Verify ingredients and cross-contamination for allergies."}

def make_recipe(ingredients: list[str], diet: str) -> dict:
    cleaned = [x.strip() for x in ingredients if x.strip()]
    return {"module":"recipe-guidance", "diet":diet, "ingredients_received":cleaned, "suggestion":f"Prepare a simple bowl or stir-fry using {', '.join(cleaned)}. Wash produce, avoid cross-contamination, and cook ingredients thoroughly.", "note":"Rule-based starter template, not LLaMA-generated advice."}
