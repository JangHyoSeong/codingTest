from itertools import permutations

N = int(input())
innings = [list(map(int, input().split())) for _ in range(N)]

max_score = 0

others = [i for i in range(1, 9)]

for order in permutations(others):
    batting_order = list(order[:3]) + [0] + list(order[3:])
    score = 0
    batter_idx = 0

    for inning in innings:
        out_count = 0
        base = [0, 0, 0]

        while out_count < 3:
            player = batting_order[batter_idx]
            result = inning[player]

            if result == 0:
                out_count += 1
            elif result == 1:
                score += base[2]
                base = [1] + base[:2]
            elif result == 2:
                score += base[2] + base[1]
                base = [0, 1, base[0]]
            elif result == 3:
                score += base[2] + base[1] + base[0]
                base = [0, 0, 1]
            elif result == 4:
                score += base[0] + base[1] + base[2] + 1
                base = [0, 0, 0]

            batter_idx = (batter_idx + 1) % 9

    max_score = max(max_score, score)

print(max_score)