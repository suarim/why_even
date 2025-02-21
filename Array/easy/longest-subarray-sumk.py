l = [3, 4, 7, 1, 6, 7,2,3,2,97,-90]
sub=[]
for i in range(len(l)):
    b=l[i]
    if b==7:
        sub.append([b])
    for j in range(i+1,len(l)):
        b+=l[j]
        if b>7:
            break
        if b != 7:
            continue
        else:
            sub.append(l[i:j+1])
            break
mm=0
for i in sub:
    mm=max(mm,len(i))
print(sub)
print(mm)