import sys

T = int(sys.stdin.readline().rstrip())

for testcase in range(T):
    N, M, K = map(int, sys.stdin.readline().rstrip().split())
    arr = list(map(int, sys.stdin.readline().rstrip().split()))

    money = arr + arr[:M-1]
    count = 0
    money_sum = sum(arr[:M])
    if money_sum < K:
        count += 1

    if M == N:
        print(count)
        continue

    for i in range(N-1):
        money_sum = money_sum - money[i] + money[i+M]
        if money_sum < K:
            count += 1
    
    print(count)