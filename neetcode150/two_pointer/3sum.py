nums = [-1,0,1,2,-1,-4]
res=set()
target=0
h={}
for i,n in enumerate(nums):
    h[n]=i
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if target-nums[i]-nums[j] in h and h[target-nums[i]-nums[j]]!=i and h[target-nums[i]-nums[j]]!=j:
            res.add(tuple(sorted([nums[i],nums[j],target-nums[i]-nums[j]])))
print(res)

nums = [-1,0,1,2,-1,-4]
nums.sort()
target=0
res=set()
for i in range(len(nums)):
    l=i+1
    r=len(nums)-1
    while l<r:
        s=nums[i]+nums[l]+nums[r]
        if s==target:
            res.add((sorted([nums[i],nums[l],nums[r]])))
            l+=1
            r-=1
        elif s>target:
            r-=1
        else:
            l+=1
print(res)
        
