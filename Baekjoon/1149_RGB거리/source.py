N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

costs = [[0] * 3 for _ in range(N+1)]

for i in range(1, N+1, 1):
    costs[i][0] = min(costs[i-1][1], costs[i-1][2]) + arr[i-1][0]
    costs[i][1] = min(costs[i-1][2], costs[i-1][0]) + arr[i-1][1]
    costs[i][2] = min(costs[i-1][0], costs[i-1][1]) + arr[i-1][2]
    
print(min(costs[-1]))