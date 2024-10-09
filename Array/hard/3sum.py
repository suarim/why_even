numbers = [0,1, 2, 3, 4, 5]
h={}
res=set()
for i,n in enumerate(numbers):
    h[n]=i
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        comp=8-(numbers[i]+numbers[j])
        if comp in h and h[comp]!=i and h[comp]!=j:
            res.add(tuple(sorted([numbers[i],numbers[j],comp])))
print(res)

res=set()
for i in range(len(numbers)):
    x=numbers[i]
    l=i+1
    r=len(numbers)-1
    while l<r:
        s=x+numbers[l]+numbers[r]
        if s==8:
            res.add(tuple(sorted([x,numbers[l],numbers[r]])))
            l+=1
            r-=1
        elif s<8:
            l+=1
        else:
            r-=1
print(res)