from math import sqrt

a, b = map(int, input().split())

valid = [True] * (b-a+1)

for i in range(2, int(b**0.5) +1):
    square = i**2
    idx_1 = max(a//square, 1)
    idx_2 = b//square + 1

    for j in range(idx_1, idx_2):
        if square*j-a >= b-a+1 or square*j-a < 0:
            continue
        else:
            valid[square*j-a] = False        

print(valid.count(True))