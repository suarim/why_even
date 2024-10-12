l=[4,7,9,10]
k=4
for i in l:
    if i<=k:
        k+=1
    else:
        print(k)
        break

arr=[]
for i in range(1,len(l)+1):
    arr.append(l[i-1]-i)
print(arr)
low=0
high=len(l)-1
while low<=high:
    m=(low+high)//2
    print("lowI->",low)
    print("highI->",high)
    print("mI->",m)
    print("\n")
    if arr[m]<k:
        low=m+1
    else:
        high=m-1
    print("low->",low)
    print("high->",high)
    print("m->",m)
    print("\n")

print(high)


low=0
high=len(l)-1
while low<=high:
    m=(low+high)//2
    missing=l[m]-m-1
    if missing<k:
        low=m+1
    else:
        high=m-1
print(high+k)