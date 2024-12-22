from collections import deque

def is_bipartite(graph):
    color = {}

    for node in graph:
        if node not in color:
            # Start BFS for this component
            queue = deque([node])
            color[node] = 1  # Assign the first color

            while queue:
                current = queue.popleft()

                for neighbor in graph[current]:
                    if neighbor not in color:
                        # Assign the opposite color to the neighbor
                        color[neighbor] = -color[current]
                        queue.append(neighbor)
                    elif color[neighbor] == color[current]:
                        # If the neighbor has the same color, it's not bipartite
                        return False

    return True

# Example usage
graph_bipartite = {
    0: [1, 3],
    1: [0, 2],
    2: [1, 3],
    3: [0, 2]
}

graph_not_bipartite = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1]
}

print(is_bipartite(graph_bipartite))  # Output: True (Graph is bipartite)
print(is_bipartite(graph_not_bipartite))  # Output: False (Graph is not bipartite)
