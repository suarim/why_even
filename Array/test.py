l=[2,1,5,4,3,0,0]
indx=-1
n=len(l)
for i in range(n-2,-1,-1):
    if l[i]<l[i+1]:
        indx=i
        break
print(indx)
print(l[indx+1:])
if indx==-1:
    l.sort()
    print(l)
    exit()
for i in range(n-1,indx,-1):
    if l[i]>l[indx]:
        l[i],l[indx]=l[indx],l[i]
        break
l[indx+1:]=l[indx+1:][::-1]
print(l)