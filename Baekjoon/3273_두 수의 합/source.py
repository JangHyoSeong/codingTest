import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline())

arr.sort()
left, right = 0, N - 1
count = 0

while left < right:
    total = arr[left] + arr[right]
    if total == x:
        count += 1
        left += 1
        right -= 1
    elif total < x:
        left += 1
    else:
        right -= 1

print(count)