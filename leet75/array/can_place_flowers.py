l=[1,0,0,0,1]
ls=[0]+l+[0]
n=1
for i in range(1,len(ls)-1):
    if ls[i]==0 and ls[i-1]==0 and ls[i+1]==0:
        ls[i]=1
        n-=1
print(n==0)
