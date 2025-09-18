import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split())
arr = [0] + list(map(int, sys.stdin.readline().rstrip().split()))

edges = [[] for _ in range(N+1)]
for i in range(2, N + 1):
    edges[arr[i]].append(i)


score = [0] * (N + 1)
for _ in range(M):
    i, w = map(int, sys.stdin.readline().rstrip().split())
    score[i] += w

q = deque([1])
while q:
    now_node = q.popleft()

    for next_node in edges[now_node]:
        q.append(next_node)
        score[next_node] += score[now_node]

print(" ".join(map(str, score[1:])))