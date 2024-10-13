nums = [3,3]
target = 6
h={}
for i,n in enumerate(nums):
    if target-n in h:
        print([h[target-n],i])
        break
    h[n]=i