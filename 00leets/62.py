m = 3
n = 7
dp=[[1]*m]*n
for i in range(1,n):
    for j in range(1,m):
        dp[i][j]=dp[i-1][j]+dp[i][j-1]
print(dp[-1][-1])