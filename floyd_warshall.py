def floyd_warshall(graph):
    n = len(graph)
    distances = [[float('infinity')] * n for _ in range(n)]
    
    for i in range(n):
        distances[i][i] = 0
        for neighbor, weight in graph[i].items():
            distances[i][neighbor] = weight
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])
    
    return distances

# Example usage:
graph = {
    0: {1: 3, 3: 8},
    1: {0: 3, 2: 1},
    2: {0: 5, 3: 2},
    3: {2: 2}
}
print(floyd_warshall(graph))
