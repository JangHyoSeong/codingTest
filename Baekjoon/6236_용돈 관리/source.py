N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]

left, right = max(arr), sum(arr)

while left <= right:
    mid = (left+right) // 2
    count, total = 1, 0

    for i in range(N):
        if total + arr[i] > mid:
            count += 1
            total = 0
        total += arr[i]


    if count <= M:
        answer = mid
        right = mid - 1

    else:
        left = mid + 1

print(answer)