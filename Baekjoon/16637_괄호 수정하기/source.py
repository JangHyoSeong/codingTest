N = int(input())
arr = list(input())

max_result = int(-21e8)
def calc(a, op, b):
    if op == '+':
        return a + b

    elif op == '-':
        return a - b
    
    elif op == '*':
        return a * b

def dfs(index, current_result):
    global max_result

    if index >= N:
        max_result = max(max_result, current_result)
        return
    
    op = arr[index-1]
    num = int(arr[index])
    next_result = calc(current_result, op, num)
    dfs(index+2, next_result)

    if index + 2 < N:
        next_num1 = int(arr[index])
        next_op = arr[index + 1]
        next_num2 = int(arr[index + 2])
        bracket_result = calc(next_num1, next_op, next_num2)
        total = calc(current_result, arr[index - 1], bracket_result)
        dfs(index + 4, total)

dfs(2, int(arr[0]))
print(max_result)