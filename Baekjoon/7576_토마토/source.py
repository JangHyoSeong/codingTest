from collections import deque

width, height = map(int, input().split())

q1 = deque()
q2 = deque()
tomatoes = []
not_tomato_num = 0
for i in range(height):
    one_line = list(map(int, input().split()))
    tomatoes.append(one_line)
    for j in range(width):
        if one_line[j] == 1:
            q1.append([i, j])
        elif one_line[j] == 0:
            not_tomato_num += 1

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

day = 0

while q1 or q2:

    while q1:
        now_x, now_y = q1.popleft()

        for i in range(4):
            next_x = now_x + dx[i]
            next_y = now_y + dy[i]

            if 0 <= next_x < height and 0 <= next_y < width and tomatoes[next_x][next_y] == 0:
                q2.append([next_x, next_y])
                tomatoes[next_x][next_y] = 1
                not_tomato_num -= 1
    
    if q2 != deque():
        day += 1
    

    while q2:
        now_x, now_y = q2.popleft()

        for i in range(4):
            next_x = now_x + dx[i]
            next_y = now_y + dy[i]

            if 0 <= next_x < height and 0 <= next_y < width and tomatoes[next_x][next_y] == 0:
                q1.append([next_x, next_y])
                tomatoes[next_x][next_y] = 1
                not_tomato_num -= 1

    if q1 != deque():
        day += 1
if not_tomato_num:
    print(-1)
else:
    print(day)