l=[100,200,1,2,3,6,4]
def linear_search(l,x):
    for i in range(len(l)):
        if l[i]==x:
            return True
    return False
ln=1

for i in range(len(l)):
    x=l[i]
    cn=1
    while linear_search(l,x+1):
        cn+=1
        x+=1
    ln=max(ln,cn)
print(ln)

st=set(l)
ln=1
for it in st:
    if it-1 not in st:
        x=it
        c=1
        while x+1 in st:
            x+=1
            c+=1
        ln=max(ln,c)
print(ln)