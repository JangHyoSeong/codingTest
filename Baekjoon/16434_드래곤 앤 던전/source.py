N, atk = map(int, input().split())
rooms = [list(map(int, input().split())) for _ in range(N)]

now_hp = 0
min_hp = 0

for room in rooms:
    if room[0] == 1:
        count = room[2] // atk
        rest = room[2] % atk

        if rest:
            atk_count = count
        else:
            atk_count = count-1

        now_hp -= (atk_count) * room[1]
        min_hp = min(now_hp, 0, min_hp)
        
    else:
        now_hp = min(room[2]+now_hp, 0)
        atk += room[1]

print(-min_hp+1)
