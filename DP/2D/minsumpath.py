
def minPathSum(grid):
    m=len(grid)
    n=len(grid[0])
    dp=[[0]*n for _ in range(m)]
    dp[0][0]=grid[0][0]
    for i in range(1,n):
        dp[0][i]=dp[0][i-1]+grid[0][1]
    for i in range(1,m):
        dp[i][0]=dp[i-1][0]+grid[i][0]
    for i in range(1,m):
        for j in range(1,n):
            dp[i][j]=min(dp[i-1][j],dp[i][j-1])+grid[i][j]
    return dp[-1][-1]

grid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]

print(minPathSum(grid))