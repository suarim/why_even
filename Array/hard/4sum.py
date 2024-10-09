numbers = [0,1, 2, 3, 4, 5]
res=set()
h={}
for i,n in enumerate(numbers):
    h[n]=i
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        for k in range(j+1,len(numbers)):
            comp=8-(numbers[i]+numbers[j]+numbers[k])
            if comp in h and h[comp]!=i and h[comp]!=j and h[comp]!=k:
                res.add(tuple(sorted([numbers[i],numbers[j],numbers[k],comp])))
print(res)
