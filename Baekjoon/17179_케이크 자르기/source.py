import sys

def can_make(x, q):
    count = 0
    last = 0

    for c in cuts:
        if c - last >= x:
            count += 1
            last = c
            if count == q:
                break
    
    if count == q and L - last >= x:
        return True
    
    return False

N, M, L = map(int, sys.stdin.readline().rstrip().split())
cuts = [int(sys.stdin.readline().rstrip()) for _ in range(M)]
queries = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

for q in queries:
    left, right = 1, L
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        if can_make(mid, q):
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
    
    print(answer)