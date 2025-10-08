import sys

T = int(sys.stdin.readline().rstrip())
for testcase in range(T):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().rstrip().split())
    n = int(sys.stdin.readline().rstrip())
    count = 0

    for _ in range(n):
        cx, cy, r = map(int, sys.stdin.readline().rstrip().split())

        start_inside = (x1 - cx) ** 2 + (y1 - cy) ** 2 < r ** 2
        end_inside = (x2 - cx) ** 2 + (y2 - cy) ** 2 < r ** 2

        if start_inside ^ end_inside:
            count += 1
    print(count)