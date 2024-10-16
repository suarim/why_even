mat=[[1,1,1],[1,0,1],[1,1,1]]
l=[]
for i in range(len(mat)):
    for j in range(len(mat[0])):
        if mat[i][j]==0:
            l.append([i,j])
for i,j in l:
    for k in range(len(mat)):
        mat[k][j]=0
    for k in range(len(mat[0])):
        mat[i][k]=0
print(mat)