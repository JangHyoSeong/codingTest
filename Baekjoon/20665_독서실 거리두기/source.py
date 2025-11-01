def to_min(t):
    h, m = int(t[:2]), int(t[2:])
    return h * 60 + m

N, T, P = map(int, input().split())
arr = []

for _ in range(T):
    s, e = input().split()
    arr.append((to_min(s), to_min(e)))

arr.sort(key=lambda x : (x[0], x[1] - x[0]))

seats = [0] * (N + 1)
P_occupied = [False] * 1260

for start, end in arr:
    now = start
    occupied = [i for i in range(1, N+1) if seats[i] > now]

    best_seat, best_dist = 0, -1
    for seat in range(1, N+1):
        if seats[seat] > now:
            continue

        dist = min([abs(seat - o) for o in occupied], default=N)
        if dist > best_dist:
            best_dist, best_seat = dist, seat
    
    seats[best_seat] = end
    if best_seat == P:
        for t in range(start, end):
            P_occupied[t] = True
    
total_time = 720
used_time = sum(P_occupied[540:1260])
print(total_time - used_time)