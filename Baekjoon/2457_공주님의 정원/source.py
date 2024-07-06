N = int(input())

flowers = []
for _ in range(N):
    temp_input = list(map(int, input().split()))
    flowers.append([temp_input[0] * 100 + temp_input[1], temp_input[2] * 100 + temp_input[3]])
    
flowers.sort()

current_end = 301
count = 0
i = 0

while current_end <= 1130:
    max_end = current_end
    while i < N and flowers[i][0] <= current_end:
        if flowers[i][1] > max_end:
            max_end = flowers[i][1]
        i += 1
    
    if max_end == current_end:
        count = 0
        break
    current_end = max_end
    count += 1
    
print(count)