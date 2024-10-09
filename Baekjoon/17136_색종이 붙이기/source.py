def can_attach(x, y, size):
    # 주어진 위치 (x, y)에서 크기 size의 색종이를 붙일 수 있는지 확인
    if x + size > 10 or y + size > 10:
        return False
    for i in range(size):
        for j in range(size):
            if table[x + i][y + j] != 1 or visited[x + i][y + j]:
                return False
    return True

def attach(x, y, size, flag):
    # 주어진 위치 (x, y)에 크기 size의 색종이를 붙이거나 떼기 (flag: True 붙이기, False 떼기)
    for i in range(size):
        for j in range(size):
            visited[x + i][y + j] = flag

def dfs(cnt):
    global min_count
    if cnt >= min_count:
        return
    # 모든 1이 덮였는지 확인
    if all(all(visited[i][j] or table[i][j] == 0 for j in range(10)) for i in range(10)):
        min_count = min(min_count, cnt)
        return

    for i in range(10):
        for j in range(10):
            if table[i][j] == 1 and not visited[i][j]:
                for size in range(5, 0, -1):
                    if used[size] < 5 and can_attach(i, j, size):
                        attach(i, j, size, True)
                        used[size] += 1
                        dfs(cnt + 1)
                        attach(i, j, size, False)
                        used[size] -= 1
                return

table = [list(map(int, input().split())) for _ in range(10)]
visited = [[False] * 10 for _ in range(10)]
used = [0] * 6
min_count = float('inf')

dfs(0)
print(-1 if min_count == float('inf') else min_count)