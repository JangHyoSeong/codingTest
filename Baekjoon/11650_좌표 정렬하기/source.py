N = int(input())
points = sorted([list(map(int, input().split())) for _ in range(N)])
for point in points:
    print(" ".join(map(str, point)))
