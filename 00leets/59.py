n = 3
arr=[[0]*n for i in range(n)]
num=1
dir=0
left=0
top=0
right=n-1
bottom=n-1
while left<=right and top<=bottom:
    if dir==0:
        for i in range(left,right+1):
            arr[top][i]=num
            num+=1
        top+=1
    elif dir==1:
        for i in range(top,bottom+1):
            arr[i][right]=num
            num+=1
        right-=1
    elif dir==2:
        for i in range(right,left-1,-1):
            arr[bottom][i]=num
            num+=1
        bottom-=1
    elif dir==3:
        for i in range(bottom,top-1,-1):
            arr[i][left]=num
            num+=1
        left+=1
    dir=(dir+1)%4
print(arr)