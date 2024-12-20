import heapq

def prims_algorithm(adj, start):
    key=[float('inf')]*len(adj)
    parent=[None]*len(adj)
    mst=[False]*len(adj)
    key[start]=0
    pq=[(0,start)]
    while pq:
        curkey,cur=heapq.heappop(pq)
        if mst[cur]:
            continue
        mst[cur]=True
        for neigh,weight in adj[cur]:
            if not mst[neigh] and weight<key[neigh]:
                key[neigh]=weight
                parent[neigh]=cur
                heapq.heappush(pq,(key[neigh],neigh))
    return parent
adj = [
    [(1, 2), (3, 6)],  # Node 0 -> Node 1 (2), Node 0 -> Node 3 (6)
    [(0, 2), (2, 3), (3, 8)],  # Node 1 -> Node 0 (2), Node 2 (3), Node 3 (8)
    [(1, 3), (3, 7)],  # Node 2 -> Node 1 (3), Node 3 (7)
    [(0, 6), (1, 8), (2, 7)]   # Node 3 -> Node 0 (6), Node 1 (8), Node 2 (7)
]
start = 0

# Run Prim's algorithm starting from node 0
mst = prims_algorithm(adj, start)
print(mst)
