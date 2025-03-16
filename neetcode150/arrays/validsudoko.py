from collections import defaultdict
board=[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

rows=defaultdict(set)
cols=defaultdict(set)
boxes=defaultdict(set)
def isvalid(board,i,j):
    if board[i][j]==".":
        return True
    if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in boxes[(i//3,j//3)]:
        return False
    rows[i].add(board[i][j])
    cols[j].add(board[i][j])
    boxes[(i//3,j//3)].add(board[i][j])
    return True
for i in range(9):
    for j in range(9):
        if not isvalid(board,i,j):
            print(False)
            exit()
print(True)