
def bfs(grid):
    direction=[(1,0),(0,1),(-1,0),(0,-1)]
    fresh=0
    time=0
    q=[]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]==2:
                q.append((i,j))
            elif grid[i][j]==1:
                fresh+=1
    while q and fresh>0:
        for _ in range(len(q)):
            r,c=q.pop(0)
            for i,j in direction:
                nr,nc=r+i,c+j
                if 0<=nr<len(grid) and 0<=nc<len(grid[0]) and grid[nr][nc]==1:
                    grid[nr][nc]=2
                    fresh-=1
                    q.append((nr,nc))
        time+=1
    return time if fresh==0 else -1

grid = [[2,1,1],[1,1,0],[0,1,1]]
print(bfs(grid))