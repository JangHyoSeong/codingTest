from itertools import combinations

N = int(input())
table = [list(input().split()) for _ in range(N)]

# 빈공간의 위치를 담을 리스트
obstacle = []
# 학생의 위치를 담을 리스트
students = []

# 테이블을 순회하면서 학생, 빈공간의 위치를 리스트에 삽입
for i in range(N):
    for j in range(N):
        if table[i][j] == 'X':
            obstacle.append([i, j])
        elif table[i][j] == 'S':
            students.append([i, j])
        
# 모든 빈공간을 길이가 3인 조합으로 만들어줌
# 이 조합 하나하나가 장애물을 배치할 케이스
obs_comb = list(combinations(obstacle, 3))

# 상하좌우 이동을 위한 리스트 선언
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 종료 조건을 만나면 return하기 위해 함수로 선언
def f(students):

    # 모든 학생들의 위치를 확인하면서
    for student in students:
        x, y = student
        
        # 동서남북으로 인덱스의 범위 안까지 이동
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            while 0 <= nx < N and 0 <= ny < N:
                
                # 도중에 장애물을 만난다면 이쪽 방향으로의 탐색을 종료
                if table[nx][ny] == 'O':
                    break
                # 도중에 선생님을 만난다면 False를 return
                elif table[nx][ny] == 'T':
                    return False
                
                # 한쪽 방향으로 계속 이동(인덱스를 벗어날 때까지)
                nx += dx[i]
                ny += dy[i]
                
    # return False를 한번도 하지 않고 루프를 탈출했다면 True를 return
    return True

# 모든 생성된 조합에 대해서 확인
for case in obs_comb:
    
    # 현재 케이스의 장애물 배치
    for x, y in case:
        table[x][y] = 'O'
    
    # 현재 케이스에서 정답 여부 확인
    flag = f(students)

    # 만약 True라면 다른 케이스는 검사하지 않아도 됨
    # break
    if flag:
        break
    
    # 현재 케이스의 장애물을 원래대로 되돌림
    for x, y in case:
        table[x][y] = 'X'

# 정답 출력
if flag:
    print('YES')
else:
    print('NO')