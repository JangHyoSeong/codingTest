N, I, M = map(int, input().split())
fish = [tuple(map(int, input().split())) for _ in range(M)]

rects = []
half = I // 2
for w in range(1, half):
    h = half - w
    rects.append((w, h))
    
    if w != h:
        rects.append((h, w))

answer = 0

xs = sorted({x for x, _ in fish})
ys = sorted({y for _, y in fish})

for x in xs:
    for y in ys:
        for w, h in rects:

            if x + h - 1 <= N and y + w - 1 <= N:
                count = 0
                for fx, fy in fish:
                    if x <= fx <= x + h and y <= fy <= y + w:
                        count += 1
                
                answer = max(answer, count)

print(answer)