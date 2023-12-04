from common_code import read_file_lines

""" Problem 1
The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

For example:
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet

In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.
"""

def extract_calibration_value_numbers(word):
    first_digit = ""
    last_digit = ""

    # Find the first digit
    for char in word:
        if char.isdigit():
            first_digit = char
            break

    # Find the last digit
    for char in reversed(word):
        if char.isdigit():
            last_digit = char
            break

    calibration_value = int(first_digit + last_digit)
    return calibration_value


""" Problem 2
Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".
"""
spelled_numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
def extract_calibration_value(word):
    for i in range(len(spelled_numbers)):
        if spelled_numbers[i] in word:
            word = word.replace(spelled_numbers[i], spelled_numbers[i][0]+ str(i+1) + spelled_numbers[i][-1])
    
    return extract_calibration_value_numbers(word)

words = read_file_lines("inputs/1.txt")
sol1 = 0
sol2 = 0
for word in words:
    sol1+= extract_calibration_value_numbers(word)  # Problem 1 solution
    sol2+= extract_calibration_value(word)           # Problem 2 solution
print(sol1)
print(sol2)