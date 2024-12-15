from collections import deque

T = int(input())

for testcase in range(T):
    string = input()

    left = deque()
    right = deque()

    for c in string:
        if c == '-':
            if left:
                left.pop()

        elif c == '<':
            if left:
                right.appendleft(left.pop())
        
        elif c == '>':
            if right:
                left.append(right.popleft())
        
        else:
            left.append(c)

    print(''.join(left) + ''.join(right))