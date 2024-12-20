graph = [[1, 2], [3], [3], []]
visited=[0]*len(graph)
stack=[]
def dfs(graph,visited,stack,node):
    visited[node]=1
    for neigh in graph[node]:
        if visited[neigh]==0:
            dfs(graph,visited,stack,neigh)
    stack.append(node)
for i in range(len(graph)):
    if visited[i]==0:
        dfs(graph,visited,stack,i)
print(stack[::-1])