T = int(input())

for testcase in range(T):
    bracket = input()

    stack = []
    for c in bracket:
        if c == '(':
            stack.append('(')
        else:
            if stack:
                stack.pop()
            else:
                print('NO')
                break

    else:
        if stack:
            print('NO')
        else:
            print('YES')