l = [9,128,-130]
res=[]
for i in range(len(l)):
    b=l[i]
    if b==7:
        res.append([b])
    for j in range(i+1,len(l)):
        b+=l[j]
        if b==7:
            res.append(l[i:j+1])
            break
        if b>7:
            break
print(res)