l=[5,5,2,3,3,5,3]
l.sort()
for i in range(1,len(l),3):
    if l[i]!=l[i-1]:
        print(l[i-1])
        exit()
print(l[-1])