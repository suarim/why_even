s='abcdab'
l=0
res=set()
maxs=0
for i in range(len(s)):
    if s[i] in res:
        res.remove(s[l])
        l+=1
    res.add(s[i])
    maxs=max(maxs,i-l+1)
print(maxs)