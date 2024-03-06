import sys
sys.stdin = open('input.txt')

T = int(input())

for testcase in range(1, T+1):
    N = int(input())
    atoms = []

    for _ in range(N):
        atom = list(map(int, input().split()))
        atom[0] += 1000
        atom[1] += 1000
        atoms.append(atom)
        
    visited = [[0] * 2001 for _ in range(2001)]

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    energy = 0

    for j in range(2001):
        stack = []
        
        for i in range(N):
            if atoms[i][3] == 0:
                continue
            x, y, direction, now_energy = atoms[i]
            if visited[x][y] == now_energy:
                visited[x][y] = 0
            
            # 움직임 계산
            nx = x + dx[direction]
            ny = y + dy[direction]
            if 0 <= nx <= 2000 and 0 <= ny <= 2000:
                atoms[i] = [nx, ny, direction, now_energy]
                visited[nx][ny] += now_energy
                stack.append([nx, ny, now_energy])
            else:
                atoms[i] = [nx, ny, direction, 0]

        for x, y, e in stack:

            if visited[x][y] > e:
                energy += visited[x][y]
                visited[x][y] = 0
                for i in range(N):
                    if atoms[i][0] == x and atoms[i][1] == y:
                        atoms[i][3] = 0

    print(f'#{testcase} {energy}')