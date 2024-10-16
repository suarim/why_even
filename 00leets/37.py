board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]

def empty():
    for i in range(9):
        for j in range(9):
            if board[i][j]==".":
                return (i,j)
    return None
def valid(num,r,c):
    if num in board[r]:
        return False
    for i in range(9):
        if num==board[i][c]:
            return False
    box_row = (r // 3) * 3
    box_col = (c // 3) * 3
    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):
            if board[i][j] == num:
                return False
    return True
def solve():
    emp=empty()
    if not emp:
        return True
    r,c=emp
    for i in range(1,10):
        if valid(str(i),r,c):
            board[r][c]=str(i)
            if solve():
                return True
            board[r][c]="."
    return False
print(solve())
print(board)