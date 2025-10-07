import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
jewels = [int(sys.stdin.readline().rstrip()) for _ in range(M)]

left, right = 1, max(jewels)
answer = right

while left <= right:
    mid = (left + right) // 2
    total = 0

    for jewel in jewels:
        total += (jewel + mid - 1) // mid
        if total > N:
            break
    
    if total <= N:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)