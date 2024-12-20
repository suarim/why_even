def soln(grid):
    def dfs(grid,i,j):
        visited[i][j]='1'
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        for x,y in directions:
            dx,dy=i+x,j+y
            if 0<=dx<len(grid) and 0<=dy<len(grid[0]) and grid[dx][dy]=='1' and visited[dx][dy]=='0':
                
                dfs(grid,dx,dy)
    count=0
    visited=[['0']*len(grid[0]) for i in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]=='1' and visited[i][j]=='0':
                count+=1
                dfs(grid,i,j)
    return count


grid = [
['1','1','0'],['1','1','0'],['0','0','1']
]

print(soln(grid))