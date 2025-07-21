arr=[1,2,3,4]

def subseq(indx,l):
    if len(l)!=0 and checkincreasing(l):
        print(l)
        # no return here

    if indx>=len(arr):
        return

    l.append(arr[indx])
    subseq(indx+1,l)
    l.pop()
    subseq(indx+1,l)

def checkincreasing(l):
    for i in range(1,len(l)):
        if l[i-1] > l[i]:
            return False
    return True

subseq(0,)
