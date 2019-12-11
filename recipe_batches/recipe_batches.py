#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    max_batch = 0
    counter = 0
# loop through recipe
# grab corresponding ingredients
    for i in recipe:
        # if ingredient doesn't exist, then return 0
        if i not in ingredients:
            print(f'{i} not found')
            return 0
            # else devide ingredient // recipe item and save value
        elif counter == 0:
            max_batch = max_batch = ingredients[i] // recipe[i]
            print(f'initial set for max_batch {max_batch}')
            # if value is less than  others replace
        elif ingredients[i] // recipe[i] < max_batch:
            max_batch = ingredients[i] // recipe[i]
            print(f'setting max_batch {max_batch}')

        counter += 1
        print(counter)
# return smallest value
    return max_batch


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
