def calc(expr):
    expr = expr.replace(' ', '')
    total = 0
    num = ' '
    sign = 1

    for ch in expr:
        if ch in '+-':
            total += sign * int(num)
            num= ''
            sign = 1 if ch == '+' else -1
        else:
            num += ch
    
    total += sign * int(num)
    return total

def dfs(idx, expr, N, answers):
    if idx == N:
        if calc(expr) == 0:
            answers.append(expr)
        
        return
    
    for op in [' ', '+', '-']:
        dfs(idx + 1, expr + op + str(idx + 1), N, answers)


T = int(input())

for testcase in range(T):
    N = int(input())
    answers = []

    dfs(1, "1", N, answers)
    answers.sort()
    for answer in answers:
        print(answer)
    print()