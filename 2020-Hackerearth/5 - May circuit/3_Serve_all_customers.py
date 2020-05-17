# Problem Statement: https://www.hackerearth.com/challenges/competitive/may-circuits-20/approximate/gotta-serveem-all-deb7cc6d/
'''
There are N people entering a restaurant at different times. These people are numbered from 1 to N by the staffs of the restaurant. 
There are K chefs working in the restaurant. These chefs are also numbered from 1 to N by the management of the restaurant. 
A person has to order immediately after he or she enters the restaurant. The arrival time of a person is given in an array A so that the
restaurant can track the timings of the customers. Also, the time that a chef takes to prepare the customer's orders is given in an 
array B. The management of the restaurant also stores some data in array C. The element of this array, C(i), denotes the increased 
amount of the satisfaction level of the ith customer if he or she has to wait for 1 unit of time after giving the order.

The restaurant is open until 10**9 units of time and all the orders must be prepared by this time. 
Your task is to minimize the sum of the total satisfaction level of all the customers who come to the restaurant.
Note: Only one chef works to prepare an order of one person. A chef can only prepare one order at a time and a person's order can only 
be prepared by one chef. Also, if a chef completes preparation of order at time , then he or she can pick up another order and start 
preparing it at time t+1.
'''
N,K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

solution = []
next_time_free = [A[0] for i in range(0,K)]

for i,a in enumerate(A): 

    chef = min(next_time_free)

    if chef > 10**9:
        break
    
    if A[i] <= chef:
        solution.append(chef)
        chef_new = chef + B[i]
        next_time_free.remove(chef)
        next_time_free.append(chef_new)
    
    else: 
        solution.append(A[i])
        chef_new = chef + B[i] + A[i]
        next_time_free.remove(chef)
        next_time_free.append(chef_new)
    

print(' '.join(str(e) for e in solution))