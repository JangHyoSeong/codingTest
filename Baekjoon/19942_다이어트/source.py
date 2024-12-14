N = int(input())
mp, mf, ms, mv = map(int, input().split())
foods = [list(map(int, input().split())) for _ in range(N)]

min_cost = float('inf')
best_combination = []

def select_food(idx, food, cost, protein, fat, carb, vitamin):
    global min_cost, best_combination

    if idx == N:
        if protein >= mp and fat >= mf and carb >= ms and vitamin >= mv:
            if cost < min_cost:
                min_cost = cost
                best_combination = food[:]
            elif cost == min_cost:
                if food < best_combination:
                    best_combination = food[:]
        return

    select_food(idx + 1, food, cost, protein, fat, carb, vitamin)

    current_food = foods[idx]

    select_food(idx + 1,
                food + [idx + 1],
                cost + current_food[4],
                protein + current_food[0],
                fat + current_food[1],
                carb + current_food[2],
                vitamin + current_food[3])

select_food(0, [], 0, 0, 0, 0, 0)

if min_cost == float('inf'):
    print(-1)
else:
    print(min_cost)
    print(' '.join(map(str, sorted(best_combination))))