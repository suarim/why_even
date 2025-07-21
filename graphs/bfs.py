from collections import deque
adj = [[1,2], [0,2,3], [0,4], [1,4], [2,3]]
q=deque()
visited=[False for i in range(len(adj))]
s=0
visited[s]=True
# res=[s]
res=[]
q.append(s)
while q:
    cur= q.popleft()
    visited[cur]=True
    res.append(cur)

    for x in adj[cur]:
        if visited[x] is not True:
            visited[x]=True
            q.append(x)
print(res)