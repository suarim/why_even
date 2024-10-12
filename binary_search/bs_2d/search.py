mat=[[1,2,3],[4,5,6],[7,8,9]]
low=0
high=(len(mat)*len(mat[0]))-1
while low<=high:
    mid=(low+high)//2
    r=mid//len(mat[0])
    c=mid%len(mat[0])
    if mat[r][c]==11:
        print("Element found at index",r,c)
        break
    elif mat[r][c]>5:
        high=mid-1
    else:
        low=mid+1
else:
    print("Element not found")