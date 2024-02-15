'''
굳이 루프를 돌 필요 없이, 몫과 나머지를 통해 계산가능
위아래 이동과 오른쪽왼쪽 이동을 따로 생각해도 됨
'''


w, h = map(int, input().split())
x, y = map(int, input().split())

t = int(input())

# 마지막 순간에 오른쪽 왼쪽으로 이동하는 방향을 구함
# 1이면 왼쪽으로 이동중(감소중)
# 0이면 오른쪽으로 이동중(증가중)
right_left = ((t + x) // w) % 2

# 마지막 순간에 위쪽 아래쪽으로 이동하는 방향을 구함
# 1이면 아래로 이동중(감소중)
# 0이면 위로 이동중(증가중)
up_down = ((t + y) // h) % 2

# 마지막 순간에 움직일 거리
right_left_go = (t + x) % w
up_down_go = (t + y) % h

# 1이라면 (왼쪽으로 이동중이라면)
if right_left:
    now_x = w - right_left_go

# 0이라면(오른쪽으로 이동중이라면)
else:
    now_x = right_left_go

# 1이라면 (아래쪽으로 이동중이라면)
if up_down:
    now_y = h - up_down_go

# 0이라면 (위로 이동중이라면)
else:
    now_y = up_down_go

print(now_x, now_y)