nums = [1,-1,2]
for i in nums:
    if i==0:
        if sum(nums[i+1:])==0:
            print(nums[i])
            break
    elif i==len(nums)-1:
        if sum(nums[:i])==0:
            print(nums[i])
            break
    else:
        if sum(nums[i+1:])==sum(nums[:i]):
            print(nums[i])
            break
