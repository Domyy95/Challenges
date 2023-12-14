# Problem Statement: https://www.hackerearth.com/challenges/competitive/may-circuits-20/algorithm/k-excess-1-be669e5a/
"""
You are given two numbers n and k. For each number in the interval [1, n], your task is to calculate its largest divisor that is 
not divisible by k. Print the sum of these divisors.

Note: k is a prime number.
"""

T = int(input())
solutions = []

for i in range(0, T):
    n, k = map(int, input().split())
    solution = n * (n + 1) // 2

    k_pow = k

    while k_pow <= n:
        up = n // k_pow
        solution = solution - (k - 1) * (up * (up + 1)) // 2
        k_pow *= k

    solutions.append(solution)

print("\n".join(str(e) for e in solutions))
