nums = [1,0,-1,0,-2,2]
target = 0
res=set()
h={}
for i,n in enumerate(nums):
    h[n]=i
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        for k in range(j+1,len(nums)):
            comp=target-nums[i]-nums[j]-nums[k]
            if comp in h and h[comp]!=i and h[comp]!=j and h[comp]!=k:
                res.add(tuple(sorted([nums[i],nums[j],nums[k],comp])))
print(list(res))