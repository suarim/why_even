l=0
maxs=0
k=2
nums=[1,1,1,0,0,0,1,1,1,1,0]
zs=0
for r in range(len(nums)):
    if nums[r]!=0:
        maxs=max(maxs,r-l+1)
    else:
        zs+=1
    if zs<=k:
        maxs=max(maxs,r-l+1)
    else:
        while zs>k:
            if nums[l]==0:
                zs-=1
            l+=1
print(maxs)