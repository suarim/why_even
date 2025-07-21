arr=[1,2,2,2,3,4,5]
l=0
k=0
for i in range(len(arr)):
    if arr[i]!=2:
        arr[l]=arr[i]
        l+=1
print(arr[:l])
    