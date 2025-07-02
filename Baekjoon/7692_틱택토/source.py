def is_win(board, player):

    win_lines = [
        [0,1,2], [3,4,5], [6,7,8],  # 가로
        [0,3,6], [1,4,7], [2,5,8],  # 세로
        [0,4,8], [2,4,6]            # 대각선
    ]
    for line in win_lines:
        if all(board[i] == player for i in line):
            return True
    return False

while True:
    line = input()
    if line == "end":
        break

    board = list(line)
    x_count = board.count('X')
    o_count = board.count('O')

    x_win = is_win(board, 'X')
    o_win = is_win(board, 'O')

    if not (x_count == o_count or x_count == o_count + 1):
        print("invalid")
        continue

    valid = False
    if x_win and not o_win and x_count == o_count + 1:
        valid = True
    elif o_win and not x_win and x_count == o_count:
        valid = True
    elif not x_win and not o_win and x_count + o_count == 9:
        valid = True

    print("valid" if valid else "invalid")
