from collections import deque

T = int(input())
for testcase in range(T):
    a, b = map(int, input().split())
    
    q = deque([(a, "")])
    visited = set()
    visited.add(a)

    while q:
        num, cmd = q.popleft()

        if num == b:
            print(cmd)
            break
        
        D = (num * 2) % 10000
        S = 9999 if num == 0 else num - 1
        L = (num % 1000) * 10 + (num // 1000)
        R = (num % 10) * 1000 + (num // 10)

        for next_num, command in [(D, "D"), (S, "S"), (L, "L"), (R, "R")]:
            if next_num not in visited:
                visited.add(next_num)
                q.append((next_num, cmd + command))