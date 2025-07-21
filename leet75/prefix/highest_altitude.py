gain = [-5,1,5,0,-7]
l=[0]+gain
for i in range(0,len(gain)):
    l[i+1]=gain[i]+l[i]
print(max(l))