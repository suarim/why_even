height = [30, 10, 60, 10, 60, 50]
n = len(height)
k = 2
dp=[9999999999 for _ in range(n)]
dp[0]=0
mmstep=float('inf')
for i in range(1,n):
    for j in range(1,k+1):
        if i-j>=0:
            jump=dp[i-j]+abs(height[i]-height[i-j])
            dp[i]=min(dp[i],jump) 
print(dp[-1])