s = "abcadbca"
res=set()
l=0
maxs=0
for i in range(len(s)):
    while s[i] in res:
        res.remove(s[l])
        l+=1
    res.add(s[i])
    maxs=max(maxs,i-l+1)
print(maxs)