N, M, K = map(int, input().split())
arr = list(map(int, input().split()))

min_dist, max_dist = 0, N
result = 0

while min_dist <= max_dist:
    mid = (min_dist + max_dist) // 2
    count = 1

    before_pos = arr[0]
    for i in range(1, K):
        if arr[i] - before_pos >= mid:
            count += 1
            before_pos = arr[i]
        
        if count >= M:
            result = mid
            min_dist = mid + 1
            break

    else:
        max_dist = mid - 1

answer = "1"
before_pos = arr[0]
count = 1
for i in range(1, K):
    if count < M and arr[i] - before_pos >= result:
        answer += "1"
        before_pos = arr[i]
        count += 1
    
    else:
        answer += "0"

print(answer)