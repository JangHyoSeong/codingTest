N = int(input())
lengths = list(map(int, input().split()))
costs = list(map(int, input().split()))

min_cost = costs[0]
total_cost = 0

for i in range(N - 1):
    total_cost += min_cost * lengths[i]
    min_cost = min(min_cost, costs[i + 1])

print(total_cost)