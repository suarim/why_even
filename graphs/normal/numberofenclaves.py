def soln(grid):
    def dfs(grid,i,j,visited):
        visited[i][j]=1
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        for x,y in directions:
            dx,dy=i+x,j+y
            if 0<=dx<len(grid) and 0<=dy<len(grid[0]) and grid[dx][dy]==1 and visited[dx][dy]==0:
                dfs(grid,dx,dy,visited)
        
    rows=len(grid)
    cols=len(grid[0])
    visited=[[0]*cols for i in range(rows)]
    for i in range(cols):
        if grid[0][i]==1 and visited[0][i]==0:
            dfs(grid,0,i,visited)
        if grid[rows-1][i]==1 and visited[rows-1][i]==0:
            dfs(grid,rows-1,i,visited)
    for i in range(rows):
        if grid[i][0]==1 and visited[i][0]==0:
            dfs(grid,i,0,visited)
        if grid[i][cols-1]==1 and visited[i][cols-1]==0:
            dfs(grid,i,cols-1,visited)
    count=0
    for i in range(rows):
        for j in range(cols):
            if visited[i][j]==0 and grid[i][j]==1:
                count+=1
    return count


grid = [[1,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
print(soln(grid))