import sys
sys.stdin = open('input.txt')

T = int(input())

for testcase in range(1, T+1):
    N = int(input())
    atoms = [list(map(int, input().split())) for _ in range(N)]

    dx = [0, 0, -0.5, 0.5]
    dy = [0.5, -0.5, 0, 0]
    energy = 0

    while len(atoms) >= 2:

        now_location = {}
        new_atoms = []
        for i in range(len(atoms)):
            nx, ny, direction, now_energy = atoms[i]
            nx += dx[direction]
            ny += dy[direction]
            atoms[i] = [nx, ny, direction, now_energy]
        
        for atom in atoms:
            try:
                now_location[(atom[0], atom[1])].append(atom)
            except:
                now_location[(atom[0], atom[1])] = [atom]


        for l in now_location:
            if len(now_location[l]) >= 2:
                for e in now_location[l]:
                    energy += e[3]
            else:
                if -1000 <= now_location[l][0][0] <= 1000 and -1000 <= now_location[l][0][1] <= 1000:
                    new_atoms.append(now_location[l][0])

        atoms = new_atoms     
            
    print(f'#{testcase} {energy}')