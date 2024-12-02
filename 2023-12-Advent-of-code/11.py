"""Problem 1
The researcher has collected a bunch of data and compiled the data into a single giant image (your puzzle input). The image includes empty space (.) and galaxies (#). For example:

...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
The researcher is trying to figure out the sum of the lengths of the shortest path between every pair of galaxies. However, there's a catch: the universe expanded in the time it took the light from those galaxies to reach the observatory.

Due to something involving gravitational effects, only some space expands. In fact, the result is that any rows or columns that contain no galaxies should all actually be twice as big.

In the above example, three columns and two rows contain no galaxies:

   v  v  v
 ...#......
 .......#..
 #.........
>..........<
 ......#...
 .#........
 .........#
>..........<
 .......#..
 #...#.....
   ^  ^  ^
These rows and columns need to be twice as big; the result of cosmic expansion therefore looks like this:

....#........
.........#...
#............
.............
.............
........#....
.#...........
............#
.............
.............
.........#...
#....#.......
Equipped with this expanded universe, the shortest path between every pair of galaxies can be found. It can help to assign every galaxy a unique number:

....1........
.........2...
3............
.............
.............
........4....
.5...........
............6
.............
.............
.........7...
8....9.......
In these 9 galaxies, there are 36 pairs. Only count each pair once; order within the pair doesn't matter. For each pair, find any shortest path between the two galaxies using only steps that move up, down, left, or right exactly one . or # at a time. (The shortest path between two galaxies is allowed to pass through another galaxy.)

For example, here is one of the shortest paths between galaxies 5 and 9:

....1........
.........2...
3............
.............
.............
........4....
.5...........
.##.........6
..##.........
...##........
....##...7...
8....9.......
This path has length 9 because it takes a minimum of nine steps to get from galaxy 5 to galaxy 9 (the eight locations marked # plus the step onto galaxy 9 itself). Here are some other example shortest path lengths:

Between galaxy 1 and galaxy 7: 15
Between galaxy 3 and galaxy 6: 17
Between galaxy 8 and galaxy 9: 5
In this example, after expanding the universe, the sum of the shortest path between all 36 pairs of galaxies is 374.

Expand the universe, then find the length of the shortest path between every pair of galaxies. What is the sum of these lengths?
"""

"""Problem 2
The galaxies are much older (and thus much farther apart) than the researcher initially estimated.

Now, instead of the expansion you did before, make each empty row or column one million times larger. That is, each empty row should be replaced with 1000000 empty rows, and each empty column should be replaced with 1000000 empty columns.

(In the example above, if each empty row or column were merely 10 times larger, the sum of the shortest paths between every pair of galaxies would be 1030. If each empty row or column were merely 100 times larger, the sum of the shortest paths between every pair of galaxies would be 8410. However, your universe will need to expand far beyond these values.)

Starting with the same initial image, expand the universe according to these new rules, then find the length of the shortest path between every pair of galaxies. What is the sum of these lengths?
"""

with open("inputs/11.txt", "r") as file:
    input = file.read().splitlines()


def find_galaxies_and_empty_spaces(input):
    galaxies = []
    for row, line in enumerate(input):
        for col, c in enumerate(line):
            if c == "#":
                galaxies.append((row, col))

    all_rows = set([g[0] for g in galaxies])
    all_cols = set([g[1] for g in galaxies])
    empty_rows = sorted(set(range(row)).difference(all_rows))
    empty_cols = sorted(set(range(col)).difference(all_cols))

    return galaxies, empty_rows, empty_cols


solution1 = 0
solution2 = 0
expand_2 = 1000000 - 1
galaxies, empty_rows, empty_cols = find_galaxies_and_empty_spaces(input)

for i, galaxy in enumerate(galaxies):
    for j in range(i + 1, len(galaxies)):
        galaxy2 = galaxies[j]
        empty_rows_passed = len(
            [
                r
                for r in empty_rows
                if (galaxy2[0] < r < galaxy[0]) or (galaxy[0] < r < galaxy2[0])
            ]
        )
        empty_cols_passed = len(
            [
                c
                for c in empty_cols
                if (galaxy2[1] < c < galaxy[1]) or (galaxy[1] < c < galaxy2[1])
            ]
        )

        solution1 += (
            abs(galaxy[0] - galaxy2[0])
            + abs(galaxy[1] - galaxy2[1])
            + empty_rows_passed
            + empty_cols_passed
        )
        solution2 += (
            abs(galaxy[0] - galaxy2[0])
            + abs(galaxy[1] - galaxy2[1])
            + (empty_rows_passed + empty_cols_passed) * expand_2
        )

print("Solution 1: ", solution1)
print("Solution 2: ", solution2)
