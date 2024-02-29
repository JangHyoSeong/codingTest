count = 0

def queen(line, n, board):
    global count
    
    if line == n:
        count += 1
        return
        
    for i in range(n):
        if is_safe(line, i, n, board):
            board[line][i] = 1
            queen(line + 1, n, board)
            board[line][i] = 0
            
def is_safe(x, y, n, board):
    
    for i in range(x):
        if board[i][y] == 1:
            return False
    
    
    i = x - 1
    j = y - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    
   
    i = x - 1
    j = y + 1
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1
    
    return True

def solution(n):
    board = [[0] * n for _ in range(n)]
    queen(0, n, board)
    return count