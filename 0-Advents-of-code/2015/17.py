"""Problem 1
The elves bought too much eggnog again - 150 liters this time. To fit it all into your refrigerator, you'll need to move it into smaller containers. You take an inventory of the capacities of the available containers.

For example, suppose you have containers of size 20, 15, 10, 5, and 5 liters. If you need to store 25 liters, there are four ways to do it:

15 and 10
20 and 5 (the first 5)
20 and 5 (the second 5)
15, 5, and 5
Filling all containers entirely, how many different combinations of containers can exactly fit all 150 liters of eggnog?
"""

"""Problem 2
While playing with all the containers in the kitchen, another load of eggnog arrives! The shipping and receiving department is requesting as many containers as you can spare.

Find the minimum number of containers that can exactly fit all 150 liters of eggnog. How many different ways can you fill that number of containers and still hold exactly 150 litres?

In the example above, the minimum number of containers was two. There were three ways to use that many containers, and so the answer there would be 3.
"""

input = [50, 44, 11, 49, 42, 46, 18, 32, 26, 40, 21, 7, 18, 43, 10, 47, 36, 24, 22, 40]

liters = 150


def find_combinations(liters, containers):
    if liters == 0:
        return True
    if liters < 0 or not containers:
        return False
    return find_combinations(
        liters - containers[0], containers[1:]
    ) + find_combinations(liters, containers[1:])


solution = find_combinations(liters, input)
print("Solution 1:", solution)


def find_min_combinations(liters, containers, containers_used=0):
    if liters == 0 and containers_used == 4:
        return 1
    if liters < 0 or not containers:
        return 0
    return find_min_combinations(
        liters - containers[0], containers[1:], containers_used + 1
    ) + find_min_combinations(liters, containers[1:], containers_used)


solution = find_min_combinations(liters, input)
print("Solution 2:", solution)
