def has_cycle_directed(graph):
    visited = set()
    rec_stack = set()

    def dfs(node):
        if node in rec_stack:  # Cycle detected
            return True
        if node in visited:  # Already processed node
            return False

        # Mark the current node as visited and add to recursion stack
        visited.add(node)
        rec_stack.add(node)

        # Explore all neighbors
        for neighbor in graph[node]:
            if dfs(neighbor):
                return True

        # Remove the node from recursion stack after processing
        rec_stack.remove(node)
        return False

    # Check for cycles in all components
    for node in graph:
        if node not in visited:
            if dfs(node):
                return True

    return False

# Example usage
graph_acyclic = {
    0: [1, 2],
    1: [2],
    2: [],
    3: [0, 4],
    4: []
}

graph_cyclic = {
    0: [1],
    1: [2],
    2: [0],
    3: [4],
    4: []
}

print(has_cycle_directed(graph_acyclic))  # Output: False (No cycle)
print(has_cycle_directed(graph_cyclic))  # Output: True (Cycle exists)
