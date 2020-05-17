# Problem Statement: https://www.hackerearth.com/challenges/competitive/may-circuits-20/algorithm/powerful-of-factorial-cb263e5b/
'''
You are given two numbers X and N. Your task is to find the last digit of the following equation:
X ** ((N!)%10) 
'''

X,N = map(int, input().split())

if N == 2:
    print(X**2 % 10)
elif N == 3:
    print(X**6 % 10)
elif N == 4:
    print(X**4 % 10)

else:
    print(1)