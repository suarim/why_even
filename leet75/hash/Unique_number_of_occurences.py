from collections import Counter
arr = [1,2,2,1,1,2]
count=Counter(arr)
print(count)
res1=set()
res2=set()
for i,v in count.items():
    res1.add(i)
    res2.add(v)
print(len(res1)==len(res2))