s="tree"
h={}
for i in range(len(s)):
    if s[i] not in h:
        h[s[i]]=1
    else:
        h[s[i]]+=1
print(h)
l=sorted(h.items(),key=lambda x:x[1],reverse=True)
for (i,j) in l:
    print(i*j,end="")   