X, Y = map(int, input().split())

Z = (Y * 100) // X
if Z >= 99:
    print(-1)
    exit()

low, high = 1, 10**18
answer = -1

while low <= high:
    mid = (low + high) // 2
    new_Z = ((Y + mid) * 100) // (X + mid)

    if new_Z > Z:
        answer = mid
        high = mid - 1
    
    else:
        low = mid + 1

print(answer)