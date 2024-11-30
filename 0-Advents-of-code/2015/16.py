"""Problem 1
Your Aunt Sue has given you a wonderful gift, and you'd like to send her a thank you card. However, there's a small problem: she signed it "From, Aunt Sue".

You have 500 Aunts named "Sue".

So, to avoid sending the card to the wrong person, you need to figure out which Aunt Sue (which you conveniently number 1 to 500, for sanity) gave you the gift. You open the present and, as luck would have it, good ol' Aunt Sue got you a My First Crime Scene Analysis Machine! Just what you wanted. Or needed, as the case may be.

The My First Crime Scene Analysis Machine (MFCSAM for short) can detect a few specific compounds in a given sample, as well as how many distinct kinds of those compounds there are. According to the instructions, these are what the MFCSAM can detect:

children, by human DNA age analysis.
cats. It doesn't differentiate individual breeds.
Several seemingly random breeds of dog: samoyeds, pomeranians, akitas, and vizslas.
goldfish. No other kinds of fish.
trees, all in one group.
cars, presumably by exhaust or gasoline or something.
perfumes, which is handy, since many of your Aunts Sue wear a few kinds.
In fact, many of your Aunts Sue have many of these. You put the wrapping from the gift into the MFCSAM. It beeps inquisitively at you a few times and then prints out a message on ticker tape:

children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1
You make a list of the things you can remember about each Aunt Sue. Things missing from your list aren't zero - you simply don't remember the value.

What is the number of the Sue that got you the gift?
"""

"""Problem 2
As you're about to send the thank you note, something in the MFCSAM's instructions catches your eye. Apparently, it has an outdated retroencabulator, and so the output from the machine isn't exact values - some of them indicate ranges.

In particular, the cats and trees readings indicates that there are greater than that many (due to the unpredictable nuclear decay of cat dander and tree pollen), while the pomeranians and goldfish readings indicate that there are fewer than that many (due to the modial interaction of magnetoreluctance).

What is the number of the real Aunt Sue?
"""

with open("inputs/16.txt", "r") as file:
    strings = file.read().splitlines()

contraints = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}

# Constraints 2: cats <= 7, trees <= 3, pomeranians >= 3, goldfish >= 5

sues_dict = {}
for string in strings:
    _, n, obj_1, n1, obj_2, n2, obj_3, n3 = string.split(" ")
    sues_dict[n[:-1]] = {
        obj_1[:-1]: int(n1[:-1]),
        obj_2[:-1]: int(n2[:-1]),
        obj_3[:-1]: int(n3),
    }

solution = 0
for sue, obj in sues_dict.items():
    if all(obj[key] == contraints[key] for key in obj):
        solution = sue
        break

print("Solution 1:", solution)

# remove cats
contraints.pop("cats")  # cats >= 7
contraints.pop("trees")  # trees >= 3
contraints.pop("pomeranians")  # pomeranians < 3
contraints.pop("goldfish")  # goldfish < 5


for sue, obj in sues_dict.items():
    if all(
        (key in obj and obj[key] == contraints[key]) or key not in obj
        for key in contraints
    ):
        if (
            obj.get("cats", 100) >= 7
            and obj.get("trees", 100) >= 3
            and obj.get("pomeranians", 0) < 3
            and obj.get("goldfish", 0) < 5
        ):
            solution = sue

print("Solution 2:", solution)
