from common_code import read_file_lines
import string
""" Problem 1
The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)

Here is an example engine schematic:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

What is the sum of all of the part numbers in the engine schematic?
"""

def check_adjacent(matrix, i, cols, symbols):
    if len(cols) == 0:
        return False
    
    if cols[0] > 0:
        cols.append(cols[0]-1)
        cols.sort()
    if cols[-1] < len(matrix[0])-1:
        cols.append(cols[-1]+1)
        cols.sort()

    for col in cols:
        if i>0 and matrix[i-1][col] in symbols:
            return i-1, col
        if i<len(matrix)-1 and matrix[i+1][col] in symbols:
            return i+1, col
    
    if cols[0]>0 and matrix[i][cols[0]] in symbols:
        return i, cols[0]
    
    if cols[-1]<len(matrix[0])-1 and matrix[i][cols[-1]] in symbols:
        return i, cols[-1]
    
    return False

def solve_matrix_sum(matrix, symbols):
    cols = len(matrix[0])
    solution = 0
    for i,line in enumerate(matrix):
        col = 0
        while col<cols:
            new_number = ""
            pos_to_check = []
            while col<cols and line[col].isdigit():
                pos_to_check.append(col)
                new_number += line[col]
                col+=1
            if new_number != "" and check_adjacent(matrix, i, pos_to_check, symbols):
                solution += int(new_number)
            col+=1

    return solution

""" Problem 2
The missing part wasn't the only issue - one of the gears in the engine is wrong. A gear is any * symbol that is adjacent to exactly two part numbers. Its gear ratio is the result of multiplying those two numbers together.

This time, you need to find the gear ratio of every gear and add them all up so that the engineer can figure out which gear needs to be replaced.

Consider the same engine schematic again:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
In this schematic, there are two gears. The first is in the top left; it has part numbers 467 and 35, so its gear ratio is 16345. The second gear is in the lower right; its gear ratio is 451490. (The * adjacent to 617 is not a gear because it is only adjacent to one part number.) Adding up all of the gear ratios produces 467835.
"""
def find_number_around(matrix, number_i, number_cols, symbol_i, symbol_j):
    to_check = [(symbol_i-1, symbol_j-1), (symbol_i-1, symbol_j), (symbol_i-1, symbol_j+1), 
                (symbol_i, symbol_j-1), (symbol_i, symbol_j+1), 
                (symbol_i+1, symbol_j-1), (symbol_i+1, symbol_j), (symbol_i+1, symbol_j+1)]
    
    # excluce the number itself
    to_check = [(i, j) for i, j in to_check if not (i == number_i and j in number_cols)]

    for i, j in to_check:
        if i>=0 and i<len(matrix) and j>=0 and j<len(matrix[0]) and matrix[i][j].isdigit():
            result = matrix[i][j]
            # left 
            z = 1
            while j-z>=0 and matrix[i][j-z].isdigit():
                result = f"{matrix[i][j-z]}{result}"
                z+=1
            
            # right
            z = 1
            while j+z<len(matrix[0]) and matrix[i][j+z].isdigit():
                result = f"{result}{matrix[i][j+z]}"
                z+=1

            return int(result)
        
    return 0


def solve_matrix_mul(matrix, symbol = "*"):
    cols = len(matrix[0])
    solution = 0
    for i,line in enumerate(matrix):
        col = 0
        while col<cols:
            new_number = ""
            pos_to_check = []
            while col<cols and line[col].isdigit():
                pos_to_check.append(col)
                new_number += line[col]
                col+=1
            adjacent = check_adjacent(matrix, i, pos_to_check, [symbol])
            if new_number != "" and adjacent:
                other_number = find_number_around(matrix, i, pos_to_check, adjacent[0], adjacent[1])
                #print(other_number, new_number)
                solution += int(new_number) * other_number
            col+=1

    return solution/2

matrix_problem = []
lines = read_file_lines("inputs/3.txt")
for line in lines:
    matrix_problem.append(list(line))

# sol 1
symbols_to_use = list(string.punctuation)
symbols_to_use.remove(".")
sol = solve_matrix_sum(matrix_problem, symbols_to_use)
print(sol)

# sol 2
sol = solve_matrix_mul(matrix_problem)
print(sol)
