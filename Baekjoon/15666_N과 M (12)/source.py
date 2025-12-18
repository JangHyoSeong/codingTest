N, M = map(int, input().split())
arr = sorted(set(map(int, input().split())))

result = []

def backtrack(start, depth):
    if depth == M:
        print(" ".join(map(str, result)))
        return
    
    for i in range(start, len(arr)):
        result.append(arr[i])
        backtrack(i, depth + 1)
        result.pop()

backtrack(0, 0)