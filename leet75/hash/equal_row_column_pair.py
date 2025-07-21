grid = grid = [[3,1,2,2],
               [1,4,4,4],
               [2,4,2,2],
               [2,5,2,2]]
v1={}
v1set=set()
v2set=set()
l1=[]
l2=[]
for i,n in enumerate(grid):
    v1[i]=n
    v1set.add(tuple(n))
    l1.append(tuple(n))
print(l1)
v2={}
for i in range(len(grid[0])):
    v2[i]=[]
    for j in range(len(grid)):
        v2[i].append(grid[j][i])
        v2set.add(tuple(v2[i]))
    l2.append(tuple(v2[i]))
print(l2)
c=0
# print(v1set.intersection(v2set))
for i in l1:
    if i in l2:
        c+=1
p=0
for i in l2:
    if i in l1:
        p+=1
print(max(c,p))