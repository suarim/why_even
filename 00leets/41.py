nums = [3,2,0]
#[0,2,3]
missing=1
nums.sort()
for i in nums:
    if i==missing:
        missing+=1
    elif i>missing:
        break
print(missing)