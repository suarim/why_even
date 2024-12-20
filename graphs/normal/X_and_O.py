def soln(board):
    
    def dfs(board,i,j,visited):
        visited[i][j]=1
        directions=[(0,1),(0,-1),(1,0),(-1,0)]  
        for x,y in directions:
            dx,dy=i+x,j+y
            if 0<=dx<len(board) and 0<=dy<len(board[0]) and board[dx][dy]=='O' and visited[dx][dy]==0:
                dfs(board,dx,dy,visited)
        
    rows=len(board)
    cols=len(board[0])
    visited=[[0]*cols for i in range(rows)]
    for i in range(cols):
        if board[0][i]=='O' and visited[0][i]==0:
            dfs(board,0,i,visited)
        if board[rows-1][i]=='O' and visited[rows-1][i]==0:
            dfs(board,rows-1,i,visited)
    for i in range(rows):
        if board[i][0]=='O' and visited[i][0]==0:
            dfs(board,i,0,visited)
        if board[i][cols-1]=='O' and visited[i][cols-1]==0:
            dfs(board,i,cols-1,visited)
    for i in range(rows):
        for j in range(cols):
            if visited[i][j]==0:
                board[i][j]='X'
    return board
board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
print(soln(board))