arr1=[1,2]
arr2=[3,4,5]
i=0
j=0
n=len(arr1)+len(arr2)
ind1=n//2
ind2=n//2-1
c=0
e1=-1
e2=-1
while i<len(arr1) and j<len(arr2):
    if arr1[i]<arr2[j]:
        if c==ind1:
            e1=arr1[i]
        if c==ind2:
            e2=arr1[i]
        i+=1
    else:
        if c==ind1:
            e1=arr2[j]
        if c==ind2:
            e2=arr2[j]
        j+=1
    c+=1
while i<len(arr1):
    if c==ind1:
        e1=arr1[i]
    if c==ind2:
        e2=arr1[i]
    i+=1
    c+=1
while j<len(arr2):
    if c==ind1:
        e1=arr2[j]
    if c==ind2:
        e2=arr2[j]
    j+=1
    c+=1
if n%2==0:
    print((e1+e2)/2)
else:
    print(e1)