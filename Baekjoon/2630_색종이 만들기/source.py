N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]

white, blue = 0, 0

def count_color(x, y, size):
    global white, blue

    color = table[x][y]
    same = True

    for i in range(x, x + size):
        for j in range(y, y + size):
            if table[i][j] != color:
                same = False
                break
        
        if not same:
            break
    
    if same:
        if color == 0:
            white += 1
        
        else:
            blue += 1
    
    else:
        half = size // 2
        count_color(x, y, half)
        count_color(x, y + half, half)
        count_color(x + half, y, half)
        count_color(x + half, y + half, half)

count_color(0, 0, N)
print(white)
print(blue)