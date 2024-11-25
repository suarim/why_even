matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 34
m=len(matrix)
n=len(matrix[0])
low=0
high=m*n-1
while low<=high:
    mid=(low+high)//2
    rows=mid//n
    cols=mid%n
    if matrix[rows][cols]==target:
        print(True)
        exit()
    elif matrix[rows][cols]<target:
        low=mid+1
    else:
        high=mid-1
print(False)