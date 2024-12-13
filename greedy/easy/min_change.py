l=[1,2,5,10,20,50,100,500,1000]
v=71
for i in range(len(l)-1,-1,-1):
    if v>=l[i]:
        print(l[i])
        v=v-l[i]