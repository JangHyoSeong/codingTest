from collections import deque

N = int(input())
K = int(input())
apples = [list(map(int, input().split())) for _ in range(K)]

L = int(input())

# 방향전환은 딕셔너리로 입력받음
# 키 값은 방향전환 시간
# value값은 방향전환 방향
swap = {}
for _ in range(L):
    temp = list(input().split())
    swap[int(temp[0])] = temp[1]

# 시작 위치를 덱에 넣고 시작
q = deque([(1, 1)])

# 1초부터 시작
time = 1

# 방향전환을 위한 리스트. 순서대로 오른쪽, 아래, 왼쪽, 위
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 현재 방향. 오른쪽부터 시작
direction = 0

# 벽에 부딪히거나 자신을 만나면 False로 바뀌어 반복 종료
flag = True

while True:

    # head를 pop
    # 덱에 왼쪽(인덱스 0)은 머리, 오른쪽(인덱스 마지막)은 꼬리가 됨
    head = q.popleft()

    # 새 머리를 만들어 줌
    new_head = (head[0] + dx[direction], head[1] + dy[direction])
    
    # 벽에 부딪히면 반복 종료
    if new_head[0] < 1 or new_head[0] > N or new_head[1] < 1 or new_head[1] > N:
        break

    # 자신의 몸을 순회해서 부딪히는지 검사. 부딪히면 종료
    for i in range(len(q)):
        if new_head == q[i]:
            flag = False
            break
    
    if flag == False:
        break

    # 사과 리스트를 순회하여, 현재 새로운 머리 위치가 사과위치라면 사과를 먹음
    for i in range(K):
        if new_head[0] == apples[i][0] and new_head[1] == apples[i][1]:
            # 먹은 사과는 먹을수 없도록 위치 초기화
            apples[i] = [-1, -1]
            q.appendleft(head)
            q.appendleft(new_head)
            break
    # 사과를 먹지 못했다면 꼬리의 맨 뒤를 지워줌
    else:
        q.appendleft(head)
        q.appendleft(new_head)
        q.pop()

    # 방향전환
    # 방향전환은 먹고 난 뒤 해줘야함 <- 문제에서 제대로 안적어줘서 좀 헤맸다
    if swap.get(time) is not None:
        if swap[time] == 'L':
            direction = (direction-1) % 4
        else:
            direction = (direction+1) % 4
    time += 1

print(time)