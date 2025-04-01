import sys

N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

left, right = 0, N-1

max_status = 0

while left < right:
    gap = right - left - 1
    max_status = max(max_status, min(arr[left], arr[right]) * gap)

    if arr[left] < arr[right]:
        left += 1
    else:
        right -= 1

print(max_status)