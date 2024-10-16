matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
for i in range(len(matrix)//2):
    matrix[i],matrix[-1-i]=matrix[-1-i],matrix[i]
print(matrix)
for i in range(len(matrix)):
    for j in range(i,len(matrix)):
        matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
print(matrix)