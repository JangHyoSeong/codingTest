N = int(input())

paper = [list(map(int, input().split())) for _ in range(N)]
paper_area = [0] * N

area = [[-1] * 1001 for _ in range(1001)]

for i in range(N):
    for j in range(paper[i][0], paper[i][0] + paper[i][2]):
        for k in range(paper[i][1], paper[i][1] + paper[i][3]):
            area[j][k] = i

for i in range(1001):
    for j in range(1001):
        if area[i][j] == -1:
            continue
        paper_area[area[i][j]] += 1

for i in paper_area:
    print(i)