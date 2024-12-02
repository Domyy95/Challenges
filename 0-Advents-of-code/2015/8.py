"""Problem 1
Not wrote the problems because it gives a python error for the format
https://adventofcode.com/2015/day/8
"""

"""Problem 2
Now, let's go the other way. In addition to finding the number of characters of code, you should now encode each code representation as a new string and find the number of characters of the new encoded representation, including the surrounding double quotes.

For example:

"" encodes to "\"\"", an increase from 2 characters to 6.
"abc" encodes to "\"abc\"", an increase from 5 characters to 9.
"aaa\"aaa" encodes to "\"aaa\\\"aaa\"", an increase from 10 characters to 16.
"\x27" encodes to "\"\\x27\"", an increase from 6 characters to 11.
Your task is to find the total number of characters to represent the newly encoded strings minus the number of characters of code in each original string literal. For example, for the strings above, the total encoded length (6 + 9 + 16 + 11 = 42) minus the characters in the original code representation (23, just like in the first part of this puzzle) is 42 - 23 = 19.
"""

with open("inputs/8.txt", "r") as file:
    strings = file.read().splitlines()

result1 = 0
result2 = 0
for string in strings:
    result1 += len(string)
    result1 -= len(eval(string))
    result2 += 2
    result2 += string.count('"')
    result2 += string.count("\\")

print("Solution 1: ", result1)
print("Solution 2: ", result2)
