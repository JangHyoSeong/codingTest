N, M, B = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]

min_height = 0
max_height = 256

min_time = 21e8
optimal_height = 0

for h in range(min_height, max_height+1):
    remove_blocks = 0
    add_blocks = 0

    for i in range(N):
        for j in range(M):
            if table[i][j] > h:
                remove_blocks += table[i][j] - h
            else:
                add_blocks += h - table[i][j]

    if remove_blocks + B >= add_blocks:
        time = remove_blocks * 2 + add_blocks
        if time < min_time or (time == min_time and h > optimal_height):
            min_time = time
            optimal_height = h

print(min_time, optimal_height)