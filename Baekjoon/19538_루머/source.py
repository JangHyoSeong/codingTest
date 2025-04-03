import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
edges = [[] for _ in range(N + 1)]

for i in range(1, N + 1):
    edges[i] = list(map(int, sys.stdin.readline().rstrip().split()[:-1]))

M = int(sys.stdin.readline().rstrip())
start = list(map(int, sys.stdin.readline().rstrip().split()))

result = [-1] * (N + 1)
believe_count = [0] * (N + 1)

q = deque()
for person in start:
    result[person] = 0
    q.append(person)

while q:
    now = q.popleft()

    for next in edges[now]:
        if result[next] == -1:
            believe_count[next] += 1

            if believe_count[next] >= (len(edges[next]) + 1) // 2:
                result[next] = result[now] + 1
                q.append(next)

print(" ".join(map(str, result[1:])))