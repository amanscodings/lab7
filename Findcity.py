from typing import List
import heapq

def findTheCity(n: int, edges: List[List[int]], distanceThreshold: int) -> int:
    # Create an adjacency matrix to represent the graph
    graph = [[float('inf')] * n for _ in range(n)]
    for u, v, w in edges:
        graph[u][v] = w
        graph[v][u] = w


    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


    reachable_cities = [0] * n
    for i in range(n):
        for j in range(n):
            if i != j and graph[i][j] <= distanceThreshold:
                reachable_cities[i] += 1


    min_reachable = min(reachable_cities)
    smallest_cities = [i for i, count in enumerate(reachable_cities) if count == min_reachable]

   
    return max(smallest_cities)

print(findTheCity(5, [[0,1,2], [0,4,8], [1,2,3], [1,4,2], [2,3,1], [3,4,1]], 2))  
print(findTheCity(4, [[0,1,3], [1,2,1], [1,3,4], [2,3,1]], 4)) 
