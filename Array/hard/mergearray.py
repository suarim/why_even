arr1=[1,4,8,10]
arr2=[2,3,9]
n=len(arr1)
m=len(arr2)
l=n-1
r=0
while l>=0 and r<m:
    if arr1[l]>=arr2[r]:
        arr1[l],arr2[r]=arr2[r],arr1[l]
        l-=1
        r+=1
    else:
        break
print(sorted(arr1))
print(sorted(arr2))