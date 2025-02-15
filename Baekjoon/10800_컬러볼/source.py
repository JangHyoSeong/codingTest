import sys
from collections import defaultdict

N = int(sys.stdin.readline().rstrip())
balls = [list(map(int, sys.stdin.readline().rstrip().split())) + [i] for i in range(N)]

balls.sort(key= lambda x : (x[1], x[0]))
color = [0] * (N+1)
result = [0] * (N)

total = 0
j = 0
for i in range(N):
    while balls[j][1] < balls[i][1]:
        color[balls[j][0]] += balls[j][1]
        total += balls[j][1]
        j += 1
    result[balls[i][2]] = total - color[balls[i][0]]

print("\n".join(map(str, result)))