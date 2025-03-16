nums = [1, 2, 3, 3]
h={}
for i in nums:
    if i in h:
        print(i)
        break   
    else:
        h[i]=1