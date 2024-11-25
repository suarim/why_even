s="leetcode exercises sound delightfup"
l=s.split()
print(l)
p=1
for i in range(1,len(l)):
    if l[i][0]==l[i-1][-1]:
        print(l[i][0])
        p=1
    else:
        p=0
        print(False)
        exit()
if p==1:
    print(l[0][0]==l[-1][-1])
