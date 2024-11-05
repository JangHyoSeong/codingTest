from collections import deque

T = int(input())

for testcase in range(T):
    operations = input()
    N = int(input())
    temp_string = input()

    if N == 0:
        if 'D' in operations:
            print('error')
        else:
            print('[]')
        continue

    temp_string = temp_string[1:-1]
    
    dq = deque(map(int, temp_string.split(",")))

    reverse = False
    for operation in operations:
        if operation == 'R':
            reverse = not reverse

        else:
            if dq:
                if reverse:
                    dq.pop()
                else:
                    dq.popleft()
            else:
                print('error')
                break
                
    else:
        dq = list(dq)
        if reverse:
            dq.reverse()
        print(f'[{",".join(map(str, dq))}]')