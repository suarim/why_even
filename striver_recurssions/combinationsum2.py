l = [10, 1, 2,7,6,1,5]
ans=set()
def combosum2(indx,arr):
    if indx>=len(l):
        if sum(arr)==8:
            ans.add(tuple(sorted(arr)))
        return
    arr.append(l[indx])
    combosum2(indx+1,arr)
    arr.pop()
    combosum2(indx+1,arr)
combosum2(0,[])
print(list(ans))