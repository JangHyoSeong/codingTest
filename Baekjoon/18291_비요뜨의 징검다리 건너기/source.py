T = int(input())

def power(n):
    if n == 0:
        return 1

    if n == 1:
        return 2

    next = power(n//2) % 1000000007
    
    if n % 2:
        return next * next * 2 % 1000000007
    
    else:
        return next * next % 1000000007

for _ in range(T):
    N = int(input())

    if N <= 2:
        print(1)
        continue

    print(power(N-2))