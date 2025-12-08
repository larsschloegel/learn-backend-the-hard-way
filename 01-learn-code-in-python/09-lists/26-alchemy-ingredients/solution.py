def check_ingredient_match(recipe, inventory):
    correct = 0
    missing = []
    for ingredient in recipe:
        if ingredient in inventory:
            correct += 1
        else:
            missing.append(ingredient)
    percentage = correct / len(recipe) * 100
    return percentage, missing


# my solution
def check_ingredient_match(recipe, inventory):
    missing_incredients = []
    for item in recipe:
        if item not in inventory:
            missing_incredients.append(item)
    percentage_of_required_ingredients = (len(recipe) - len(missing_incredients)) / len(recipe) * 100
    return percentage_of_required_ingredients, missing_incredients,
