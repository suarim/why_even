s1="cat"
s2="tac"
s1=sorted(s1)
s2=sorted(s2)
print(s1==s2)

s1="cat"
s2="sac"
d1={}
d2={}
for i in s1:
    if i in d1:
        d1[i]+=1
    else:
        d1[i]=1
for i in s2:
    if i in d2:
        d2[i]+=1
    else:
        d2[i]=1
print(d1==d2)