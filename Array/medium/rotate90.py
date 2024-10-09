matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for i in range(len(matrix)):
    for j in range(i, len(matrix[0])):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
print(matrix)

for i in range(len(matrix)):
    matrix[i].reverse()

# for i in range(len(matrix)//2):
#     matrix[i],matrix[-i-1]=matrix[-i-1],matrix[i]
print(matrix)