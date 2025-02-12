N = int(input())
K = int(input())
arr = list(map(int, input().split()))

if K >= N:
    print(0)
    exit()

arr.sort()
distances = [arr[i] - arr[i-1] for i in range(1, N)]
distances.sort()

print(sum(distances[:N-K]))