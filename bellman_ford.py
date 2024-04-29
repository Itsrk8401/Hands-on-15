def bellman_ford(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node].items():
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight
    
    # Check for negative weight cycles
    for node in graph:
        for neighbor, weight in graph[node].items():
            if distances[node] + weight < distances[neighbor]:
                raise ValueError("Graph contains a negative weight cycle")
    
    return distances

# Example usage:
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'D': -1},
    'C': {'A': 2, 'D': 1},
    'D': {'B': -2, 'C': 3}
}
start_node = 'A'
print(bellman_ford(graph, start_node))
