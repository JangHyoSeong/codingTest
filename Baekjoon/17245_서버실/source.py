import sys

N = int(sys.stdin.readline().rstrip())
table = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

total = sum(sum(row) for row in table)
half = (total + 1) // 2

left, right = 0, max(max(row) for row in table)
answer = right

while left <= right:
    mid = (left + right) // 2

    count = 0

    for i in range(N):
        for j in range(N):
            count += min(table[i][j], mid)
    
    if count >= half:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)