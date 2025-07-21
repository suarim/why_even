l=[2,3]
ans=[]
def subsetsum(indx,arr):
    if indx>=len(l):
        ans.append(sum(arr))
        return
    arr.append(l[indx])
    subsetsum(indx+1,arr)
    arr.pop()
    subsetsum(indx+1,arr)
subsetsum(0,[])
print(sorted(ans))