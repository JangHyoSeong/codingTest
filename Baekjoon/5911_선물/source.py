N, B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

arr.sort(key= lambda x: (sum(x), x[0]))

max_count = 0
for i in range(N):
    coupon_cost = arr[i][0] // 2 + arr[i][1]
    others = sorted(arr[j][0] + arr[j][1] for j in range(N) if j != i)
    
    total, count = coupon_cost, 1
    for cost in others:
        if total + cost > B:
            break
        total += cost
        count += 1

    if total <= B:
        max_count = max(max_count, count)

print(max_count)