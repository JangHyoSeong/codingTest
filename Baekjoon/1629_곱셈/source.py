a, b, c = map(int, input().split())

def devide(a, b, c):
    if b == 0:
        return 1
    elif b % 2 == 0:
        half = devide(a, b // 2, c)
        return (half * half) % c
    else:
        half = devide(a, (b-1) // 2, c)
        return (half * half * a) % c

print(devide(a, b, c))