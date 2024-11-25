l=[1,2,3,4,5]
k=2
print(l[k:]+l[:k])
# O(n)

l.reverse()
print(l)
z=len(l)-k
l[:z]=reversed(l[:z])
print(l)
l[z:]=reversed(l[z:])
print(l)