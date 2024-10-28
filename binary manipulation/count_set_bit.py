n=2
c=0
res=""
while n!=0:
    res+=str(n%2)
    if n%2==1:
        c+=1
    n//=2
print(c)