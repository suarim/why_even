from collections import deque
adj = [
    [0, 1, 1, 0, 0],
    [1, 0, 1, 1, 0],
    [1, 1, 0, 0, 1],
    [0, 1, 0, 0, 1],
    [0, 0, 1, 1, 0]
]
src = 0
q=deque([src])
dist=[-1]*len(adj)
dist[src]=0
n=len(adj)
while q:
    node=q.popleft()
    for i in range(n):
        if adj[node][i]==1 and dist[i]==-1:
            dist[i]=dist[node]+1
            q.append(i)
print(dist)