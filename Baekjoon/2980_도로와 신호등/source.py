N, L = map(int, input().split())
traffics = [list(map(int, input().split())) for _ in range(N)]

time, pos = 0, 0

for D, R, G in traffics:
    time += (D - pos)
    pos = D

    cycle = R + G
    now = time % cycle

    if now < R:
        time += (R - now)
    
time += (L - pos)
print(time)