import sys

N = int(sys.stdin.readline().rstrip())
bulbs = list(map(int, sys.stdin.readline().rstrip()))
targets = list(map(int, sys.stdin.readline().rstrip()))

def toggle(bulbs, idx):
    for i in range(idx-1, idx+2):
        if 0 <= i < len(bulbs):
            bulbs[i] = (bulbs[i] + 1) % 2

def solve(N, bulbs, targets, start_from_zero):
    new_bulbs = bulbs[:]
    count = 0

    if start_from_zero:
        toggle(new_bulbs, 0)
        count += 1
    
    for i in range(1, N):
        if new_bulbs[i-1] != targets[i-1]:
            toggle(new_bulbs, i)
            count += 1

    return count if new_bulbs == targets else int(21e8)

result1 = solve(N, bulbs, targets, True)
result2 = solve(N, bulbs, targets, False)

result = min(result1, result2)
print(result if result != int(21e8) else -1)