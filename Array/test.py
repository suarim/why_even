l=[1,0,0,0,1]
l=[0]+l+[0]
n=2
for i in range(1,len(l)-1):
    if l[i]==0 and l[1+i]==0 and l[i-1]==0:
        l[i]=1
        n-=1
print(n==0)
