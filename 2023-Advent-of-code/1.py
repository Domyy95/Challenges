from common_code import read_file_lines, extract_k_len_substr

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
words_to_number = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}
def extract_calibration_value(word):
    first_digit = ""
    last_digit = ""
    len_word = len(word)

    # Find the first digit
    for i, char in enumerate(word):
        substrs = extract_k_len_substr(word[0:i], 3)
        substrs += extract_k_len_substr(word[0:i], 4)
        substrs += extract_k_len_substr(word[0:i], 5)
        for substr in substrs:
            if substr in words_to_number:
                first_digit = words_to_number[substr]
                break
        
        if first_digit != "":
            break

        if char.isdigit():
            first_digit = char
            break
        
    # Find the last digit
    for i, char in enumerate(reversed(word)):
        substrs = extract_k_len_substr(word[len_word-i:len_word], 3)
        substrs += extract_k_len_substr(word[len_word-i:len_word], 4)
        substrs += extract_k_len_substr(word[len_word-i:len_word], 5)
        for substr in substrs:
            if substr in words_to_number:
                last_digit = words_to_number[substr]
                break
        
        if last_digit != "":
            break

        if char.isdigit():
            last_digit = char
            break
    
    calibration_value = int(first_digit + last_digit)
    return calibration_value

words = read_file_lines("inputs/1.txt")
sol = 0
for word in words:
    # sol+= extract_calibration_value_numbers(word) # Problem 1 solution
    sol+= extract_calibration_value(word) # Problem 2 solution
print(sol)