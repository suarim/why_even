l=[5,4,-1,7,8]
msf=0
meh=0
cs=0
for i in l:
    meh+=i
    if meh<i:
        meh=i
    if msf<meh:
        msf=meh
print(msf)