import sys
from collections import defaultdict

N = int(sys.stdin.readline().rstrip())
arr = list(sys.stdin.readline().split())

factor_count = defaultdict(int)

def factorize(x, sign):
    x = abs(x)
    if x <= 1:
        return
    d = 2
    while d * d <= x:
        while x % d == 0:
            factor_count[d] += sign
            x //= d
        d += 1
    if x > 1:
        factor_count[x] += sign

first = int(arr[0])
if first == 0:
    print("mint chocolate")
    exit()

factorize(first, 1)

for i in range(1, len(arr), 2):
    op = arr[i]
    num = int(arr[i + 1])

    if op == "*":
        if num == 0:
            print("mint chocolate")
            exit()
        factorize(num, 1)
    else:
        factorize(num, -1)

for v in factor_count.values():
    if v < 0:
        print("toothpaste")
        break
else:
    print("mint chocolate")
