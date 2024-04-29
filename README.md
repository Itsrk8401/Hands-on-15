# Hands-on-15

These are all classic algorithms used for finding shortest paths in graphs, but they differ in their approaches and applications:

1. # Dijkstra's Algorithm:
   - It's a greedy algorithm used to find the shortest path between a single source node and all other nodes in a weighted graph with non-negative edge weights.
   - It maintains a set of vertices whose shortest distance from the source node is already known, and iteratively expands this set until it reaches the destination.
   - Dijkstra's algorithm can't handle negative edge weights, as it assumes that once a node's shortest path is determined, it is finalized.

2. # Bellman-Ford Algorithm:
   - This algorithm can handle graphs with negative edge weights, unlike Dijkstra's algorithm.
   - It iterates through all edges of a graph a number of times equal to the number of vertices minus one, relaxing the edges each time to improve the accuracy of the shortest path estimates.
   - Bellman-Ford detects negative weight cycles, which can be useful in some applications.

3. # Floyd-Warshall Algorithm:
   - It's used to find the shortest paths between all pairs of vertices in a weighted graph, including graphs with negative edge weights (but no negative cycles).
   - Floyd-Warshall works by considering all possible paths between pairs of vertices and progressively updating the shortest path lengths.
   - Unlike Dijkstra's and Bellman-Ford, Floyd-Warshall's complexity is O(V^3), making it less efficient for most single-source shortest path problems, but it's efficient for finding shortest paths between all pairs of vertices.
