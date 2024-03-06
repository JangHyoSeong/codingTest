N = int(input())

times = [list(map(int, input().split())) for _ in range(N)]

times.sort()
count = 1
start, end = times[0][0], times[0][1]
for i in range(1, N):
    if times[i][1] < end:
        start, end = times[i][0], times[i][1]
    elif end <= times[i][0]:
        count += 1
        start, end = times[i][0], times[i][1]

print(count)