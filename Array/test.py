s="tree"
h={}
for i in range(len(s)):
    if s[i] not in h:
        h[s[i]]=1
    else:
        h[s[i]]+=1
res=[]
for i,j in h.items():
    res.append((i,j))
print(res)
res.sort(key=lambda x:x[1],reverse=True)
for i,j in res:
    print(i*j,end="")