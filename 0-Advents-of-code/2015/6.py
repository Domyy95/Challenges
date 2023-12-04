import re

"""Problem 1
Because your neighbors keep defeating you in the holiday house decorating contest year after year, you've decided to deploy one million lights in a 1000x1000 grid.

Furthermore, because you've been especially nice this year, Santa has mailed you instructions on how to display the ideal lighting configuration.
Lights in your grid are numbered from 0 to 999 in each direction; the lights at each corner are at 0,0, 0,999, 999,999, and 999,0. The instructions include whether to turn on, turn off, or toggle various inclusive ranges given as coordinate pairs. Each coordinate pair represents opposite corners of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square. The lights all start turned off.

To defeat your neighbors this year, all you have to do is set up your lights by doing the instructions Santa sent you in order.

For example:

turn on 0,0 through 999,999 would turn on (or leave on) every light.
toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off the ones that were on, and turning on the ones that were off.
turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.
After following the instructions, how many lights are lit?
"""

"""Problem 2
You just finish implementing your winning light pattern when you realize you mistranslated Santa's message from Ancient Nordic Elvish.

The light grid you bought actually has individual brightness controls; each light can have a brightness of zero or more. The lights all start at zero.

The phrase turn on actually means that you should increase the brightness of those lights by 1.

The phrase turn off actually means that you should decrease the brightness of those lights by 1, to a minimum of zero.

The phrase toggle actually means that you should increase the brightness of those lights by 2.

What is the total brightness of all lights combined after following Santa's instructions?

For example:

turn on 0,0 through 0,0 would increase the total brightness by 1.
toggle 0,0 through 999,999 would increase the total brightness by 2000000.
"""


def click_lights(inst, lights_grid):
    from_x, from_y, to_x, to_y = re.findall(r"\d+", inst)
    if "toggle" in instruction:
        for i in range(int(from_x), int(to_x) + 1):
            for j in range(int(from_y), int(to_y) + 1):
                lights_grid[i][j] = not lights_grid[i][j]

    elif "turn off" in instruction:
        for i in range(int(from_x), int(to_x) + 1):
            for j in range(int(from_y), int(to_y) + 1):
                lights_grid[i][j] = False

    elif "turn on" in instruction:
        for i in range(int(from_x), int(to_x) + 1):
            for j in range(int(from_y), int(to_y) + 1):
                lights_grid[i][j] = True

    return lights_grid


def click_lights_brightness(inst, lights_grid):
    from_x, from_y, to_x, to_y = re.findall(r"\d+", inst)
    if "toggle" in instruction:
        for i in range(int(from_x), int(to_x) + 1):
            for j in range(int(from_y), int(to_y) + 1):
                lights_grid[i][j] += 2

    elif "turn off" in instruction:
        for i in range(int(from_x), int(to_x) + 1):
            for j in range(int(from_y), int(to_y) + 1):
                if lights_grid[i][j] > 0:
                    lights_grid[i][j] -= 1

    elif "turn on" in instruction:
        for i in range(int(from_x), int(to_x) + 1):
            for j in range(int(from_y), int(to_y) + 1):
                lights_grid[i][j] += 1

    return lights_grid


with open("inputs/6.txt", "r") as file:
    instructions = file.read().splitlines()

lights_grid = [[0 for _ in range(1000)] for _ in range(1000)]
lights_grid_brightness = [[0 for _ in range(1000)] for _ in range(1000)]

for instruction in instructions:
    lights_grid = click_lights(instruction, lights_grid)
    lights_grid_brightness = click_lights_brightness(
        instruction, lights_grid_brightness
    )

print("Solution 1: ", sum([sum(row) for row in lights_grid]))
print("Solution 2: ", sum([sum(row) for row in lights_grid_brightness]))
