s="52678768777222"
for i in range(len(s)-1,-1,-1):
    if int(s[:i+1])%2!=0:
        print(s[:i+1])
        break
print("")


s="52678768777322"
low=0
high=len(s)-1
ans=-1
while low<=high:
    mid=(low+high)//2
    if int(s[:mid])%2!=0:
        ans=s[:mid+1]
        low=mid+1
    else:
        high=mid-1
print(ans[:-1])