import sys

T = int(sys.stdin.readline().rstrip())

for testcase in range(T):
    N = int(sys.stdin.readline().rstrip())
    numbers = [sys.stdin.readline().rstrip() for _ in range(N)]
    numbers.sort()
    flag = True
    for i in range(N-1):
        if numbers[i+1].startswith(numbers[i]):
            flag = False
            break

    print("YES" if flag else "NO")
