import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
arr = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

arr.sort()
min_gap = float('inf')

front, rear = 0, 0

while front < N and rear < N:
    gap = arr[rear] - arr[front]

    if gap < M:
        rear += 1
    else:
        min_gap = min(min_gap, gap)
        front += 1

print(min_gap)