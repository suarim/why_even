n=17
l=1
[1,2,3,4,5]
ans=0
r=n
while l<=r:
    m=(l+r)//2
    if m*m<=n:
        ans=m
        l=m+1
    else:
        r=m-1
print(ans)
