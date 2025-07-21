l = [1, 2, 3]
target=7
def combosum(i,arr,comsum):
    if comsum==target:
        print(arr)
        return
    if comsum>target or i>=len(l):
        return 
    arr.append(l[i])
    combosum(i,arr,comsum+l[i])
    arr.pop()
    combosum(i+1,arr,comsum)
combosum(0,[],0)