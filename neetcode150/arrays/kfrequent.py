nums = [1,2,2,3,3,3]
k = 2
h={}
for i in nums:
    if i in h:
        h[i]+=1
    else:
        h[i]=1
print(h)
for i,j in h.items():
    if j>=k:
        print(i)
        