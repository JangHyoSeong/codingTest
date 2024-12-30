T = int(input())

for testcase in range(T):
    bracket = input()

    count = 0
    for c in bracket:
        if c == '(':
            count += 1
        
        else:
            if count <= 0:
                print('NO')
                break
            else:
                count -= 1
    else:
        if count:
            print('NO')
        else:
            print('YES')