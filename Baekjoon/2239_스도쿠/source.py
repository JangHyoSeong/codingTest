table = [list(map(int, input())) for _ in range(9)]

empty = [(i, j) for i in range(9) for j in range(9) if table[i][j] == 0]

def is_valid(x, y, num):
    for i in range(9):
        if table[x][i] == num or table[i][y] == num:
            return False
    
    box_x = (x // 3) * 3
    box_y = (y //3 ) * 3

    for i in range(3):
        for j in range(3):
            if table[box_x + i][box_y + j] == num:
                return False
    
    return True

def solve(index):
    if index == len(empty):
        for row in table:
            print("".join(map(str, row)))

        exit()
    
    x, y = empty[index]
    for num in range(1, 10):
        if is_valid(x, y, num):
            table[x][y] = num
            solve(index + 1)
            table[x][y] = 0
    
solve(0)