l=[1,2,3,4,5,6,7,8,9,10]
cap=10
days=5
ans=-1
def count(l,cap):
    no=1
    load=0
    for i in l:
        if i+load>cap:
            no+=1
            load=i
        else:
            load+=i
    print(no)
    return no
low=max(l)
high=sum(l)
x=[i for i in range(low,high+1)]
print("x->",x)
while low<=high:
    mid=(low+high)//2
    print("mid->",mid)
    if count(l,mid)<=days:
        ans=mid
        high=mid-1
    else:
        low=mid+1
print(ans)    