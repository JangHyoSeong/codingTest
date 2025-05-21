import sys

N, M, H = map(int, sys.stdin.readline().rstrip().split())
ladder = [[False] * (N+1) for _ in range(H+1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    ladder[a][b] = True

def check():
    for i in range(1, N+1):
        pos = i

        for j in range(1, H+1):
            if ladder[j][pos]:
                pos += 1
            elif pos > 1 and ladder[j][pos - 1]:
                pos -= 1
        
        if pos != i:
            return False
    return True

result = 4

def dfs(count, x, y):
    global result

    if count >= result:
        return

    if check():
        if result > count:
            result = count
        return

    for i in range(x, H+1):
        k = y if i == x else 1
        for j in range(k, N):
            if not ladder[i][j] and not ladder[i][j-1] and not ladder[i][j+1]:
                ladder[i][j] = True
                dfs(count + 1, i, j)
                ladder[i][j] = False

dfs(0, 1, 1)
print(result if result <= 3 else -1)