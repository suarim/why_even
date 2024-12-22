def kkk(nums):
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]
    if n == 2:
        return max(nums[0], nums[1])
    
    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    
    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])
    
    return dp[-1]

# Main logic
nums = [2,3,2]
n = len(nums)

if n == 1:
    print(nums[0])
elif n == 2:
    print(max(nums))
else:
    # Call the kkk function for two cases
    result = max(kkk(nums[1:]), kkk(nums[:-1]))
    print(result)
