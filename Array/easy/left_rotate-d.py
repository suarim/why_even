l=[1,2,3,4,5]
k=2
print(l[k:]+l[:k])
# O(n)

l.reverse()

l[:k+1]=reversed(l[:k+1])
l[k+1:]=reversed(l[k+1:])
print(l)