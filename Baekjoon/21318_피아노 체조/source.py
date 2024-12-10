N = int(input())
arr = list(map(int, input().split()))
Q = int(input())
queries = [tuple(map(int, input().split())) for _ in range(Q)]

mistakes = [0] * (N)
for i in range(1, N):
    if arr[i-1] > arr[i]:
        mistakes[i] = mistakes[i-1] + 1
    else:
        mistakes[i] = mistakes[i-1]

for query in queries:
    a, b = query
    print(mistakes[b-1] - mistakes[a-1])