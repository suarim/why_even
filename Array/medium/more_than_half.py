l=[2,2,1,1,1,2,2]
c=0
for i in range(len(l)):
    if c==0:
        c=1
        ele=l[i]
    elif ele==l[i]:
        c+=1
    else:
        c-=1
print(ele)