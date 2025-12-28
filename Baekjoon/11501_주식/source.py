import sys

T = int(sys.stdin.readline().rstrip())
for testcase in range(T):
    N = int(sys.stdin.readline().rstrip())
    prices = list(map(int, sys.stdin.readline().rstrip().split()))

    max_price = 0
    profit = 0

    for i in range(N-1, -1, -1):
        if prices[i] > max_price:
            max_price = prices[i]
        
        else:
            profit += max_price - prices[i]
    
    print(profit)