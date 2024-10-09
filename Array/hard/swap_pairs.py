arr = [3, 1, 5, 4, 2, 100, -90, 0]
inv=0
def merge(l,r):
    global inv
    i=0
    j=0
    while i<len(l) and j<len(r):
        if l[i]>2*l[j]:
            inv+=len(l)-i
            j+=1
        else:
            i+=1
    result=[]
    i=0
    j=0
    while i<len(l) and j<len(r):
        if l[i]<r[j]:
            result.append(l[i])
            i+=1
        else:
            result.append(r[j])
            j+=1
            
    result.extend(l[i:])
    result.extend(r[j:])
    return result
    
def mergesort(arr):
    if len(arr)<=1:
        return arr
    m=len(arr)//2
    l=mergesort(arr[:m])
    r=mergesort(arr[m:])
    return merge(l,r)
sorted_arr = mergesort(arr)
print(sorted_arr)
print(inv)
#O(nlogn)
#Ω(nlogn)
#works well for large data sets
