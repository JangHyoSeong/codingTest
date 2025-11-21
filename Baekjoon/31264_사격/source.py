import sys

N, M, A = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

arr.sort()
left, right = 1, arr[N-1]

answer = A
while left <= right:
    mid = (left + right) // 2

    idx = 0
    now_shoot = mid
    now_score = 0
    for count in range(M):
        if now_shoot < arr[0]:
            break

        while idx + 1 < N and arr[idx + 1] <= now_shoot:
            idx += 1
        
        now_shoot += arr[idx]
        now_score += arr[idx]
    
    if now_score < A:
        left = mid + 1
    
    else:
        answer = mid
        right = mid - 1

print(answer)