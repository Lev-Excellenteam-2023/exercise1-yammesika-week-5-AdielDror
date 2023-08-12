# The function receives a dictionary of ingredients - the name of the ingredient
# and its price per 100 grams, an optional parameter of a list of products that we will ignore,
# and for each component you will receive an argument bearing the name and the quantity in grams
# that we want and return the price for buying all the ingredients
def get_recipe_price(prices, optionals=[], **ingredients):
    final_price = 0
    for ingredient in ingredients:
        final_price += prices[ingredient] * ingredients.get(ingredient) // 100
    print(final_price)
    return final_price


get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100)
get_recipe_price({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300)
get_recipe_price({})
