n=3
dp=[0*(i+1) for i in range(n+1)]
dp[0]=1
dp[1]=2
for i in range(2,n+1):
    dp[i]=dp[i-1]+dp[i-2]
print(dp[n])