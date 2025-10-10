N, L = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
count = 1
start = arr[0]

for x in arr:
    if x - start + 0.5 > L:
        count += 1
        start = x

print(count)