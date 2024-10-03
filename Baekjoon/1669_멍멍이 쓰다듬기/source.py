import math

X, Y = map(int, input().split())
gap = Y - X

if gap == 0:
    print(0)
else:
    k = int(math.sqrt(gap))
    
    if k * k == gap:
        print(2 * k - 1)
    elif k * k < gap <= k * k + k:
        print(2 * k)
    else:
        print(2 * k + 1)
