
from collections import deque
def dist(mat):
    q=deque()
    visited=[[0]*len(mat[0]) for i in range(len(mat))]
    distance=[[0]*len(mat[0]) for i in range(len(mat))]
    directions=[(0,1),(0,-1),(1,0),(-1,0)]
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j]==0:
                q.append((i,j,0))
                visited[i][j]=1
    while q:
        r,c,d=q.popleft()
        distance[r][c]=d
        for i,j in directions:
            nr,nc=i+r,j+c
            if 0<=nr<len(mat) and 0<=nc<len(mat[0]) and mat[nr][nc]==1  and visited[nr][nc]==0:
                visited[nr][nc]=1
                # distance[nr][nc]=d+1
                q.append((nr,nc,d+1))
    return distance


mat = [[0,0,0],[0,1,0],[1,1,1]]
print(dist(mat))