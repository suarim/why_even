nums=[3,1,3,4,3]
k = 6
l=0
c=0
r=len(nums)-1
nums.sort()
while l<r:
    if nums[l]+nums[r]==k:
        l+=1
        r-=1
        c+=1
    elif nums[l]+nums[r]>k:
        r-=1
    else:
        l+=1
print(c)