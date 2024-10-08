l=[1,1,1,1,0,0,0,2,2,2,1,1,1,0,0,0]
c0=0
c1=0
c2=0
for i in l:
    if i==0:
        c0+=1
    elif i==1:
        c1+=1
    else:
        c2+=1
for i in range(c0):
    l[i]=0
for i in range(c0,c0+c1):
    l[i]=1
for i in range(c0+c1,c0+c1+c2):
    l[i]=2
print(l)
# O(n)