N, max_weight = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

def select(i, N, temp_value, temp_weight):
    global max_value
    if i == N:
        if temp_weight <= max_weight and temp_value > max_value:
            max_value = temp_value
        return

    if temp_weight > max_weight:
        return
    
    select(i+1, N, temp_value + arr[i][1], temp_weight + arr[i][0])
    select(i+1, N, temp_value, temp_weight)
    

max_value = 0

select(0, N, 0, 0)
print(max_value)