from itertools import combinations

N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]

team = list(combinations(range(N), N//2))

team_len = len(team)

min_gap = 200 * N

for i in range(team_len // 2):
    temp_gap = 0
    team1_sum = 0
    team2_sum = 0
    for member1 in team[i]:
        for member2 in team[i]:
            team1_sum += table[member1][member2]

    for member1 in team[team_len -1 -i]:
        for member2 in team[team_len -1 -i]:
            team2_sum += table[member1][member2]

    temp_gap = abs(team2_sum - team1_sum)
    min_gap = min(min_gap, temp_gap)

print(min_gap)