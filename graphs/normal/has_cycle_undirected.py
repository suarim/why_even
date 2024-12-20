
def hascycle(graph,n):
    def dfs(node,parent,visited,graph):
        visited[node]=True
        for neigh in graph[node]:
            if not visited[neigh]:
                if dfs(neigh,node,visited,graph):
                    return True
            elif neigh!=parent:
                return True
        return False
    visited=[False]*n
    for i in range(n):
        if dfs(i,-1,visited,graph) :
            return True
    return False

graph = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1, 3],
    3: [2]
}
n=len(graph)
print(hascycle(graph,n))    