nums = [0,1,0,3,12,0]
p=0
pos=0
for i in range(len(nums)):
    if nums[i]!=0:
        nums[pos]=nums[i]
        pos+=1
print(nums[:pos]+[0]*(len(nums)-pos))
