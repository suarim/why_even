l=[1,1,1,2,3,4,4,4,5,5,5,5,7,8,8]
set=set(l)
i=0
print(set)
for x in set:
    l[i]=x
    i+=1
print(i)
print(l[:i])

l = [1, 1, 1, 2, 3, 4, 4, 4, 5, 5, 5, 5, 7, 8, 8]
k = 1

for i in range(1, len(l)):
    if l[i] != l[i - 1]:
        l[k] = l[i]
        k += 1

print(l[:k])  
