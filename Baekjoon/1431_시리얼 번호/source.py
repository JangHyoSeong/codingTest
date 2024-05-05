N = int(input())
arr = [input() for _ in range(N)]

arr.sort(key=lambda x: (len(x), sum(int(c) for c in x if c.isdigit()), x))

for serial in arr:
    print(serial)