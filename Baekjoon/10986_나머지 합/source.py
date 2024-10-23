N, M = map(int, input().split())
arr = list(map(int, input().split()))

remainder = [0] * M
current_sum = 0
count = 0

remainder[0] = 1

for num in arr:
    current_sum = (current_sum + num) % M
    
    if current_sum < 0:
        current_sum += M
    
    count += remainder[current_sum]
    
    remainder[current_sum] += 1

print(count)