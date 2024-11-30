"""Problem 1
In years past, the holiday feast with your family hasn't gone so well. Not everyone gets along! This year, you resolve, will be different. You're going to find the optimal seating arrangement and avoid all those awkward conversations.

You start by writing up a list of everyone invited and the amount their happiness would increase or decrease if they were to find themselves sitting next to each other person. You have a circular table that will be just big enough to fit everyone comfortably, and so each person will have exactly two neighbors.

For example, suppose you have only four attendees planned, and you calculate their potential happiness as follows:

Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol.
Then, if you seat Alice next to David, Alice would lose 2 happiness units (because David talks so much), but David would gain 46 happiness units (because Alice is such a good listener), for a total change of 44.

If you continue around the table, you could then seat Bob next to Alice (Bob gains 83, Alice gains 54). Finally, seat Carol, who sits next to Bob (Carol gains 60, Bob loses 7) and David (Carol gains 55, David gains 41). The arrangement looks like this:

     +41 +46
+55   David    -2
Carol       Alice
+60    Bob    +54
     -7  +83
After trying every other seating arrangement in this hypothetical scenario, you find that this one is the most optimal, with a total change in happiness of 330.

What is the total change in happiness for the optimal seating arrangement of the actual guest list?
"""

"""Problem 2
In all the commotion, you realize that you forgot to seat yourself. At this point, you're pretty apathetic toward the whole thing, and your happiness wouldn't really go up or down regardless of who you sit next to. You assume everyone else would be just as ambivalent about sitting next to you, too.

So, add yourself to the list, and give all happiness relationships that involve you a score of 0.

What is the total change in happiness for the optimal seating arrangement that actually includes yourself?
"""
from itertools import permutations

with open("inputs/13.txt", "r") as file:
    strings = file.read().splitlines()


def parse_input(strings):
    happiness = {}
    people = set()
    for string in strings:
        string = string.split()
        person1 = string[0]
        person2 = string[-1][:-1]  # -1 to remove the dot
        people.add(person1)
        people.add(person2)
        if string[2] == "lose":
            happiness[(person1, person2)] = -int(string[3])
        else:
            happiness[(person1, person2)] = int(string[3])
    return people, happiness


def solve(people, happiness_dict):
    possible_seats = permutations(people)
    max_happiness = 0
    for seat in possible_seats:
        happiness = 0
        for i in range(len(seat)):
            happiness += happiness_dict[(seat[i], seat[(i + 1) % len(seat)])]
            happiness += happiness_dict[(seat[i], seat[(i - 1) % len(seat)])]
        max_happiness = max(max_happiness, happiness)
    return max_happiness


people, happiness_dict = parse_input(strings)
solution = solve(people, happiness_dict)
print("Solution 1: ", solution)

# Part 2
for person in people:
    happiness_dict[("Me", person)] = 0
    happiness_dict[(person, "Me")] = 0

people.add("Me")
solution = solve(people, happiness_dict)
print("Solution 2: ", solution)
