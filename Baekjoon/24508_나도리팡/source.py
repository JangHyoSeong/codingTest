N, K, T = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
sum_arr = sum(arr)
if sum_arr % K:
    print('NO')
    exit()

count = 0

for i in range(sum_arr//K):
    count += K - arr[N-1-i]

if count > T:
    print('NO')
else:
    print('YES')