For this approach i used the Floyd-Warshall approach because it distances between all pairs of cities. Then the adjency matrix fills edges, i thought it would be good.
It iterates through the cities, counting the number of cities reachable within the distance threshold for each city, 
and returns the city number with the minimum number of reachable cities.
