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
from heapq import heappush, heappop
 
class Order():
    __slots__ = ['index', 'arrival', 'preparation', 'cost']    
    def __init__(self, index, arrival, preparation, cost):
        self.index = index
        self.arrival = arrival
        self.preparation = preparation
        self.cost = cost

    def __lt__(self, other):
        # compare 2 orders: self < other <=> self must be served before other
        # cost1: cost of serving self first, then serving other
        cost1self = self.preparation * self.cost
        cost1other = (max(self.arrival + self.preparation, other.arrival) - other.arrival) * other.cost + other.preparation * other.cost
        cost1 = cost1self + cost1other
        # cost2: cost of serving other first, then serving self
        cost2other = other.preparation * other.cost
        cost2self = (max(other.arrival + other.preparation, self.arrival) - self.arrival) * self.cost + self.preparation * self.cost
        cost2 = cost2self + cost2other
        return cost1 < cost2
 
def solve(orders, N, K):
    output = [0] * N
    chefs = []
    # all K chefs are immediately available at T = 0
    for chef in range(K):
        heappush(chefs, 0)
    # process all orders in their sorted order
    for order in orders:
        # next chef is available at time T
        T = heappop(chefs)
        # and starts working at max(T, order.arrival)
        T = max(T, order.arrival)
        output[order.index] = T
        # chef will be available at max(T, order.arrival) + order.preparation
        heappush(chefs, T + order.preparation)
    return ' '.join([str(x) for x in output])
 
if __name__ == "__main__":
    N, K = list(map(int, input().strip().split()))
    A = list(map(int, input().strip().split()))  # customer arrival time
    B = list(map(int, input().strip().split()))  # preparation time
    C = list(map(int, input().strip().split()))  # cost per unit of time
    orders = []

    for index, (a, b, c) in enumerate(zip(A, B, C)):
        orders.append(Order(index, a, b, c))
        
    # sort orders in the order in which they will be processed (the 1st chef
    # available will process the next order in the line of orders)
    orders = sorted(orders)
    print(solve(orders, N, K))