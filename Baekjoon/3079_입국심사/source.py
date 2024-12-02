N, M = map(int, input().split())
times = [int(input()) for _ in range(N)]

min_time, max_time = 0, max(times) * M
while min_time <= max_time:
    mid = (min_time + max_time) // 2
    total = 0

    for time in times:
        total += mid // time

    if total >= M:
        max_time = mid - 1
    
    else:
        min_time = mid + 1

print(min_time)