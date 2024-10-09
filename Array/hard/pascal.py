def nCr(n,r):
    res=1
    for i in range(r):
        res*=(n-i)
        res//=(i+1)
    return res

print(nCr(5,1)) 

n=5
for i in range(n+1):
    print(nCr(5,i),end=" ")

print("\n")
ans=[]
for i in range(5):
    temp=[]
    for j in range(i+1):
        print(nCr(i,j),end=" ")
        temp.append(nCr(i,j))
    ans.append(temp)
    print("\n")
print(ans)