import sys

N, K = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

left, right = 0, max(arr)
answer = right

while left <= right:
    mid = (left + right) // 2

    total = 0
    for number in arr:
        if number > mid:
            total += number - mid
        
        if total > K:
            break
    
    if total <= K:
        answer = mid
        right = mid - 1
    
    else:
        left = mid + 1

print(answer)