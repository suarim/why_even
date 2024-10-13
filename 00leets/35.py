nums = [1,3,5,6]
target = 5

l=0
r=len(nums)-1
while l<=r:
    m=(l+r)//2
    if nums[m]==target:
        print(m)
        exit()
    elif nums[m]<target:
        l=m+1
    else:
        r=m-1
print(l)