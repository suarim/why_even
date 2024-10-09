l=[4,7,1,-1,0]
leader=[l[-1]]
x=l[-1]
for i in range(len(l)-2,-1,-1):
    if l[i]>x:
        leader.append(l[i])
        x=l[i]
print(leader)