N = int(input())

def star(n):
    if n == 1:
        return ['*']
    
    small_star = star(n//3)
    pattern = []

    for line in small_star:
        pattern.append(line * 3)

    for line in small_star:
        pattern.append(line + ' ' * (n//3) + line)

    for line in small_star:
        pattern.append(line * 3)

    return pattern

print('\n'.join(star(N)))