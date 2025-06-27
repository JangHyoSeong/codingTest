from collections import deque

N = int(input())
arr = list(map(int, input().split()))

q = deque((i + 1, move) for i, move in enumerate(arr))
result = []

while q:
    idx, move = q.popleft()
    result.append(idx)

    if not q:
        break

    if move > 0:
        q.rotate(-(move - 1))
    else:
        q.rotate(-move)

print(" ".join(map(str, result)))    