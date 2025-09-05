import sys

N = int(sys.stdin.readline().rstrip())
lines = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

lines.sort()

total_length = 0
cur_start, cur_end = lines[0]

for x, y in lines[1:]:

    if x <= cur_end:
        cur_end = max(cur_end, y)
    
    else:
        total_length += cur_end - cur_start
        cur_start, cur_end = x, y

total_length += cur_end - cur_start
print(total_length)