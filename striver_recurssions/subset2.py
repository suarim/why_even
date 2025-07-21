l=[1,2,2]
ans=set()
def subset2(indx,arr):
    if indx>=len(l):
        ans.add(tuple(sorted(arr)))
        return
    arr.append(l[indx])
    subset2(indx+1,arr)
    arr.pop()
    subset2(indx+1,arr)
subset2(0,[])
print(ans)