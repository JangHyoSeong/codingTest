from collections import deque

T = int(input())

def find_start():
    # 시작 지점을 찾는 함수
    for i in range(N):
        for j in range(M):
            if table[i][j] == '@':
                table[i][j] = '.'
                return (i, j)

for testcase in range(T):
    # 입력받기
    M, N = map(int, input().split())
    table = [list(input()) for _ in range(N)]

    # 방문 여부를 처리할 리스트
    visited = [[False] * M for _ in range(N)]

    # 현재 상근이가 있을 수 있는 좌표들을 담은 deque(큐)
    now_q = deque()
    # 시작 위치를 저장
    start = find_start()
    # 시작 위치 방문 처리
    visited[start[0]][start[1]] = True
    # 시작 위치를 삽입후 시작
    now_q.append(start)

    # 탈출여부, 불가능 여부를 변수에 저장
    escape = False
    impossible = False

    # 상하좌우 탐색을 위한 리스트
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    # 몇초가 지났는지 저장할 변수
    count = 0

    # 현재 불의 위치를 저장할 리스트
    now_fire = []
    # 현재 불의 위치를 리스트에 저장
    for i in range(N):
        for j in range(M):
            if table[i][j] == '*':
                now_fire.append((i, j))

    # 탈출했거나, 탈출 못하는 경우 반복 종료
    while not escape and not impossible:

        # 옮겨진 불의 위치를 저장할 리스트
        next_fire = []
        
        # 불을 모두 옮겨주고, 다음 불의 위치를 저장
        for fire in now_fire:
            for i in range(4):
                nx = fire[0] + dx[i]
                ny = fire[1] + dy[i]

                if 0 <= nx < N and 0 <= ny < M:
                    if table[nx][ny] == '.':
                        table[nx][ny] = '*'
                        next_fire.append((nx, ny))
        
        now_fire = next_fire

        # 다음 상근이가 있을 수 있는 위치를 저장할 deque
        next_queue = deque()

        # 현재 상근이가 있을 수 있는 위치를 BFS로 순회하면서 다음 위치로 삽입
        while now_q:
            now = now_q.popleft()

            for i in range(4):
                nx = now[0] + dx[i]
                ny = now[1] + dy[i]

                # 만약 인덱스를 벗어나지 않는다면
                if 0 <= nx < N and 0 <= ny < M:
                    # 아직 방문하지 않았고 빈공간이라면
                    if not visited[nx][ny] and table[nx][ny] == '.':
                        # 다음 상근이의 위치 큐에 삽입
                        next_queue.append((nx, ny))
                        # 방문처리
                        visited[nx][ny] = True
                # 인덱스를 벗어났다면 == 상근이가 탈출했다면
                else:
                    # 탈출을 True로 바꿈
                    escape = True

        # 이동할 수 있는 위치가 없다면 impossible을 true로 바꿈
        if next_queue == deque():
            impossible = True
        else:
            # 이동할 수 있는 위치가 있다면 새롭게 now_q를 갱신
            now_q = next_queue

        # 시간을 더해줌
        count += 1
        
    # 탈출 가능하다면 시간출력, 아니라면 IMPOSSIBLE
    if escape == True:
        print(count)
    else:
        print('IMPOSSIBLE')