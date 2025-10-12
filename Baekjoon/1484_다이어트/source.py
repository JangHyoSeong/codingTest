G = int(input())

result = []
x, y = 1, 1

while True:
    diff = x*x - y*y

    if diff == G:
        result.append(x)
        x += 1
    
    elif diff > G:
        if x - y == 1:
            break
        y += 1
    
    else:
        x += 1

print("\n".join(map(str, result)) if result else -1)