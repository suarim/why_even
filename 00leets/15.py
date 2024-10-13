nums = [-1,0,1,2,-1,-4]
h={}
for i,n in enumerate(nums):
    h[n]=i  
res=set()
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if -nums[i]-nums[j] in h:
            if h[-nums[i]-nums[j]]!=i and h[-nums[i]-nums[j]]!=j:
                res.add(tuple(sorted([nums[i],nums[j],-nums[i]-nums[j]])))
print(res)