l=[1,0,0,0,0,1,0,1,1,1,0,1]
start=0
zc=0
k=1
maxc=-9999
for i in range(len(l)):
    if l[i]==0:
        zc+=1
    while zc >k:
        if l[start]==0:
            zc-=1
        start+=1
    maxc=max(maxc,i-start+1)
print(maxc)
    