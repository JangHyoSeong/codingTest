N = int(input())
arr = list(map(int, input().split()))
total = int(input())

start, end = 0, max(arr)

while start <= end:
    mid = (start + end) // 2
    result = 0

    for num in arr:
        result += min(num, mid)

    if result <= total:
        start = mid + 1
    else:
        end = mid - 1

print(end)