nums = [2,3,1,1,4]
l=0
r=0
res=0
while r<len(nums)-1:
    far=0
    for i in range(l,r+1):
        far=max(far,i+nums[i])
    res+=1
    l=r+1
    r=far
print(res)