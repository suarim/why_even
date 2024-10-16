nums = [1,2,0]
missing=1
nums.sort()
for i in range(0,len(nums)):
    if nums[i]==missing:
        missing+=1
    elif i>missing:
        break
print(missing)