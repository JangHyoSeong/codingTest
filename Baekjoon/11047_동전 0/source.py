N, K = map(int, input().split())

coin = []
for _ in range(N):
    coin.append(int(input()))

count = 0
for i in range(N-1, -1, -1):
    count += K // coin[i]
    K %= coin[i]

print(count)