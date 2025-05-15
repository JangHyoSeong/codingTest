import sys

N, Q = map(int, sys.stdin.readline().rstrip().split())
ducks = [int(sys.stdin.readline().rstrip()) for _ in range(Q)]

tree = set()
result = []

for duck in ducks:
    path = []
    now = duck

    while now >= 1:
        path.append(now)
        now //= 2
    
    blocked = 0
    for land in reversed(path):
        if land in tree:
            blocked = land
            break
    
    print(blocked)
    if blocked == 0:
        tree.add(duck)