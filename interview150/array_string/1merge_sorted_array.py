arr1=[1,3,5,6,7,9]
arr2=[2,4,7,8,9]
k=[]
i=0
j=0
while i<len(arr1) and j<len(arr2):
    if arr1[i]<=arr2[j]:
        k.append(arr1[i])
        i+=1
    else:
        k.append(arr2[j])
        j+=1
print(k)