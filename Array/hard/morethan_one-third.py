import math
l=[1,1,1,1,2,3,2,2,2]
n=math.ceil(len(l)/3)
k=[]
h={}
for i in l:
    if i in h:
        h[i]+=1
    else:
        h[i]=1
for i,j in h.items():
    if j>n:
        k.append(i)
print(k)