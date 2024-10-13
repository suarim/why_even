nums = [5,7,7,8,8,10]
target = 8
def first(nums,target):
    l=0
    ans=0
    r=len(nums)-1
    while l<=r:
        m=(l+r)//2
        if nums[m]==target:
            ans=m
            r=m-1
        elif nums[m]<target:
            l=m+1
        else:
            r=m-1
    return ans
ans=0
def last(nums,target):
    l=0
    ans=0
    r=len(nums)-1
    while l<=r:
        m=(l+r)//2
        if nums[m]==target:
            ans=m
            l=m+1
        elif nums[m]<target:
            l=m+1
        else:
            r=m-1
    return ans
print(first(nums,target))
print(last(nums,target))
