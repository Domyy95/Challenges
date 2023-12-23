""" Problem 1
In short: if you move the rocks, you can focus the dish. The platform even has a control panel on the side that lets you tilt it in one of four directions! The rounded rocks (O) will roll when the platform is tilted, while the cube-shaped rocks (#) will stay in place. You note the positions of all of the empty spaces (.) and rocks (your puzzle input). For example:

O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
Start by tilting the lever so all of the rocks will slide north as far as they will go:

OOOO.#.O..
OO..#....#
OO..O##..O
O..#.OO...
........#.
..#....#.#
..O..#.O.O
..O.......
#....###..
#....#....
You notice that the support beams along the north side of the platform are damaged; to ensure the platform doesn't collapse, you should calculate the total load on the north support beams.

The amount of load caused by a single rounded rock (O) is equal to the number of rows from the rock to the south edge of the platform, including the row the rock is on. (Cube-shaped rocks (#) don't contribute to load.) So, the amount of load caused by each rock in each row is as follows:

OOOO.#.O.. 10
OO..#....#  9
OO..O##..O  8
O..#.OO...  7
........#.  6
..#....#.#  5
..O..#.O.O  4
..O.......  3
#....###..  2
#....#....  1
The total load is the sum of the load caused by all of the rounded rocks. In this example, the total load is 136.

Tilt the platform so that the rounded rocks all roll north. Afterward, what is the total load on the north support beams?
"""

""" Problem 2
The parabolic reflector dish deforms, but not in a way that focuses the beam. To do that, you'll need to move the rocks to the edges of the platform. Fortunately, a button on the side of the control panel labeled "spin cycle" attempts to do just that!

Each cycle tilts the platform four times so that the rounded rocks roll north, then west, then south, then east. After each tilt, the rounded rocks roll as far as they can before the platform tilts in the next direction. After one cycle, the platform will have finished rolling the rounded rocks in those four directions in that order.

Here's what happens in the example above after each of the first few cycles:

After 1 cycle:
.....#....
....#...O#
...OO##...
.OO#......
.....OOO#.
.O#...O#.#
....O#....
......OOOO
#...O###..
#..OO#....

After 2 cycles:
.....#....
....#...O#
.....##...
..O#......
.....OOO#.
.O#...O#.#
....O#...O
.......OOO
#..OO###..
#.OOO#...O

After 3 cycles:
.....#....
....#...O#
.....##...
..O#......
.....OOO#.
.O#...O#.#
....O#...O
.......OOO
#...O###.O
#.OOO#...O
This process should work if you leave it running long enough, but you're still worried about the north support beams. To make sure they'll survive for a while, you need to calculate the total load on the north support beams after 1000000000 cycles.

In the above example, after 1000000000 cycles, the total load on the north support beams is 64.

Run the spin cycle for 1000000000 cycles. Afterward, what is the total load on the north support beams?


"""

CYCLES = 1000000000

with open("inputs/14.txt", "r") as file:
    input = tuple(file.read().splitlines())


def slide_rocks_north(grid):
    # transpose
    grid = list(map("".join, zip(*grid)))
    new_grid = []

    for row in grid:
        ordered_rows = []
        for group in row.split("#"):
            ordered_rows.append("".join(sorted(group, reverse=True)))

        new_grid.append("#".join(ordered_rows))

    return tuple(list(map("".join, zip(*new_grid))))


def print_grid(grid):
    for row in grid:
        print(row)
    print()


# 1 cycle = move rocks north, west, south, east
def cycle(grid):
    for _ in range(4):
        grid = slide_rocks_north(grid)
        # rotare 90 degrees
        grid = tuple(["".join(row[::-1]) for row in zip(*grid)])

    return grid


solution1 = 0
solution2 = 0

grid_slided = slide_rocks_north(input)
solution1 = sum(
    row.count("O") * (len(grid_slided) - i) for i, row in enumerate(grid_slided)
)

print("Solution 1:", solution1)

seen = {input}
seen_list = [input]

grid_cycle = input
for i in range(CYCLES):
    grid_cycle = cycle(grid_cycle)
    # print_grid(grid_cycle)

    if grid_cycle in seen:
        break
    seen.add(grid_cycle)
    seen_list.append(grid_cycle)

first_cycle_grid_index = seen_list.index(grid_cycle)
final_grid = seen_list[
    (CYCLES - first_cycle_grid_index) % (i + 1 - first_cycle_grid_index)
    + first_cycle_grid_index
]

solution2 = sum(
    row.count("O") * (len(final_grid) - i) for i, row in enumerate(final_grid)
)
print("Solution 2:", solution2)
