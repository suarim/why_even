l=[1,2,3,4,5,6]
k=2
print(l[k:]+l[:k])

l.reverse()
z=len(l)-k
l[:z]=reversed(l[:z])
l[z:]=reversed(l[z:])
print(l)