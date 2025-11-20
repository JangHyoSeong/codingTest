N, M = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]

max_sum = int(-21e8)
for top in range(N):
    temp = [0] * M

    for bottom in range(top, N):
        
        for col in range(M):
            temp[col] += table[bottom][col]

        current_max = temp[0]
        max_ending_here = temp[0]

        for i in range(1, M):
            max_ending_here = max(temp[i], max_ending_here + temp[i])
            current_max = max(current_max, max_ending_here)
        
        max_sum = max(max_sum, current_max)

print(max_sum)