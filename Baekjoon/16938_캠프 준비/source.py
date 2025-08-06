N, L, R, X = map(int, input().split())
arr = list(map(int, input().split()))

result = 0

def backtrack(index, selected):
    global result
    if len(selected) >= 2:
        total = sum(selected)
        if L <= total <= R and max(selected) - min(selected) >= X:
            result += 1

    for i in range(index, N):
        backtrack(i + 1, selected + [arr[i]])

backtrack(0, [])
print(result)