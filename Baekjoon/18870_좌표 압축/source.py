N = int(input())
arr = list(map(int, input().split()))
sorted_arr = sorted(arr)
idx = 0

index_dict = {
    sorted_arr[0] : 0
}

for i in range(1, N):
    if sorted_arr[i] != sorted_arr[i-1]:
        idx += 1
        index_dict[sorted_arr[i]] = idx

for i in range(N):
    print(index_dict[arr[i]], end=" ")