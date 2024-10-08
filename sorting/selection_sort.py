arr=[3,1,5,4,2]
def getmax(start,end):
    max=arr[start]
    x=start
    for i in range(start,end+1):
        if arr[i]>max:
            max=arr[i]
            x=i
    return x
for i in range(len(arr)):
    last=len(arr)-i-1
    maxindex=getmax(0,last)
    arr[maxindex],arr[last]=arr[last],arr[maxindex]
print(arr)

# O(n^2)
# Ω(n^2)
#works well for small data sets
