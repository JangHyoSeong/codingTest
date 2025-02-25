N = int(input())

f = [0] * (N+1)
g = [0] * (N+1)

for i in range(1, N+1):
    for j in range(i, N+1, i):
        f[j] += i

for i in range(1, N+1):
    g[i] = g[i-1] + f[i]

print(g[N])