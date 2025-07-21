l=[1,2,3,1]
def subsequence(indx,arr):
    if indx>=len(l):
        if sum(l)==4:
            print(arr)
        return
    arr.append(l[indx])
    subsequence(indx+1,arr)
    arr.pop()
    subsequence(indx+1,arr)
subsequence(0,[])