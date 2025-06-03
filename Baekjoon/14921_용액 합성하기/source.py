import sys

N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

front, rear = 0, N-1
min_gap = int(21e8)
while front < rear:
    temp_gap = arr[rear] + arr[front]

    if abs(min_gap) > abs(temp_gap):
        min_gap = temp_gap
        
    if temp_gap == 0:
        min_gap = 0
        break

    elif temp_gap > 0:
        rear -= 1

    else:
        front += 1

print(min_gap)