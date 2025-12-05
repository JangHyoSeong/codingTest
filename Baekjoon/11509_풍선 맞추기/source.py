import sys

N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

arrow = {}

count = 0

for h in arr:
    if h in arrow and arrow[h] > 0:
        arrow[h] -= 1
        if h - 1 > 0:
            arrow[h-1] = arrow.get(h-1, 0) + 1
    
    else:
        count += 1
        if h - 1 > 0:
            arrow[h-1] = arrow.get(h-1, 0) + 1

print(count)