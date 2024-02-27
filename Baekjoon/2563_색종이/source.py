N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

canvas = [[0] * 100 for _ in range(100)]
count = 0
for i in range(N):
    for j in range(10):
        for k in range(10):
            canvas[paper[i][0] + j][paper[i][1] + k] = 1

for i in range(100):
    count += canvas[i].count(1)

print(count)