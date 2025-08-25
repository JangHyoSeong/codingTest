import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
arr = []
for class_id in range(N):
    team = list(map(int, sys.stdin.readline().rstrip().split()))

    for value in team:
        arr.append((value, class_id))
    
arr.sort(key=lambda x: x[0])

count = [0] * N
covered = 0
answer = int(10e9)

left = 0
for right in range(len(arr)):
    value_right, class_right = arr[right]

    if count[class_right] == 0:
        covered += 1
    
    count[class_right] += 1

    while covered == N:
        value_left, class_left = arr[left]
        answer = min(answer, value_right - value_left)

        count[class_left] -= 1
        if count[class_left] == 0:
            covered -= 1
        
        left += 1

if N == 1:
    print(0)
else:
    print(answer)