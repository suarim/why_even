l=[100,5,200,1,2,3,6,4]
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

l = [100, 5, 200, 1, 2, 3, 6, 4]
numset = set(l)
streak =1 
for num in numset:
    if num-1 not in numset:
        curnum = num
        curstreak = 1
        while curnum+1 in numset:
            curnum+=1
            curstreak+=1
        streak = max(streak,curstreak)
print(streak)