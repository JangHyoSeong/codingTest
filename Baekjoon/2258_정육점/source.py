import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
meats = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

meats.sort(key = lambda x : (x[1], -x[0]))

weight_sum = 0
max_cost, total_cost = 0, 0

for i in range(N):
    weight, cost = meats[i]

    if weight_sum < M:
        weight_sum += weight
        
        if max_cost == cost:
            total_cost += cost
        else:
            max_cost = cost
            total_cost = cost
    
    elif max_cost == cost:
        continue

    elif total_cost > cost:
        total_cost = cost
        break

    else:
        break

if weight_sum < M:
    print(-1)
else:
    print(total_cost)