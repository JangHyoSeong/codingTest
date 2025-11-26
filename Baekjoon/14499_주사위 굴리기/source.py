N, M, x, y, K = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]
moves = list(map(int, input().split()))

dice = [0] * 7
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

for cmd in moves:
    nx = x + dx[cmd]
    ny = y + dy[cmd]

    if not (0 <= nx < N and 0 <= ny < M):
        continue

    x, y = nx, ny
    t = dice[:]
    if cmd == 1: # 동
        dice[1], dice[3], dice[6], dice[4] = t[4], t[1], t[3], t[6]

    elif cmd == 2: # 서
        dice[1], dice[4], dice[6], dice[3] = t[3], t[1], t[4], t[6]

    elif cmd == 3: # 북
        dice[1], dice[2], dice[6], dice[5] = t[5], t[1], t[2], t[6]

    else: # 남
        dice[1], dice[5], dice[6], dice[2] = t[2], t[1], t[5], t[6]
    
    if table[x][y] == 0:
        table[x][y] = dice[6]
    
    else:
        dice[6] = table[x][y]
        table[x][y] = 0

    print(dice[1])