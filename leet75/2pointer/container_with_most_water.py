height = [1,8,6,2,5,4,8,3,7]
l=0
r=len(height)-1
ma=-9999
while l<r:
    h=min(height[l],height[r])
    w=r-l
    a=h*w
    ma=max(a,ma)
    if height[l]>height[r]:
        r-=1
    else:
        l+=1
print(ma)