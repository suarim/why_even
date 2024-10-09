l=[1,2,-1,3]
res=max(l)
curmin,curmax=1,1
for i in l:
    if i==0:
        curmax,curmin=1,1
        continue
    temp=curmax*i
    curmax=max(curmax*i,i,curmin*i)
    curmin=min(temp,i,curmax*i)
    res=max(res,curmax)
print(res)