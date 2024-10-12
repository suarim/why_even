mat=[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
row=0
col=len(mat[0])-1
target=5
while row<len(mat) and col>=0:
    if mat[row][col]==target:
        print("Element found at index",row,col)
        break
    elif mat[row][col]>target:
        col-=1
    else:
        row+=1
else:
    print("Element not found")