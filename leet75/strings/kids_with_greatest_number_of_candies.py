candies = [2,3,5,1,3]
extraCandies = 3
res=[]
i=0
for i in candies:
    if i+extraCandies>=max(candies):
        res.append(True)
    else:
        res.append(False)
print(res)
