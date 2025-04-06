import sys

N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
B, C = map(int, sys.stdin.readline().rstrip().split())

count = 0
for num in arr:
    count += 1
    num -= B

    if num > 0:
        if num % C:
            count += num // C + 1
        else:
            count += num // C

print(count)