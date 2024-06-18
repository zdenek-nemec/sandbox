from unittest import TestCase


def cakes(recipe: dict, available: dict) -> int:
    """Or one-liner return min(available.get(k, 0)/recipe[k] for k in recipe)"""
    max_cakes = {}
    for ingredient in recipe.keys():
        if ingredient not in available:
            return 0
        max_cakes[ingredient] = available[ingredient] // recipe[ingredient]
    return min(max_cakes.values())


def main():
    print("Pete, the baker")

    print(f'{cakes({"flour": 500, "sugar": 200, "eggs": 1}, {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}) = }')
    print(f'{cakes({"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}, {"sugar": 500, "flour": 2000, "milk": 2000}) = }')

    recipe = {"flour": 500, "sugar": 200, "eggs": 1}
    available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
    TestCase().assertEqual(cakes(recipe, available), 2, 'example #1')

    recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
    available = {"sugar": 500, "flour": 2000, "milk": 2000}
    TestCase().assertEqual(cakes(recipe, available), 0, 'example #2')


if __name__ == "__main__":
    main()
