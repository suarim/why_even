l=[1,1,0,1,1,1,1,0,1,1,1]
max_ones=0
k=0
for i in range(len(l)):
    if l[i]==0:
        k=0
    else:
        k+=1
    max_ones=max(max_ones,k)
print(max_ones)