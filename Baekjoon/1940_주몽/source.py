import sys

N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

arr.sort()
front, rear = 0, N-1

count = 0
while front < rear:
    temp_sum = arr[front] + arr[rear]

    if temp_sum == M:
        count += 1
        front += 1
        rear -= 1
    
    elif temp_sum < M:
        front += 1
    
    else:
        rear -= 1

print(count)    