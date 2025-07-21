nums=[1,2,3,4]
l=[1]*len(nums)
r=[1]*len(nums)
for i in range(1,len(nums)):
    l[i]=l[i-1]*nums[i-1]
print(l)
for i in range(len(nums)-2,-1,-1):
    r[i]=r[i+1]*nums[i+1]
print(r)
for i in range(len(nums)):
    nums[i]=l[i]*r[i]
print(nums)