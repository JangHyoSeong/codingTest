N, M = map(int, input().split())

if N == 0:
    print(0)
    exit()

arr = list(map(int, input().split()))

count = 1
now_weight = 0
for num in arr:
    now_weight += num

    if now_weight > M:
        now_weight = num
        count += 1

print(count)