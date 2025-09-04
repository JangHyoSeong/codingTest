import sys

N, M, L, K = map(int, sys.stdin.readline().rstrip().split())
meteors = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(K)]

max_count = 0
for i in range(K):
    for j in range(K):
        x1 = meteors[i][0]
        y1 = meteors[j][1]

        count = 0

        for x, y in meteors:
            if x1 <= x <= x1 + L and y1 <= y <= y1 +L:
                count += 1

        max_count = max(max_count, count)

print(K - max_count)