"""Problem 1
You're airdropped near Easter Bunny Headquarters in a city somewhere. "Near", unfortunately, is as close as you can get - the instructions on the Easter Bunny Recruiting Document the Elves intercepted start here, and nobody had time to work them out further.

The Document indicates that you should start at the given coordinates (where you just landed) and face North. Then, follow the provided sequence: either turn left (L) or right (R) 90 degrees, then walk forward the given number of blocks, ending at a new intersection.

There's no time to follow such ridiculous instructions on foot, though, so you take a moment and work out the destination. Given that you can only walk on the street grid of the city, how far is the shortest path to the destination?

For example:

Following R2, L3 leaves you 2 blocks East and 3 blocks North, or 5 blocks away.
R2, R2, R2 leaves you 2 blocks due South of your starting position, which is 2 blocks away.
R5, L5, R5, R3 leaves you 12 blocks away.
How many blocks away is Easter Bunny HQ?
"""

"""Problem 2
Then, you notice the instructions continue on the back of the Recruiting Document. Easter Bunny HQ is actually at the first location you visit twice.

For example, if your instructions are R8, R4, R4, R8, the first location you visit twice is 4 blocks away, due East.

How many blocks away is the first location you visit twice?
"""

input = "R2, L1, R2, R1, R1, L3, R3, L5, L5, L2, L1, R4, R1, R3, L5, L5, R3, L4, L4, R5, R4, R3, L1, L2, R5, R4, L2, R1, R4, R4, L2, L1, L1, R190, R3, L4, R52, R5, R3, L5, R3, R2, R1, L5, L5, L4, R2, L3, R3, L1, L3, R5, L3, L4, R3, R77, R3, L2, R189, R4, R2, L2, R2, L1, R5, R4, R4, R2, L2, L2, L5, L1, R1, R2, L3, L4, L5, R1, L1, L2, L2, R2, L3, R3, L4, L1, L5, L4, L4, R3, R5, L2, R4, R5, R3, L2, L2, L4, L2, R2, L5, L4, R3, R1, L2, R2, R4, L1, L4, L4, L2, R2, L4, L1, L1, R4, L1, L3, L2, L2, L5, R5, R2, R5, L1, L5, R2, R4, R4, L2, R5, L5, R5, R5, L4, R2, R1, R1, R3, L3, L3, L4, L3, L2, L2, L2, R2, L1, L3, R2, R5, R5, L4, R3, L3, L4, R2, L5, R5"

directions = input.split(", ")


def get_final_position(directions):
    visited = set((0, 0))
    first_revisited = None
    position = [0, 0]
    direction = 0
    for d in directions:
        if d[0] == "R":
            direction += 1
        else:
            direction -= 1
        direction = direction % 4
        distance = int(d[1:])
        positions_visited = []
        if direction == 0:
            positions_visited = [
                (position[0], position[1] + i) for i in range(1, distance + 1)
            ]
            position[1] += distance
        elif direction == 1:
            positions_visited = [
                (position[0] + i, position[1]) for i in range(1, distance + 1)
            ]
            position[0] += distance
        elif direction == 2:
            positions_visited = [
                (position[0], position[1] - i) for i in range(1, distance + 1)
            ]
            position[1] -= distance
        elif direction == 3:
            positions_visited = [
                (position[0] - i, position[1]) for i in range(1, distance + 1)
            ]
            position[0] -= distance

        if first_revisited is None:
            for position_v in positions_visited:
                if tuple(position_v) in visited:
                    first_revisited = position_v
                    break
                else:
                    visited.add(tuple(position_v))

    return first_revisited, position


first_revisited, final_position = get_final_position(directions)
sol_1 = sum([abs(x) for x in final_position])
sol_2 = sum([abs(x) for x in first_revisited])
print("Solution 1:", sol_1)
print("Solution 2:", sol_2)
