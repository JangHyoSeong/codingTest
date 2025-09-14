N = int(input())

table = [-1] * N
result = 0

def check_valid(x, y):
    for i in range(x):
        if table[i] == y or abs(x - i) == abs(y - table[i]):
            return False
    
    return True

def backtracking(depth, N):
    global result

    if depth == N:
        result += 1
        return

    for i in range(N):
        if check_valid(depth, i):
            table[depth] = i
            backtracking(depth + 1, N)

backtracking(0, N)
print(result)