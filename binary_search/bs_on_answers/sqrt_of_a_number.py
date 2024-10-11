n=69
for i in range(1,n//2+1):
    if i*i==n:
        print(i)
        break
    if i*i>n:
        print(i-1)
        break

low=1
high=n
while low<=high:
    m=(low+high)//2
    if m*m<=n:
        ans=m
        low=m+1
    else:
        high=m-1
print(ans)
    