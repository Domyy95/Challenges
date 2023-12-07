""" Problem 1
Every year, Santa manages to deliver all of his presents in a single night.

This year, however, he has some new locations to visit; his elves have provided him the distances between every pair of locations. He can start and end at any two (different) locations he wants, but he must visit each location exactly once. What is the shortest distance he can travel to achieve this?

For example, given the following distances:

London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141
The possible routes are therefore:

Dublin -> London -> Belfast = 982
London -> Dublin -> Belfast = 605
London -> Belfast -> Dublin = 659
Dublin -> Belfast -> London = 659
Belfast -> Dublin -> London = 605
Belfast -> London -> Dublin = 982
The shortest of these is London -> Dublin -> Belfast = 605, and so the answer is 605 in this example.

What is the distance of the shortest route?
"""

""" Problem 2
The next year, just to show off, Santa decides to take the route with the longest distance instead.

He can still start and end at any two (different) locations he wants, and he still must visit each location exactly once.

For example, given the distances above, the longest route would be 982 via (for example) Dublin -> London -> Belfast.

What is the distance of the longest route?
"""

input = """
Tristram to AlphaCentauri = 34
Tristram to Snowdin = 100
Tristram to Tambi = 63
Tristram to Faerun = 108
Tristram to Norrath = 111
Tristram to Straylight = 89
Tristram to Arbre = 132
AlphaCentauri to Snowdin = 4
AlphaCentauri to Tambi = 79
AlphaCentauri to Faerun = 44
AlphaCentauri to Norrath = 147
AlphaCentauri to Straylight = 133
AlphaCentauri to Arbre = 74
Snowdin to Tambi = 105
Snowdin to Faerun = 95
Snowdin to Norrath = 48
Snowdin to Straylight = 88
Snowdin to Arbre = 7
Tambi to Faerun = 68
Tambi to Norrath = 134
Tambi to Straylight = 107
Tambi to Arbre = 40
Faerun to Norrath = 11
Faerun to Straylight = 66
Faerun to Arbre = 144
Norrath to Straylight = 115
Norrath to Arbre = 135
Straylight to Arbre = 127
"""

# Compute all the minimum distances from a node to all the other nodes
def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    unvisited_nodes = list(graph.keys())

    while unvisited_nodes:
        current_node = min(unvisited_nodes, key=lambda node: distances[node])
        unvisited_nodes.remove(current_node)

        for neighbor, weight in graph[current_node].items():
            distance = distances[current_node] + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance

    return distances

def parse_input(input):
    graph = {}

    for line in input.strip().splitlines():
        city1, _, city2, _, distance = line.split(" ")
        
        if city1 not in graph:
            graph[city1] = {}
        if city2 not in graph:
            graph[city2] = {}
        
        graph[city1][city2] = int(distance)
        graph[city2][city1] = int(distance)

    return graph
        

graph = parse_input(input)
min_solution = float('infinity')
for city in graph:
    distances = dijkstra(graph, city)
    # print(distances, max(distances.values()))
    min_solution = min(min_solution, max(distances.values()))
    
print("dijkstra solution 1: ", min_solution) 

# I have to find the shortest path that visits all the nodes not the minimum distance from a node to all the other nodes
# I have to solve a Travelling Salesman Problem (TSP) https://en.wikipedia.org/wiki/Travelling_salesman_problem

# brute force solution
from itertools import permutations

places = set()
distances = {}
for line in input.strip().splitlines():
    source, _, dest, _, distance = line.split()
    places.add(source)
    places.add(dest)
    distances.setdefault(source, {})[dest] = int(distance)
    distances.setdefault(dest, {})[source] = int(distance)

shortest = float('infinity')
longest = 0
for items in permutations(places):
    dist = sum(map(lambda x, y: distances[x][y], items[:-1], items[1:]))
    shortest = min(shortest, dist)
    longest = max(longest, dist)

print("Solution 1: ", shortest)
print("Solution 2: ", longest)