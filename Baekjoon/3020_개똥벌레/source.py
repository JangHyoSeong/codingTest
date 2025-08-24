import sys

N, H = map(int, sys.stdin.readline().rstrip().split())

bot = [0] * (H + 2)
top = [0] * (H + 2)

for i in range(N):
    x = int(sys.stdin.readline().rstrip())
    if i % 2 == 0:
        bot[x] += 1
    
    else:
        top[x] += 1

for h in range(H, 0, -1):
    bot[h] += bot[h + 1]
    top[h] += top[h + 1]

crashes = [bot[h] + top[H-h+1] for h in range(1, H+1)]
m = min(crashes)
print(m, crashes.count(m))