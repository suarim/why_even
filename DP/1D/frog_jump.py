height = [30, 10, 60, 10, 60, 50]
n = len(height)
dp = [-1 for _ in range(n)]
dp[0] = 0
j1,j2=0,0
for i in range(1,n):
    j1=abs(height[i]-height[i-1])+dp[i-1]
    if i>1:
        j2=abs(height[i]-height[i-2])+dp[i-2]   
    dp[i]=min(j1,j2)
print(dp[-1])