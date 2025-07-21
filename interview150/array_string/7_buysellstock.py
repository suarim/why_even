prices = [7,1,5,3,6,4]
minbuyprice=999
maxsellprice=999
maxpro=-999
for i in prices:
   
   minbuyprice = min(minbuyprice,i)
   maxpro=max(maxpro,i-minbuyprice)
print(maxpro)