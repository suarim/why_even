l=[20,15,26,2,98,6]
z=sorted(l)
d={}
for i,n in enumerate(z):
    if n not in d:
        d[n]=i+1
k=[]
for i in l:
    k.append(d[i])
print(k)