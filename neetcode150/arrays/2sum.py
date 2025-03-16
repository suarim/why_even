nums = [3,4,5,6]
target = 7
h={}
for i,n in enumerate(nums):
    h[n]=i
for i in range(len(nums)):
    if target-nums[i] in h and h[target-nums[i]]!=i:
        print([i,h[target-nums[i]]])
        break