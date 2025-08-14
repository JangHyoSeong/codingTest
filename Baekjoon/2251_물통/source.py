from collections import deque

A, B, C = map(int, input().split())
q = deque([(0, 0)])

visited = [[False] * (B + 1) for _ in range(A + 1)]
visited[0][0] = True
result = set()

def pour(x, y, cap_y):
    amount = min(x, cap_y - y)
    return x - amount, y + amount

while q:
    a, b= q.popleft()
    c = C - a - b

    if a == 0:
        result.add(c)
    
    # A → B
    na, nb = pour(a, b, B)
    if not visited[na][nb]:
        visited[na][nb] = True
        q.append((na, nb))

    # A → C
    na, nc = pour(a, c, C)
    if not visited[na][b]:
        visited[na][b] = True
        q.append((na, b))

    # B → A
    nb, na = pour(b, a, A)
    if not visited[na][nb]:
        visited[na][nb] = True
        q.append((na, nb))

    # B → C
    nb, nc = pour(b, c, C)
    if not visited[a][nb]:
        visited[a][nb] = True
        q.append((a, nb))

    # C → A
    nc, na = pour(c, a, A)
    if not visited[na][b]:
        visited[na][b] = True
        q.append((na, b))

    # C → B
    nc, nb = pour(c, b, B)
    if not visited[a][nb]:
        visited[a][nb] = True
        q.append((a, nb))

print(*sorted(result))