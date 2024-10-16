height = [0,1,0,2,1,0,1,3,2,1,2,1]
lwall=0
rwall=0
ml=[0]*len(height)
mr=[0]*len(height)
for i in range(len(height)):
    j=-i-1
    ml[i]=lwall
    mr[j]=rwall
    lwall=max(lwall,height[i])
    rwall=max(rwall,height[j])

sum=0
for i in range(len(height)):
    sum+=max(0,min(ml[i],mr[i])-height[i])
print(sum)