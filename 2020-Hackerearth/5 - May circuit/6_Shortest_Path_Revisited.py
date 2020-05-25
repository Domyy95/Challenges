# Problem Statement: https://www.hackerearth.com/challenges/competitive/may-circuits-20/algorithm/shortest-path-revisited-9e1091ea/
'''
In the country of HackerEarth, there are N cities and M bi - directional roads. We need to transport essential items from 
City 1  to all other cities. (There exists a path always)

But every road has some positive amount of Toll Charge associated with it say C (it is not same for all roads). 
We need to find the minimum amount of charge that it required to deliver essential items for each city.

Fortunately, to our rescue we have K special offers, which means while travelling from City 1 to any other city we can select 
at-most K roads and we will not be charged for using those roads. 

Can you now find the minimum charge that we have to pay to deliver essential items for each city.

(Remember we require to provide answers for each destination city separately i.e. we have K offers for every city and not as a whole)
'''

from sys import setrecursionlimit,stdin,stdout
from collections import deque

setrecursionlimit(10**6)

def shortestpath(tree,cost):
    global k
    q=deque()
    q.appendleft([1,0])
    while q:
        lis=q.pop()
        child=lis[0]
        parent=lis[1]
        for i in tree[child]:
            if i[0]==parent:
                continue
            flag=0
            for j in range(k+1):
                if j<k and cost[i[0]][j+1]>cost[child][j]:
                    flag=1
                    cost[i[0]][j+1]=cost[child][j]
                if cost[i[0]][j]>cost[child][j]+i[1]:
                    flag=1
                    cost[i[0]][j]=cost[child][j]+i[1]
            if flag==1:
                q.appendleft([i[0],child])
       
def main():
    global k
    n,m,k=map(int,stdin.readline().split())
    tree={}
    for i in range(m):
        u,v,w=map(int,stdin.readline().split())
        if tree.get(u)==None:
            tree[u]=[[v,w]]
        else:
            tree[u].append([v,w])
        if tree.get(v)==None:
            tree[v]=[[u,w]]
        else:
            tree[v].append([u,w])
    cost=[[10**10 for i in range(k+1)] for j in range(n+1)]
    
    cost[1][0]=0
    shortestpath(tree,cost)
    for i in range(1,n+1):
        print(min(cost[i]),end=" ")
        
if __name__=="__main__":
    main()