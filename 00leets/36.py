from collections import defaultdict
board=[["1","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,["5","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
rows=defaultdict(set)
cols=defaultdict(set)
box=defaultdict(set)
for i in range(9):
    for j in range(9):
        if board[i][j]==".":
            continue
        if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in box[(i//3,j//3)]:
            print(False)
            exit()
        rows[i].add(board[i][j])
        cols[j].add(board[i][j])
        box[(i//3,j//3)].add(board[i][j])
print(True)
