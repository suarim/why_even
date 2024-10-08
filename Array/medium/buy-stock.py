l=[7,1,5,3,6,4,7]
maxprofit=0
minprice=l[0]
for i in range(1,len(l)):
    if l[i]<minprice:
        minprice=l[i]
    else:
        maxprofit=max(maxprofit,l[i]-minprice)
print(maxprofit)