N = int(input())
arr = list(map(int, input().split()))

count = 0
while any(arr):
    for i in range(N):
        if arr[i] % 2 == 1:
            arr[i] -= 1
            count += 1
    
    if all(num == 0 for num in arr):
        break

    arr = [num // 2 for num in arr]
    count += 1

print(count)