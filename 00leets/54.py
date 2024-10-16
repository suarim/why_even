matrix = [[1,2,3],[4,5,6],[7,8,9]]
top=0
bottom=len(matrix)-1
left=0
right=len(matrix[0])-1
result=[]
d=0
while top<=bottom and left<=right:
    if d==0:
        for i in range(left,right+1):
            result.append(matrix[top][i])
        top+=1
    elif d==1:
        for i in range(top,bottom+1):
            result.append(matrix[i][right])
        right-=1
    elif d==2:
        for i in range(right,left-1,-1):
            result.append(matrix[bottom][i])
        bottom-=1
    elif d==3:
        for i in range(bottom,top-1,-1):
            result.append(matrix[i][left])
        left+=1
    d=(d+1)%4
print(result)