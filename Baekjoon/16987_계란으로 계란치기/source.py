N = int(input())
eggs = [list(map(int, input().split())) for _ in range(N)]

max_crush = 0
def egg_crush(idx, N):

    global max_crush
    if idx == N:
        temp_crush = 0
        for i in range(N):
            if eggs[i][0] <= 0:
                temp_crush += 1
        max_crush = max(max_crush, temp_crush)
        return
    
    if eggs[idx][0] <= 0:
        egg_crush(idx+1, N)

    else:
        is_crashed = False
        for i in range(N):
            if idx == i or eggs[i][0] <= 0:
                continue
            is_crashed = True
            eggs[idx][0] -= eggs[i][1]
            eggs[i][0] -= eggs[idx][1]
            egg_crush(idx+1, N)
            eggs[idx][0] += eggs[i][1]
            eggs[i][0] += eggs[idx][1]
        
        if not is_crashed:
            egg_crush(N, N)

egg_crush(0, N)
print(max_crush)