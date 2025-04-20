import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    arr_1 = set(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline().rstrip())
    arr_2 = list(map(int, sys.stdin.readline().split()))
    
    for num in arr_2:
        print(1 if num in arr_1 else 0)