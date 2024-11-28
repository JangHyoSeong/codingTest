K, N = map(int, input().split())
arr = [int(input()) for _ in range(K)]

min_length, max_length = 0, max(arr)
while min_length <= max_length:
    mid = (min_length + max_length) // 2

    count = 0
    for lan in arr:
        if mid:
            count += lan // mid
        else:
            print(1)
            exit()
    
    if count < N:
        max_length = mid - 1
    else:
        min_length = mid + 1

print(max_length)