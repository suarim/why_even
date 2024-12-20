
graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
color=[-1]*len(graph)
def dfs(node,col):
    color[node]=col
    for neigh in graph[node]:
        if color[neigh]==-1:
            if not dfs(neigh,1-col):
                return False
        elif color[neigh]==color[node]:
            return False
    return True
for i in range(len(graph)):
    if color[i]==-1:
        if not dfs(i,0):
            print(False)