l=[7,7,7,7,13,11,12,7]
m=2
k=3
def min_bouquet(l,day,m,k):
    c=0
    no=0
    for i in l:
        if day>=i:
            c+=1
        else:
            no+=c//k
            c=0
    no+=c//k
    return no>=m
low=min(l)
high=max(l)
ans=0
if m*k>len(l):
    print(-1)
    exit()
while low<=high:
    mid=(low+high)//2 
    if min_bouquet(l,mid,m,k):
        ans=mid
        high=mid-1
    else:
        low=mid+1
print(ans)
    
