N, M = map(int, input().split())

arr = [i for i in range(1, N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[a-1], arr[b-1] = arr[b-1], arr[a-1]

print(" ".join(map(str, arr)))