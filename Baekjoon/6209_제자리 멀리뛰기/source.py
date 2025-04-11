import sys

d, n, m = map(int, sys.stdin.readline().rstrip().split())
rocks = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

rocks.sort()
rocks = [0] + rocks + [d]

left, right = 1, d
result = 0

while left <= right:
    mid = (left + right) // 2
    prev = 0
    remove_count = 0

    for i in range(1, len(rocks)):
        if rocks[i] - rocks[prev] < mid:
            remove_count += 1
        else:
            prev = i

    if remove_count > m:
        right = mid - 1
    else:
        result = mid
        left = mid + 1

print(result)