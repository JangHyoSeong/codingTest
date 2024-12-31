def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

N = int(input())
M = int(input())

if M == 0:
    print(N)
    exit()

parent = list(range(N + 1))
check = [0] * (N + 1)
sections = [tuple(map(int, input().split())) for _ in range(M)]
sections.sort()

right = 0
for a, b in sections:
    if a < right:
        a = right

    num = find(parent, a)
    for j in range(a, b + 1):
        parent[j] = num
    right = b

cnt = 0
for i in range(1, N + 1):
    root = find(parent, i)
    if check[root] == 0:
        cnt += 1
        check[root] = 1

print(cnt)