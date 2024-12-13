g=[1,5,3,3,4]
s=[4,2,1,2,1,3]
g.sort()
s.sort()
l=0
r=0
while l<len(g) and len(s)>r:
    if g[l]<=s[r]:
        l+=1
    r+=1
print(l)