# Problem Statement: https://www.hackerearth.com/challenges/competitive/may-circuits-20/algorithm/avoiding-networked-paths-revisited-38d27ffb/
'''
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
'''
