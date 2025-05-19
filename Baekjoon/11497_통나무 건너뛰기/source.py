import sys

T = int(sys.stdin.readline().rstrip())

for testcase in range(T):
    N = int(sys.stdin.readline().rstrip())
    arr = list(map(int, sys.stdin.readline().rstrip().split()))

    arr.sort()
    new_arr = [0] * N

    for i in range(N):
        if i % 2:
            new_arr[N - 1 - (i//2)] = arr[i]
        else:
            new_arr[i//2] = arr[i]

    max_gap = 0
    for i in range(N-1):
        max_gap = max(max_gap, abs(new_arr[i+1] - new_arr[i]))

    print(max_gap)