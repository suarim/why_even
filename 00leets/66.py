l=[1,2,3]
res=0
tens=10**(len(l)-1)
for i in range(len(l)):
    res+=l[i]*tens
    tens//=10
res=res+1
k=[]
while res:
    k.append(res%10)
    res//=10
print(k[::-1])