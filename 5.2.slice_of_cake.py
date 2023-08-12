# The function receives a dictionary of ingredients - the name of the ingredient
# and its price per 100 grams, an optional parameter of a list of products that we will ignore,
# and for each component you will receive an argument bearing the name and the quantity in grams
# that we want and return the price for buying all the ingredients
def get_recipe_price(prices, optionals=[], **ingredients):
    final_price = 0
    for ingredient in ingredients:
        final_price += prices[ingredient] * ingredients.get(ingredient) // 100
    return final_price


if __name__ == '__main__':
    print(get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))
    print(get_recipe_price({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300))
    print(get_recipe_price({}))
