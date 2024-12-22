nums = [2,7,9,3,1]
n = len(nums)
if n==1:
    print(nums[0])
if n==2:
    print(max(nums))
dp=[0]*n
dp[0]=nums[0]
dp[1]=max(nums[0],nums[1])
for i in range(2,n):
    dp[i]=max(dp[i-1],dp[i-2]+nums[i])
print(dp[-1])