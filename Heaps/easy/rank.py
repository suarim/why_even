l=[1,5,8,15,8,25,9]
l.sort()
print(l)
h={}
z=1
for i in range(len(l)):
    if l[i] not in h:
        h[l[i]]=z
        z+=1
print(h)
for i in l:
    print(h[i])