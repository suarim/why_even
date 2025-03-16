height = [2,2,2]
l=0
r=len(height)-1
res=0
maxres=0
while l<r:
    h=min(height[l],height[r])
    w=r-l
    res=h*w
    maxres=max(maxres,res)
    if height[l]<height[r]:
        l+=1
    else:
        r-=1
print(maxres)