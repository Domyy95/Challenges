"""Problem 1
Now that you can think clearly, you move deeper into the labyrinth of hallways and office furniture that makes up this part of Easter Bunny HQ. This must be a graphic design department; the walls are covered in specifications for triangles.

Or are they?

The design document gives the side lengths of each triangle it describes, but... 5 10 25? Some of these aren't triangles. You can't help but mark the impossible ones.

In a valid triangle, the sum of any two sides must be larger than the remaining side. For example, the "triangle" given above is impossible, because 5 + 10 is not larger than 25.

In your puzzle input, how many of the listed triangles are possible?
"""

"""Problem 2
Now that you've helpfully marked up their design documents, it occurs to you that triangles are specified in groups of three vertically. Each set of three numbers in a column specifies a triangle. Rows are unrelated.

For example, given the following specification, numbers with the same hundreds digit would be part of the same triangle:

101 301 501
102 302 502
103 303 503
201 401 601
202 402 602
203 403 603
In your puzzle input, and instead reading by columns, how many of the listed triangles are possible?
"""

with open("inputs/3.txt") as f:
    triangles = f.readlines()

triangles = [list(map(int, x.split())) for x in triangles]

result_1 = 0
for triangle in triangles:
    triangle_r = triangle.copy()
    triangle_r.sort()
    if triangle_r[0] + triangle_r[1] > triangle_r[2]:
        result_1 += 1

print("Solution 1:", result_1)

result_2 = 0
for i in range(0, len(triangles), 3):
    for j in range(3):
        triangle = [triangles[i][j], triangles[i + 1][j], triangles[i + 2][j]]
        triangle.sort()
        if triangle[0] + triangle[1] > triangle[2]:
            result_2 += 1

print("Solution 2:", result_2)
