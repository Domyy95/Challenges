# Problem Statement: https://www.hackerearth.com/challenges/competitive/may-circuits-20/algorithm/cycle-count-0644f309/
"""
You are given an N-sided regular polygon. You have connected the center of the polygon with all the vertices, thus dividing the polygon into N equal parts.

Your task is to find the count of simple cycles that exist in the modified structure of the polygon.
"""

Q = int(input())

for i in range(0, Q):
    N = int(input())
    sol = (N * (N - 1)) + 1
    print(sol)
