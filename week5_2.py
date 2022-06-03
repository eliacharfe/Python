import functools


def join(*joined_list: list[any], separator='-'):
    """
    The function gets an unlimited number of lists and an optional parameter (called sep) and put it
    between each 2 lists.
    :param joined_list: Lists of arguments.
    :param separator: The parameter to put between each 2 lists.
    :return: A new list with the elements of the lists which between the elements of 2 different
    lists there is sep (or '-' by default).
    """
    if not joined_list:
        return list[any]

    return [argument for lst_args in joined_list for argument in lst_args + [separator]][:-1]


def get_recipe_price(prices: dict, optionals=[], **ingredients):
    """
    This function calculates how much we need to pay for the ingredients passed (with their price
    and quantity for 100g) in order to form a recipe.
    :param prices: A dictionary of ingredients with their prices (the values are their price for 100g).
    :param optionals: An optional parameter that gets a list of ingredients to ignore.
    :param ingredients: In each argument passed in the parameter we specify the name of the ingredient
    and its value is the amount (in grams) that we need to buy for the recipe.
    """
    if not prices and not ingredients:
        return 0

    return functools.reduce(lambda prices_sum, next_price: prices_sum + next_price,
                            [ingredients[price] * prices[price] // 100
                             for price in prices if price not in optionals])


if __name__ == '__main__':
    print(join([1, 2], [8], [9, 5, 6], separator='@'))
    print(join([1, 2], [8], [9, 5, 6]))
    print(join([1]))
    print(join())
    print("-----------------------------------------")

    print(get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))
    print(get_recipe_price({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300))
    print(get_recipe_price({}))


