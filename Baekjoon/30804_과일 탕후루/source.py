N = int(input())
fruits = list(map(int, input().split()))

count_arr = [0] * 10
front = 0
max_length = 0
unique_count = 0

for rear in range(N):
    if count_arr[fruits[rear]] == 0:
        unique_count += 1
    count_arr[fruits[rear]] += 1

    while unique_count > 2:
        count_arr[fruits[front]] -= 1
        if count_arr[fruits[front]] == 0:
            unique_count -= 1
        front += 1
    
    current_length = rear - front + 1
    max_length = max(max_length, current_length)

print(max_length)