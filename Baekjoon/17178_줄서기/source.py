N = int(input())

prev_max = list(map(int, input().split()))
prev_min = prev_max[:]

for _ in range(1, N):
    current = list(map(int, input().split()))
    max0 = max(prev_max[0], prev_max[1]) + current[0]
    max1 = max(prev_max) + current[1]
    max2 = max(prev_max[1], prev_max[2]) + current[2]
    
    min0 = min(prev_min[0], prev_min[1]) + current[0]
    min1 = min(prev_min) + current[1]
    min2 = min(prev_min[1], prev_min[2]) + current[2]

    prev_max = [max0, max1, max2]
    prev_min = [min0, min1, min2]

print(max(prev_max), min(prev_min))