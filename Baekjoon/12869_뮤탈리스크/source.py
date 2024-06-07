from collections import deque

def min_attacks(hp):
    # 최대 체력 범위 설정
    MAX_HP = 60

    # 세 SCV의 초기 체력을 맞춰 0으로 확장
    while len(hp) < 3:
        hp.append(0)

    # dp 배열로 각 체력 상태에서의 최소 공격 횟수를 저장
    dp = [[[float('inf')] * (MAX_HP + 1) for _ in range(MAX_HP + 1)] for __ in range(MAX_HP + 1)]
    dp[hp[0]][hp[1]][hp[2]] = 0

    queue = deque([(hp[0], hp[1], hp[2])])

    while queue:
        a, b, c = queue.popleft()
        current_attacks = dp[a][b][c]

        # 가능한 공격 조합들
        attacks = [
            (9, 3, 1),
            (9, 1, 3),
            (3, 9, 1),
            (3, 1, 9),
            (1, 9, 3),
            (1, 3, 9)
        ]

        for da, db, dc in attacks:
            na, nb, nc = max(0, a - da), max(0, b - db), max(0, c - dc)
            if dp[na][nb][nc] > current_attacks + 1:
                dp[na][nb][nc] = current_attacks + 1
                queue.append((na, nb, nc))

    return dp[0][0][0]

# 입력
n = int(input())  # SCV의 수 (1 이상 3 이하)
hp = list(map(int, input().split()))  # 각 SCV의 초기 체력

# 결과 출력
print(min_attacks(hp))
