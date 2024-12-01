"""Problem 1
After the million lights incident, the fire code has gotten stricter: now, at most ten thousand lights are allowed. You arrange them in a 100x100 grid.

Never one to let you down, Santa again mails you instructions on the ideal lighting configuration. With so few lights, he says, you'll have to resort to animation.

Start by setting your lights to the included initial configuration (your puzzle input). A # means "on", and a . means "off".

Then, animate your grid in steps, where each step decides the next configuration based on the current one. Each light's next state (either on or off) depends on its current state and the current states of the eight lights adjacent to it (including diagonals). Lights on the edge of the grid might have fewer than eight neighbors; the missing ones always count as "off".

For example, in a simplified 6x6 grid, the light marked A has the neighbors numbered 1 through 8, and the light marked B, which is on an edge, only has the neighbors marked 1 through 5:

1B5...
234...
......
..123.
..8A4.
..765.
The state a light should have next is based on its current state (on or off) plus the number of neighbors that are on:

A light which is on stays on when 2 or 3 neighbors are on, and turns off otherwise.
A light which is off turns on if exactly 3 neighbors are on, and stays off otherwise.
All of the lights update simultaneously; they all consider the same current state before moving to the next.

Here's a few steps from an example configuration of another 6x6 grid:

Initial state:
.#.#.#
...##.
#....#
..#...
#.#..#
####..

After 1 step:
..##..
..##.#
...##.
......
#.....
#.##..

After 2 steps:
..###.
......
..###.
......
.#....
.#....

After 3 steps:
...#..
......
...#..
..##..
......
......

After 4 steps:
......
......
..##..
..##..
......
......
After 4 steps, this example has four lights on.

In your grid of 100x100 lights, given your initial configuration, how many lights are on after 100 steps?
"""

"""Problem 2
You flip the instructions over; Santa goes on to point out that this is all just an implementation of Conway's Game of Life. At least, it was, until you notice that something's wrong with the grid of lights you bought: four lights, one in each corner, are stuck on and can't be turned off. The example above will actually run like this:

Initial state:
##.#.#
...##.
#....#
..#...
#.#..#
####.#

After 1 step:
#.##.#
####.#
...##.
......
#...#.
#.####

After 2 steps:
#..#.#
#....#
.#.##.
...##.
.#..##
##.###

After 3 steps:
#...##
####.#
..##.#
......
##....
####.#

After 4 steps:
#.####
#....#
...#..
.##...
#.....
#.#..#

After 5 steps:
##.###
.##..#
.##...
.##...
#.#...
##...#
After 5 steps, this example now has 17 lights on.

In your grid of 100x100 lights, given your initial configuration, but with the four corners always in the on state, how many lights are on after 100 steps?
"""


def count_neighbors(grid, x, y):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if 0 <= x + i < len(grid) and 0 <= y + j < len(grid[0]):
                if grid[x + i][y + j] == "#":
                    count += 1
    return count


def step(grid):
    new_grid = []
    for i in range(len(grid)):
        row = ""
        for j in range(len(grid[0])):
            count = count_neighbors(grid, i, j)
            if grid[i][j] == "#":
                if count == 2 or count == 3:
                    row += "#"
                else:
                    row += "."
            else:
                if count == 3:
                    row += "#"
                else:
                    row += "."
        new_grid.append(row)
    return new_grid


def step_borders_always_on(grid):
    new_grid = []
    for i in range(len(grid)):
        row = ""
        for j in range(len(grid[0])):
            if (i == 0 or i == len(grid) - 1) and (j == 0 or j == len(grid[0]) - 1):
                row += "#"
                continue

            count = count_neighbors(grid, i, j)
            if grid[i][j] == "#":
                if count == 2 or count == 3:
                    row += "#"
                else:
                    row += "."
            else:
                if count == 3:
                    row += "#"
                else:
                    row += "."
        new_grid.append(row)

    return new_grid


with open("inputs/18.txt", "r") as file:
    start_grid = file.read().strip().split("\n")

steps = 100

grid_1 = start_grid.copy()
grid_2 = start_grid.copy()
grid_2[0] = "#" + grid_2[0][1:-1] + "#"
grid_2[-1] = "#" + grid_2[-1][1:-1] + "#"
for _ in range(steps):
    grid_1 = step(grid_1)
    grid_2 = step_borders_always_on(grid_2)

solution = sum(row.count("#") for row in grid_1)
print("Solution 1:", solution)

solution = sum(row.count("#") for row in grid_2)
print("Solution 2:", solution)
