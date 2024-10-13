height = [1,8,6,2,5,4,8,3,7]
low=0
high=len(height)-1
maxarea=0
while low<high:
    minheight=min(height[low],height[high])
    width=high-low
    area=minheight*width
    print(area)
    maxarea=max(maxarea,area)
    if height[low]>height[high]:
        high-=1
    else:
        low+=1
print(maxarea)