import sys
input = sys.stdin.readline

N, C = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr.sort()

start = 1
end = arr[-1] - arr[0]
result = 0

while start <= end:
    mid = (start + end) // 2
    count = 1
    prev_house = arr[0]

    for i in range(1, N):
        if arr[i] - prev_house >= mid:
            count += 1
            prev_house = arr[i]

    if count >= C:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)