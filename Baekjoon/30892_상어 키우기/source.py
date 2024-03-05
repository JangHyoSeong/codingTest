N, eat_num, size = map(int, input().split())

size_arr = list(map(int, input().split()))
size_arr.sort(reverse=True)

count = 0
while count < eat_num:

    if size > size_arr[0]:
        idx = 0
        while count < eat_num:
            if idx >= N:
                break
            if size_arr[idx] != 0:
                size += size_arr[idx]
                count += 1
            idx += 1
        break

    for i in range(N):
        if size > size_arr[i] and size_arr[i] != 0:
            size += size_arr[i]
            size_arr[i] = 0
            count += 1
            break
    else:
        break

print(size)