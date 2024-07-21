from sys import stdin

N, M = map(int, stdin.readline().strip().split())
arr = [list(map(int, stdin.readline().strip().split())) for _ in range(M)]

result = list(range(N+1))

for a, b in reversed(arr):
    result[a] = result[b]

result = result[1:]
print(" ".join(map(str, result)))