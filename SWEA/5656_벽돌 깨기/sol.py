import sys
sys.stdin = open('input.txt')

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def gameStart(count, N, bricks):

    global min_count
    if count == N:
        brick_count = 0
        for i in range(height):
            for j in range(width):
                if bricks[i][j] != 0:
                    brick_count += 1
        if min_count > brick_count:
            min_count = brick_count
        return
    
    for i in range(width):
        new_bricks = [line[:] for line in bricks]
        idx = 0

        while idx < height and new_bricks[idx][i] == 0:
            idx += 1
        
        if idx != height:
            remove = brickOut(idx, i, new_bricks)
            brickSort(new_bricks)
        gameStart(count+1, N, new_bricks)


def brickOut(x, y, bricks):

    stack = []
    stack.append((x, y))
    count = 0
    
    while stack:
        
        x, y = stack.pop()
        splash = bricks[x][y]
        bricks[x][y] = 0

        if splash <= 1:
            continue
        
        for i in range(4):
            for j in range(1, splash):
                new_x = x + dx[i] * j
                new_y = y + dy[i] * j
                if new_x >=0 and new_x < height and new_y>=0 and new_y < width:
                    stack.append((new_x, new_y))

    
def brickSort(bricks):
    
    width = len(bricks[0])
    height = len(bricks)

    for i in range(width):
        brick_left = []

        for j in range(height):

            if bricks[j][i] != 0:
                brick_left.append(bricks[j][i])
            bricks[j][i] = 0
        
        for j in range(len(brick_left)):
            bricks[height-1-j][i] = brick_left.pop()



T = int(input())

for testcase in range(1, T+1):
    N, width, height = map(int, input().split())
    bricks = [list(map(int, input().split())) for _ in range(height)]

    min_count = width * height
    num_of_bricks = 0

                
    gameStart(0, N, bricks)

    print(f'#{testcase} {min_count}')