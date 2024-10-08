
l=[1,2,-5,4,5,-3,90]
msf=-9999
meh=0
cs=0
for i in l:
    meh+=i
    if meh<i:
        meh=i
        cs=i
    if msf<meh:
        msf=meh
        s=cs
        e=i
print(msf)
print(l[s-1:e])