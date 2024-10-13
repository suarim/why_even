nums = [0,0,0]
target = 1
cls=999999999
nums.sort()
for i in range(len(nums)):
    l=i+1
    r=len(nums)-1
    while l<r:
        s=nums[i]+nums[l]+nums[r]
        if abs(s-target)<abs(cls-target):
            cls=s
        if s==target:
            print(s)
            exit()
        if s<target:
            l+=1
        else:
            r-=1
print(cls)
