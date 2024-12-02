"""Problem 1
Finally, as you approach what must be the heart of the mountain, you see a bright light in a cavern up ahead. There, you discover that the beam of light you so carefully focused is emerging from the cavern wall closest to the facility and pouring all of its energy into a contraption on the opposite side.

Upon closer inspection, the contraption appears to be a flat, two-dimensional square grid containing empty space (.), mirrors (/ and \), and splitters (| and -).

The contraption is aligned so that most of the beam bounces around the grid, but each tile on the grid converts some of the beam's light into heat to melt the rock in the cavern.

You note the layout of the contraption (your puzzle input). For example:

.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....
The beam enters in the top-left corner from the left and heading to the right. Then, its behavior depends on what it encounters as it moves:

If the beam encounters empty space (.), it continues in the same direction.
If the beam encounters a mirror (/ or \), the beam is reflected 90 degrees depending on the angle of the mirror. For instance, a rightward-moving beam that encounters a / mirror would continue upward in the mirror's column, while a rightward-moving beam that encounters a \ mirror would continue downward from the mirror's column.
If the beam encounters the pointy end of a splitter (| or -), the beam passes through the splitter as if the splitter were empty space. For instance, a rightward-moving beam that encounters a - splitter would continue in the same direction.
If the beam encounters the flat side of a splitter (| or -), the beam is split into two beams going in each of the two directions the splitter's pointy ends are pointing. For instance, a rightward-moving beam that encounters a | splitter would split into two beams: one that continues upward from the splitter's column and one that continues downward from the splitter's column.
Beams do not interact with other beams; a tile can have many beams passing through it at the same time. A tile is energized if that tile has at least one beam pass through it, reflect in it, or split in it.

In the above example, here is how the beam of light bounces around the contraption:

>|<<<\....
|v-.\^....
.v...|->>>
.v...v^.|.
.v...v^...
.v...v^..\
.v../2\\..
<->-/vv|..
.|<<<2-|.\
.v//.|.v..
Beams are only shown on empty tiles; arrows indicate the direction of the beams. If a tile contains beams moving in multiple directions, the number of distinct directions is shown instead. Here is the same diagram but instead only showing whether a tile is energized (#) or not (.):

######....
.#...#....
.#...#####
.#...##...
.#...##...
.#...##...
.#..####..
########..
.#######..
.#...#.#..
Ultimately, in this example, 46 tiles become energized.

The light isn't energizing enough tiles to produce lava; to debug the contraption, you need to start by analyzing the current situation. With the beam starting in the top-left heading right, how many tiles end up being energized?


"""

"""Problem 2
As you try to work out what might be wrong, the reindeer tugs on your shirt and leads you to a nearby control panel. There, a collection of buttons lets you align the contraption so that the beam enters from any edge tile and heading away from that edge. (You can choose either of two directions for the beam if it starts on a corner; for instance, if the beam starts in the bottom-right corner, it can start heading either left or upward.)

So, the beam could start on any tile in the top row (heading downward), any tile in the bottom row (heading upward), any tile in the leftmost column (heading right), or any tile in the rightmost column (heading left). To produce lava, you need to find the configuration that energizes as many tiles as possible.

In the above example, this can be achieved by starting the beam in the fourth tile from the left in the top row:

.|<2<\....
|v-v\^....
.v.v.|->>>
.v.v.v^.|.
.v.v.v^...
.v.v.v^..\
.v.v/2\\..
<-2-/vv|..
.|<<<2-|.\
.v//.|.v..
Using this configuration, 51 tiles are energized:

.#####....
.#.#.#....
.#.#.#####
.#.#.##...
.#.#.##...
.#.#.##...
.#.#####..
########..
.#######..
.#...#.#..
Find the initial beam configuration that energizes the largest number of tiles; how many tiles are energized in that configuration?
"""


with open("inputs/16.txt", "r") as file:
    grid = file.read().splitlines()


def calc_energized(grid, start):
    # (row, col, movement row, movement col)
    queue = [start]
    seen = set()

    while queue:
        row, col, drow, dcol = queue.pop(0)
        row += drow
        col += dcol

        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
            continue

        new_pos = grid[row][col]

        if (
            new_pos == "."
            or (new_pos == "-" and dcol != 0)
            or (new_pos == "|" and drow != 0)
        ):
            queue.append((row, col, drow, dcol))
            seen.add((row, col, drow, dcol))

        elif new_pos == "\\":
            drow, dcol = dcol, drow
            if (row, col, drow, dcol) not in seen:
                queue.append((row, col, drow, dcol))
                seen.add((row, col, drow, dcol))

        elif new_pos == "/":
            drow, dcol = -dcol, -drow
            if (row, col, drow, dcol) not in seen:
                queue.append((row, col, drow, dcol))
                seen.add((row, col, drow, dcol))

        else:
            for dr, dc in [(1, 0), (-1, 0)] if new_pos == "|" else [(0, 1), (0, -1)]:
                if (row, col, dr, dc) not in seen:
                    queue.append((row, col, dr, dc))
                    seen.add((row, col, dr, dc))

    visited = {(row, col) for (row, col, _, _) in seen}

    return len(visited)


# row -1 because its like you start outside the grid
solution1 = calc_energized(grid, (0, -1, 0, 1))
print(f"Solution 1: ", solution1)

solution2 = 0
for row in range(len(grid)):
    solution2 = max(
        solution2,
        calc_energized(grid, (row, -1, 0, 1)),
        calc_energized(grid, (row, len(grid), 0, -1)),
    )

for col in range(len(grid[0])):
    solution2 = max(
        solution2,
        calc_energized(grid, (-1, col, 1, 0)),
        calc_energized(grid, (len(grid), col, -1, 0)),
    )

print(f"Solution 2: ", solution2)
