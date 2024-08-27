from math import log2

m = int(input())
arr = [0] + list(map(int, input().split()))
Q = int(input())
queries = [list(map(int, input().split())) for _ in range(Q)]


LOG_K = int(log2(500000))
table = [[0] * (m+1) for _ in range(LOG_K + 1)]

for i in range(1, m+1):
    table[0][i] = arr[i]

for k in range(1, LOG_K+1):
    for i in range(1, m+1):
        temp = table[k-1][i]
        table[k][i] = table[k-1][temp]


for query in queries:
    count, cur = query
    temp_log = int(log2(count)) + 1

    idx = 0
    while idx < temp_log:
        if count % 2:
            cur = table[idx][cur]
        idx += 1
        count //= 2

    print(cur)