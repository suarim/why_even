import heapq
adj = [
    [(1, 1), (2, 4)],  # Node 0 -> Node 1 (weight 1), Node 0 -> Node 2 (weight 4)
    [(2, 2), (3, 5)],  # Node 1 -> Node 2 (weight 2), Node 1 -> Node 3 (weight 5)
    [(3, 1)],          # Node 2 -> Node 3 (weight 1)
    []                 # Node 3 has no outgoing edges
]
src = 0
pq=[(0,src)]
dist=[float('inf')]*len(adj)
dist[src]=0
while pq:
    curdist,srcc=heapq.heappop(pq)
    if dist[srcc]<curdist:
        continue
    for neigh,weight in adj[srcc]:
        if curdist+weight<dist[neigh]:
            dist[neigh]=curdist+weight
            heapq.heappush(pq,(dist[neigh],neigh))
print(dist)