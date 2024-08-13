N, X = map(int, input().split())

burger_len = [0] * (N+1)
patty_count = [0] * (N+1)

burger_len[0] = 1
patty_count[0] = 1

for i in range(1, N+1):
    burger_len[i] = 2 * burger_len[i-1] + 3
    patty_count[i] = 2 * patty_count[i-1] + 1

def eat(level, x):
    if level == 0:
        return 1 if x > 0 else 0
    
    if x == 1:
        return 0
    elif x <= 1 + burger_len[level-1]:
        return eat(level-1, x-1)
    elif x == 2 + burger_len[level-1]:
        return patty_count[level-1]+1
    elif x <= 2 + 2 * burger_len[level-1]:
        return patty_count[level-1] + 1 + eat(level-1, x-1-burger_len[level-1])
    else:
        return 2 * patty_count[level-1]+1
    
print(eat(N, X))