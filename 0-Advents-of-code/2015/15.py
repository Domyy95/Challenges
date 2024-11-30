"""Problem 1
Today, you set out on the task of perfecting your milk-dunking cookie recipe. All you have to do is find the right balance of ingredients.

Your recipe leaves room for exactly 100 teaspoons of ingredients. You make a list of the remaining ingredients you could use to finish the recipe (your puzzle input) and their properties per teaspoon:

capacity (how well it helps the cookie absorb milk)
durability (how well it keeps the cookie intact when full of milk)
flavor (how tasty it makes the cookie)
texture (how it improves the feel of the cookie)
calories (how many calories it adds to the cookie)
You can only measure ingredients in whole-teaspoon amounts accurately, and you have to be accurate so you can reproduce your results in the future. The total score of a cookie can be found by adding up each of the properties (negative totals become 0) and then multiplying together everything except calories.

For instance, suppose you have these two ingredients:

Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
Then, choosing to use 44 teaspoons of butterscotch and 56 teaspoons of cinnamon (because the amounts of each ingredient must add up to 100) would result in a cookie with the following properties:

A capacity of 44*-1 + 56*2 = 68
A durability of 44*-2 + 56*3 = 80
A flavor of 44*6 + 56*-2 = 152
A texture of 44*3 + 56*-1 = 76
Multiplying these together (68 * 80 * 152 * 76, ignoring calories for now) results in a total score of 62842880, which happens to be the best score possible given these ingredients. If any properties had produced a negative total, it would have instead become zero, causing the whole score to multiply to zero.

Given the ingredients in your kitchen and their properties, what is the total score of the highest-scoring cookie you can make?
"""

"""Problem 2
Your cookie recipe becomes wildly popular! Someone asks if you can make another recipe that has exactly 500 calories per cookie (so they can use it as a meal replacement). Keep the rest of your award-winning process the same (100 teaspoons, same ingredients, same scoring system).

For example, given the ingredients above, if you had instead selected 40 teaspoons of butterscotch and 60 teaspoons of cinnamon (which still adds to 100), the total calorie count would be 40*8 + 60*3 = 500. The total score would go down, though: only 57600000, the best you can do in such trying circumstances.

Given the ingredients in your kitchen and their properties, what is the total score of the highest-scoring cookie you can make with a calorie total of 500?
"""


input = """Sprinkles: capacity 2, durability 0, flavor -2, texture 0, calories 3
Butterscotch: capacity 0, durability 5, flavor -3, texture 0, calories 3
Chocolate: capacity 0, durability 0, flavor 5, texture -1, calories 8
Candy: capacity 0, durability -1, flavor 0, texture 5, calories 8"""

max_spoons = 100

ingredients = {}
for line in input.split("\n"):
    ingredient, _, capacity, _, durability, _, flavor, _, texture, _, calories = (
        line.split()
    )
    ingredients[ingredient[:-1]] = (
        int(capacity[:-1]),
        int(durability[:-1]),
        int(flavor[:-1]),
        int(texture[:-1]),
        int(calories),
    )

max_score = 0
max_score_500_calories = 0
for sprinkles in range(max_spoons + 1):
    for butterscotch in range(max_spoons - sprinkles + 1):
        for chocolate in range(max_spoons - sprinkles - butterscotch + 1):
            candy = max_spoons - sprinkles - butterscotch - chocolate
            capacity = (
                sprinkles * ingredients["Sprinkles"][0]
                + butterscotch * ingredients["Butterscotch"][0]
                + chocolate * ingredients["Chocolate"][0]
                + candy * ingredients["Candy"][0]
            )
            durability = (
                sprinkles * ingredients["Sprinkles"][1]
                + butterscotch * ingredients["Butterscotch"][1]
                + chocolate * ingredients["Chocolate"][1]
                + candy * ingredients["Candy"][1]
            )
            flavor = (
                sprinkles * ingredients["Sprinkles"][2]
                + butterscotch * ingredients["Butterscotch"][2]
                + chocolate * ingredients["Chocolate"][2]
                + candy * ingredients["Candy"][2]
            )
            texture = (
                sprinkles * ingredients["Sprinkles"][3]
                + butterscotch * ingredients["Butterscotch"][3]
                + chocolate * ingredients["Chocolate"][3]
                + candy * ingredients["Candy"][3]
            )
            calories = (
                sprinkles * ingredients["Sprinkles"][4]
                + butterscotch * ingredients["Butterscotch"][4]
                + chocolate * ingredients["Chocolate"][4]
                + candy * ingredients["Candy"][4]
            )
            score = (
                max(0, capacity) * max(0, durability) * max(0, flavor) * max(0, texture)
            )

            max_score = max(max_score, score)
            if calories == 500:
                max_score_500_calories = max(max_score_500_calories, score)

print("Solution 1: ", max_score)
print("Solution 2: ", max_score_500_calories)
