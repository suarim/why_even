l=[2,3,4,6,7,8,11]
h={}
for i,n in enumerate(l):
    h[n]=i
print(h)
target=9
for i in range(len(l)):
    if target-l[i] in h:
        print([i,h[target-l[i]]])
        break