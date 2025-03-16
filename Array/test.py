
from collections import defaultdict
board = [["1","2",".",".","3",".",".",".","."],
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
def valid(num,i,j):
    if num==".":
        return True
    if num in rows[i] or num in cols[j] or num in boxes[(i//3,j//3)]:
        return False
    rows[i].add(num)
    cols[j].add(num)
    boxes[(i//3,j//3)].add(num)
    return True
for i in range(9):
    for j in range(9):
        if not valid(board[i][j],i,j):
            print(False)
            exit()
print(True)
