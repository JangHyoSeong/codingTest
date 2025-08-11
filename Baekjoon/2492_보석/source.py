import sys

N, M, T, K = map(int, sys.stdin.readline().rstrip().split())
stones = [tuple(map(int, sys.stdin.readline().rstrip().split())) for _ in range(T)]

xs = {x for x, _ in stones}
ys = {y for _, y in stones}
xs.add(N - K)
ys.add(M - K)

xs = sorted(xs)
ys = sorted(ys)

max_count = 0
ans_x, ans_y = 0, 0

for X in xs:
    for Y in ys:
        if X < 0 or Y < 0 or X + K > N or Y + K > M:
            continue

        cnt = 0
        for sx, sy in stones:
            if X <= sx <= X + K and Y <= sy <= Y + K:
                cnt += 1

        if cnt > max_count:
            max_count = cnt
            ans_x, ans_y = X, Y

print(ans_x, ans_y + K)
print(max_count)