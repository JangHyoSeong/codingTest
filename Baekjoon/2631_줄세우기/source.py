import bisect

N = int(input())
numbers = [int(input()) for _ in range(N)]

lis = []
for num in numbers:
    idx = bisect.bisect_left(lis, num)
    if idx == len(lis):
        lis.append(num)
    else:
        lis[idx] = num

print(N - len(lis))