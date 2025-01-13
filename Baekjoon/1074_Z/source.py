N, r, c = map(int, input().split())

result = 0
size = 2 ** (N-1)

while N > 0:

    if r < size and c < size:
        pass

    elif r < size and c >= size:
        result += size * size
        c -= size

    elif r >= size and c < size:
        result += 2 * size * size
        r -= size
    
    else:
        result += 3 * size * size
        r -= size
        c -= size

    size //= 2
    N -= 1

print(result)