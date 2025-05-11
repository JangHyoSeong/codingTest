import sys

N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

total = sum(arr)
max_val = max(arr)

if max_val <= total - max_val + 1:
    print(total)
else:
    print((total - max_val) * 2 + 1)