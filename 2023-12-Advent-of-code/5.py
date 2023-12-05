from tqdm import tqdm

""" Problem 1
The almanac (your puzzle input) lists all of the seeds that need to be planted. It also lists what type of soil to use with each kind of seed, what 
type of fertilizer to use with each kind of soil, what type of water to use with each kind of fertilizer, and so on. Every type of seed, soil, fertilizer 
and so on is identified with a number, but numbers are reused by each category - that is, soil 123 and fertilizer 123 aren't necessarily related to each other.

For example:
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
The almanac starts by listing which seeds need to be planted: seeds 79, 14, 55, and 13.

The rest of the almanac contains a list of maps which describe how to convert numbers from a source category into numbers in a destination category. That is, the section that starts with seed-to-soil map: describes how to convert a seed number (the source) to a soil number (the destination). This lets the gardener and his team know which soil to use with which seeds, which water to use with which fertilizer, and so on.

Rather than list every source number and its corresponding destination number one by one, the maps describe entire ranges of numbers that can be converted. Each line within a map contains three numbers: the destination range start, the source range start, and the range length.

Consider again the example seed-to-soil map:

50 98 2
52 50 48
The first line has a destination range start of 50, a source range start of 98, and a range length of 2. This line means that the source range starts at 98 and contains two values: 98 and 99. The destination range is the same length, but it starts at 50, so its two values are 50 and 51. With this information, you know that seed number 98 corresponds to soil number 50 and that seed number 99 corresponds to soil number 51.

The second line means that the source range starts at 50 and contains 48 values: 50, 51, ..., 96, 97. This corresponds to a destination range starting at 52 and also containing 48 values: 52, 53, ..., 98, 99. So, seed number 53 corresponds to soil number 55.

Any source numbers that aren't mapped correspond to the same destination number. So, seed number 10 corresponds to soil number 10.

So, the entire list of seed numbers and their corresponding soil numbers looks like this:

seed  soil
0     0
1     1
...   ...
48    48
49    49
50    52
51    53
...   ...
96    98
97    99
98    50
99    51
With this map, you can look up the soil number required for each initial seed number:

Seed number 79 corresponds to soil number 81.
Seed number 14 corresponds to soil number 14.
Seed number 55 corresponds to soil number 57.
Seed number 13 corresponds to soil number 13.
The gardener and his team want to get started as soon as possible, so they'd like to know the closest location that needs a seed. Using these maps, find the lowest location number that corresponds to any of the initial seeds. To do this, you'll need to convert each seed number through other categories until you can find its corresponding location number. In this example, the corresponding types are:

Seed 79, soil 81, fertilizer 81, water 81, light 74, temperature 78, humidity 78, location 82.
Seed 14, soil 14, fertilizer 53, water 49, light 42, temperature 42, humidity 43, location 43.
Seed 55, soil 57, fertilizer 57, water 53, light 46, temperature 82, humidity 82, location 86.
Seed 13, soil 13, fertilizer 52, water 41, light 34, temperature 34, humidity 35, location 35.
So, the lowest location number in this example is 35.

What is the lowest location number that corresponds to any of the initial seed numbers?
"""

""" Problem 2
Everyone will starve if you only plant such a small number of seeds. Re-reading the almanac, it looks like the seeds: line actually describes ranges of seed numbers.

The values on the initial seeds: line come in pairs. Within each pair, the first value is the start of the range and the second value is the length of the range. So, in the first line of the example above:

seeds: 79 14 55 13
This line describes two ranges of seed numbers to be planted in the garden. The first range starts with seed number 79 and contains 14 values: 79, 80, ..., 91, 92. The second range starts with seed number 55 and contains 13 values: 55, 56, ..., 66, 67.

Now, rather than considering four seed numbers, you need to consider a total of 27 seed numbers.

In the above example, the lowest location number can be obtained from seed number 82, which corresponds to soil 84, fertilizer 84, water 84, light 77, temperature 45, humidity 46, and location 46. So, the lowest location number is 46.

Consider all of the initial seed numbers listed in the ranges on the first line of the almanac. What is the lowest location number that corresponds to any of the initial seed numbers?
"""


def chain_mappings(seeds, maps):
    locations = []
    for seed in seeds:
        for map_ in maps:
            for dest, src, range in map_:
                if src <= seed < src + range:
                    seed += dest - src
                    break

        locations.append(seed)

    return locations


def chain_mappings_with_range(seed_pairs, maps):
    locations = []
    for pair in seed_pairs:
        remain = [pair]  # x,y
        result = []

        for map_ in maps:
            while remain:
                seed_range = remain.pop()
                # src = a
                # src+range-1 = b
                for dest, src, range in map_:
                    # no overlap, x-y-a-b or a-b-x-y
                    if seed_range[1] < src or src + range <= seed_range[0]:
                        continue

                    # a-x-y-b
                    elif src <= seed_range[0] <= seed_range[1] < src + range:
                        offset = seed_range[0] - src
                        result.append(
                            (
                                dest + offset,
                                dest + offset + seed_range[1] - seed_range[0],
                            )
                        )
                        break

                    # x-a-y-b
                    elif seed_range[0] < src <= seed_range[1] < src + range:
                        offset = seed_range[1] - src
                        result.append((dest, dest + offset))
                        remain.append((seed_range[0], src - 1))
                        break

                    # a-x-b-y
                    elif src <= seed_range[0] < src + range <= seed_range[1]:
                        offset = seed_range[0] - src
                        result.append((dest + offset, dest + range - 1))
                        remain.append((src + range, seed_range[1]))
                        break

                    # x-a-b-y
                    elif seed_range[0] < src <= src + range <= seed_range[1]:
                        result.append((dest, dest + range - 1))
                        remain.append((seed_range[0], src - 1))
                        remain.append((src + range, seed_range[1]))
                        break

                else:  # Do not match any source range
                    result.append(seed_range)

            # When a map is done, the result becomes the new remain
            remain = result
            result = []

        #  When all maps are done, the remain are the new locations
        locations.extend(remain)

    return locations


with open("inputs/5.txt", "r") as file:
    data = file.read().splitlines()


seeds = [*map(int, data[0].split(": ")[1].split())]

# maps[0]: seed-to-soil map, maps[1]: soil-to-fertilizer map, maps[2]: fertilizer-to-water map, maps[3]: water-to-light map, masp[4]: light-to-temperature map, maps[5]: temperature-to-humidity map, maps[6]: humidity-to-location map
# each map is a list of Map objects: [source, dest, range], [source, dest, range]
maps = [
    [[*map(int, n.split())] for n in i.split("\n")[1:]]
    for i in "\n".join(data[2:]).split("\n\n")
]

locations = chain_mappings(seeds, maps)
print("Solution 1:", min(locations))

seeds_pairs = [(seeds[i], seeds[i] + seeds[i + 1] - 1) for i in range(0, len(seeds), 2)]

locations = chain_mappings_with_range(seeds_pairs, maps)
print("Solution 2:", min(i[0] for i in locations))
