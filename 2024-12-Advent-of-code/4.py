"""Problem 1
"Looks like the Chief's not here. Next!" One of The Historians pulls out a device and pushes the only button on it. After a brief flash, you recognize the interior of the Ceres monitoring station!

As the search for the Chief continues, a small Elf who lives on the station tugs on your shirt; she'd like to know if you could help her with her word search (your puzzle input). She only has to find one word: XMAS.

This word search allows words to be horizontal, vertical, diagonal, written backwards, or even overlapping other words. It's a little unusual, though, as you don't merely need to find one instance of XMAS - you need to find all of them. Here are a few ways XMAS might appear, where irrelevant characters have been replaced with .:


..X...
.SAMX.
.A..A.
XMAS.S
.X....
The actual word search will be full of letters instead. For example:

MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
In this word search, XMAS occurs a total of 18 times; here's the same word search again, but where letters not involved in any XMAS have been replaced with .:

....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX
Take a look at the little Elf's word search. How many times does XMAS appear?
"""

"""Problem 2
The Elf looks quizzically at you. Did you misunderstand the assignment?

Looking for the instructions, you flip over the word search to find that this isn't actually an XMAS puzzle; it's an X-MAS puzzle in which you're supposed to find two MAS in the shape of an X. One way to achieve that is like this:

M.S
.A.
M.S
Irrelevant characters have again been replaced with . in the above diagram. Within the X, each MAS can be written forwards or backwards.

Here's the same example from before, but this time all of the X-MASes have been kept instead:

.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........
In this example, an X-MAS appears 9 times.

Flip the word search from the instructions back over to the word search side and try again. How many times does an X-MAS appear?
"""


def find_all_words(lines, word_to_find):
    result = 0
    # horizontal
    for line in lines:
        result += line.count(word_to_find) + line.count(word_to_find[::-1])

    # vertical
    vertical = ["".join(col) for col in zip(*lines)]
    for line in vertical:
        result += line.count(word_to_find) + line.count(word_to_find[::-1])

    # diagonals
    rows, cols = len(lines), len(lines[0])
    word_len = len(word_to_find)
    for i in range(rows):
        for j in range(cols):
            if i + word_len <= rows and j + word_len <= cols:
                diag = "".join([lines[i + k][j + k] for k in range(word_len)])
                result += diag.count(word_to_find) + diag.count(word_to_find[::-1])

            # reverse diagonal
            if i + word_len <= rows and j - word_len >= -1:
                diag = "".join([lines[i + k][j - k] for k in range(word_len)])
                result += diag.count(word_to_find) + diag.count(word_to_find[::-1])

    return result


def find_all_x_shapes(lines):
    middle_char = "A"
    result = 0
    rows, cols = len(lines), len(lines[0])
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if lines[i][j] == middle_char:
                if (
                    lines[i - 1][j - 1] == lines[i - 1][j + 1] == "M"
                    and lines[i + 1][j - 1] == lines[i + 1][j + 1] == "S"
                ):
                    result += 1
                elif (
                    lines[i - 1][j - 1] == lines[i + 1][j - 1] == "M"
                    and lines[i - 1][j + 1] == lines[i + 1][j + 1] == "S"
                ):
                    result += 1
                elif (
                    lines[i + 1][j - 1] == lines[i + 1][j + 1] == "M"
                    and lines[i - 1][j - 1] == lines[i - 1][j + 1] == "S"
                ):
                    result += 1
                elif (
                    lines[i - 1][j + 1] == lines[i + 1][j + 1] == "M"
                    and lines[i + 1][j - 1] == lines[i - 1][j - 1] == "S"
                ):
                    result += 1

    return result


with open("inputs/4.txt") as f:
    input = f.read().strip()

lines = input.split("\n")
result = find_all_words(lines, "XMAS")
print("Solution 1:", result)
result = find_all_x_shapes(lines)
print("Solution 2:", result)


# Amazing solution found on Reddit
def solve(data, slices, variants):
    count = 0

    for y in range(len(data)):
        for x in range(len(data[0])):
            for slice in slices:
                try:
                    word = "".join([data[y + dy][x + dx] for dx, dy in slice])

                    if word in variants:
                        count += 1
                except:
                    pass

    return count


slices1 = [
    ((0, 0), (1, 0), (2, 0), (3, 0)),  # horizontal
    ((0, 0), (0, 1), (0, 2), (0, 3)),  # vertical
    ((0, 0), (1, 1), (2, 2), (3, 3)),  # diagonal
    ((0, 3), (1, 2), (2, 1), (3, 0)),  # other diagonal
]

slices2 = [
    ((0, 0), (1, 1), (2, 2), (0, 2), (2, 0)),  # x-shape
]

part1 = solve(lines, slices1, {"XMAS", "SAMX"})
part2 = solve(lines, slices2, {"MASMS", "SAMSM", "MASSM", "SAMMS"})
print(part1, part2)
