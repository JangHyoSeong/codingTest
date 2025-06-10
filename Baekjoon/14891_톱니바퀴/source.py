from collections import deque

gears = [deque(map(int, input())) for _ in range(4)]
K = int(input())
moves = [list(map(int, input().split())) for _ in range(K)]

def rotate(gear: deque, direction):
    if direction == 1:
        gear.appendleft(gear.pop())
    else:
        gear.append(gear.popleft())
    
for gear_num, direction in moves:
    gear_num -= 1
    rotate_dirs = [0] * 4
    rotate_dirs[gear_num] = direction

    for i in range(gear_num-1, -1, -1):
        if gears[i][2] != gears[i+1][6]:
            rotate_dirs[i] = -rotate_dirs[i+1]
        else:
            break
    
    for i in range(gear_num + 1, 4):
        if gears[i-1][2] != gears[i][6]:
            rotate_dirs[i] = -rotate_dirs[i-1]
        else:
            break
    
    for i in range(4):
        if rotate_dirs[i] != 0:
            rotate(gears[i], rotate_dirs[i])

score = 0
for i in range(4):
    if gears[i][0] == 1:
        score += (1 << i)
print(score)