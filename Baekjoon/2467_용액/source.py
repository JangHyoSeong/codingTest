N = int(input())
liqud = list(map(int, input().split()))

front, rear = 0, N-1

min_gap = 2000000000
while front < rear:
    cur_gap = liqud[front] + liqud[rear]

    if abs(cur_gap) <= min_gap:
        result_a, result_b = liqud[front], liqud[rear]
        min_gap = abs(cur_gap)

    if cur_gap <= 0:
        front += 1
    
    else:
        rear -= 1

print(result_a, result_b)