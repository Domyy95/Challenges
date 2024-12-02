"""Problem 1
Santa needs help figuring out which strings in his text file are naughty or nice.

A nice string is one with all of the following properties:

It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
For example:

ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings.
aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
jchzalrnumimnmhp is naughty because it has no double letter.
haegwjzuvuyypxyu is naughty because it contains the string xy.
dvszwmarrgswjxmb is naughty because it contains only one vowel.
How many strings are nice?
"""

"""Problem 2
Realizing the error of his ways, Santa has switched to a better model of determining whether a string is naughty or nice. None of the old rules apply, as they are all clearly ridiculous.

Now, a nice string is one with all of the following properties:

It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.
For example:

qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a letter that repeats with exactly one letter between them (zxz).
xxyxx is nice because it has a pair that appears twice and a letter that repeats with one between, even though the letters used by each rule overlap.
uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a single letter between them.
ieodomkazucvgmuy is naughty because it has a repeating letter with one between (odo), but no pair that appears twice.
How many strings are nice under these new rules?
"""

vowels = "aeiou"
forbidden = ["ab", "cd", "pq", "xy"]


def is_nice(string, forbidden: list = forbidden, must_have: str = vowels):
    if sum([string.count(vowel) for vowel in must_have]) < 3:
        return False
    if not any([string[i] == string[i + 1] for i in range(len(string) - 1)]):
        return False
    if any([forbid in string for forbid in forbidden]):
        return False
    return True


def is_nice_2(string):
    if not any([string[i : i + 2] in string[i + 2 :] for i in range(len(string) - 2)]):
        return False
    if not any([string[i] == string[i + 2] for i in range(len(string) - 2)]):
        return False
    return True


with open("inputs/5.txt", "r") as file:
    strings = file.read().splitlines()

result1 = 0
result2 = 0
for string in strings:
    result1 += is_nice(string)
    result2 += is_nice_2(string)

print("Solution 1: ", result1)
print("Solution 2: ", result2)
