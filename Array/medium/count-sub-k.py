l = [3, 4, 7, 1, 6, 7,2,3,2,9,-2]
sub=[]
for i in range(len(l)):
    b=l[i]
    if b==7:
        sub.append([b])
    for j in range(i+1,len(l)):
        b+=l[j]
        if b>7:
            break
        if b==7:
            sub.append(l[i:j+1])
            break
print(len(sub))