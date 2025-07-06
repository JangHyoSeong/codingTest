from itertools import combinations

def team_sum(team):
    ability = 0
    for i in team:
        for j in team:
            if i != j:
                ability += table[i][j]
    
    return ability

N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]

min_diff = int(21e8)
people = list(range(N))

for r in range(1, N // 2 + 1):
    for team in combinations(people, r):
        another_team = [p for p in people if p not in team]

        a_team = team_sum(team)
        b_team = team_sum(another_team)
        diff = abs(a_team - b_team)

        min_diff = min(min_diff, diff)
        if min_diff == 0:
            break

print(min_diff)