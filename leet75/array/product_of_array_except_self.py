nums=[1,2,3,4]
res=[1]*len(nums)
pre=1
for i in range(len(nums)):
    res[i]=pre
    pre*=nums[i]
print(res)
post=1
for i in range(len(nums)-1,-1,-1):
    res[i]=post
    post*=nums[i]

print(res)