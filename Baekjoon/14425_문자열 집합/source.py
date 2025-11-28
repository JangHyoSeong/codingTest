import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
strings = set(sys.stdin.readline().rstrip() for _ in range(N))

count = 0
for _ in range(M):
    query = sys.stdin.readline().rstrip()

    if query in strings:
        count += 1

print(count)