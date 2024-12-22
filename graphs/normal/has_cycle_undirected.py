from collections import deque

def has_cycle_bfs(graph):
    visited = set()

    def bfs(start):
        queue = deque([(start, -1)])  # (current_node, parent_node)
        visited.add(start)

        while queue:
            node, parent = queue.popleft()

            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, node))
                elif neighbor != parent:
                    # If the neighbor is visited and not the parent, a cycle exists
                    return True
        return False

    # Check all components of the graph
    for node in graph:
        if node not in visited:
            if bfs(node):
                return True

    return False

# Example usage
graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0],
    3: [1, 4],
    4: [3]
}

print(has_cycle_bfs(graph))  # Output: False (No cycle in the graph)

graph_with_cycle = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1],
    3: [4],
    4: [3]
}

print(has_cycle_bfs(graph_with_cycle))  # Output: True (Cycle exists)
