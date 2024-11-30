# Problem Statement: https://www.hackerearth.com/challenges/competitive/may-circuits-20/algorithm/avoiding-networked-paths-revisited-38d27ffb/
"""
A group of people is going for a fun trip to a city coordinated at (1, 1). During their visit, a network started spreading all
over the world. After knowing about the network, they decided to safely return to their home town coordinated at (n, m).
Among all the paths from (1, 1) to (n, m), some got in the contact with this network. They want to avoid networked paths and
hence started calculating the total number of safe paths. Since it can take them a lot of time to find all the safe paths,
so they have asked you to help.

You have been given a map in the form of a matrix A of size n×m. Each coordinate represents a city on the map.
You are required to find the total number of safe paths starting from city (1, 1) and ending at city (n, m).
You are allowed to move either right or down in a single move, that is, if you are at city (x, y),
then you can go to either (x+1, y) or (x, y+1) in a single move. You are not allowed to move outside the map.

A path is networked if the product of all the numbers in the path is divisible by X.
"""

MOD = 10**9 + 7


def numToKey(n):
    ret = 0

    if n % (107 * 107) == 0:
        ret += 2
    elif n % 107 == 0:
        ret += 1

    ret *= 3

    if n % (1361 * 1361) == 0:
        ret += 2

    elif n % 1361 == 0:
        ret += 1

    ret *= 2

    if n % 10000019 == 0:
        ret += 1

    return ret


transfer = []

for i in range(18):
    row = []

    x = i & 1
    y = (i // 2) % 3
    z = i // 6

    for j in range(18):
        x1 = j & 1
        y1 = (j // 2) % 3
        z1 = j // 6

        row.append((min(2, z + z1) * 3 + min(2, y + y1)) * 2 + min(1, x + x1))
    transfer.append(row)

# for row in transfer:
#     print(*row)

n, m = [int(x) for x in input().split()]

dp = [[0 for i in range(18)] for j in range(m)]
dp[0][0] = 1

for r in range(n):
    for i, val in enumerate([int(x) for x in input().split()]):
        nextSet = [0 for i in range(18)]

        key = numToKey(val)

        if key == 0:
            if i > 0:
                nextSet = dp[i - 1][:]

            for j, other in enumerate(dp[i]):
                if other == 0:
                    continue
                nextSet[j] += other
                nextSet[j] %= MOD

        else:
            if i > 0:
                for j, other in enumerate(dp[i - 1]):
                    if other == 0:
                        continue
                    nextSet[transfer[key][j]] += other

            for j, other in enumerate(dp[i]):
                if other == 0:
                    continue
                nextSet[transfer[key][j]] += other
                nextSet[transfer[key][j]] %= MOD

        dp[i] = nextSet

print(sum(dp[-1][:-1]) % MOD)
# print(dp)
