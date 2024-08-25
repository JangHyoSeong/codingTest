R, C, M = map(int, input().split())

if M == 0:
    print(0)
    exit()

# 상어의 위치 및 정보를 담을 딕셔너리
sharks = {}

# 초기 상어 위치 설정
for i in range(M):
    r, c, s, d, z = map(int, input().split())
    sharks[(r, c)] = (s, d, z)

result = 0

# 방향 설정 (1: 위, 2: 아래, 3: 오른쪽, 4: 왼쪽)
directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

# 이동 함수
def move_shark(r, c, s, d):
    if d == 1 or d == 2:
        s = s % (2 * (R - 1))  # 주기 활용
    else:
        s = s % (2 * (C - 1))

    for _ in range(s):
        nr, nc = r + directions[d - 1][0], c + directions[d - 1][1]
        if nr < 1 or nr > R or nc < 1 or nc > C:  # 경계를 넘으면 방향 반대
            d = d - 1 if d % 2 == 0 else d + 1
            nr, nc = r + directions[d - 1][0], c + directions[d - 1][1]
        r, c = nr, nc

    return r, c, d

for x in range(1, C + 1):
    # 1. 낚시왕이 있는 열에서 가장 가까운 상어 잡기
    for depth in range(1, R + 1):
        if (depth, x) in sharks:
            result += sharks[(depth, x)][2]  # 상어 크기 더하기
            del sharks[(depth, x)]  # 상어 제거
            break

    # 2. 상어 이동
    new_sharks = {}

    for (r, c), (s, d, z) in sharks.items():
        nr, nc, nd = move_shark(r, c, s, d)

        # 이동 후 위치에 다른 상어가 있으면 크기 비교
        if (nr, nc) not in new_sharks or new_sharks[(nr, nc)][2] < z:
            new_sharks[(nr, nc)] = (s, nd, z)

    sharks = new_sharks

print(result)
