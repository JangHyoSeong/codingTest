import sys
sys.stdin = open('input.txt')

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

T = int(input())

for testcase in range(1, T+1):
    N = int(input())
    board = []
    worm_hole = []
    for i in range(N):
        one_line = list(map(int, input().split()))
        board.append(one_line)
        for j in range(N):
            if one_line[j] >= 6:
                worm_hole.append((one_line[j],i,j))


    direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    count_list = []

    for dir in range(4):
        for i in range(N):
            for j in range(N):
                
                if board[i][j] != 0:
                    continue
                x, y = i, j
                count = 0

                while True:
                    x += direction[dir][0]
                    y += direction[dir][1]

                    if x < 0 or x >= N or y < 0 or y >= N:

                        dir = (dir+2)%4
                        x += direction[dir][0]
                        y += direction[dir][1]
                        if x == i and y == j:
                            break
                        count += 1

                    elif board[x][y] == 5:
                        dir = (dir+2)%4
                        x += direction[dir][0]
                        y += direction[dir][1]
                        if x == i and y == j:
                            break
                        count += 1
                        
                    now_position = board[x][y]

                    if x == i and y == j:
                        break

                    if now_position == -1:
                        break

                    if now_position == 0:
                        continue
                    
                    if now_position >= 6:
                        for var in worm_hole:
                            if now_position == var[0] and x != var[1] and y != var[2]:
                                x = var[1]
                                y = var[2]
                                break
                        continue

                    
                    if now_position == 1:
                        
                        if dir == UP or dir == RIGHT:
                            dir = (dir+2)%4
                        elif dir == DOWN:
                            dir = RIGHT
                        elif dir == LEFT:
                            dir = UP
                    
                    elif now_position == 2:
                        
                        if dir == DOWN or dir == RIGHT:
                            dir = (dir+2)%4
                        elif dir == UP:
                            dir = RIGHT
                        elif dir == LEFT:
                            dir = DOWN

                    elif now_position == 3:
                        
                        if dir == DOWN or dir == LEFT:
                            dir = (dir+2)%4
                        elif dir == UP:
                            dir = LEFT
                        elif dir == RIGHT:
                            dir = DOWN

                    elif now_position == 4:
                        
                        if dir == UP or dir == LEFT:
                            dir = (dir+2)%4
                        elif dir == DOWN:
                            dir = LEFT
                        elif dir == RIGHT:
                            dir = UP

                    count += 1
                    
                if count not in count_list:    
                    count_list.append(count)
    print(count_list)
    print(f'#{testcase} {max(count_list)}')