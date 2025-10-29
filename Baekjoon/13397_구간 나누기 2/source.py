def is_possible(limit):
    count = 1
    min_val = arr[0]
    max_val = arr[0]

    for num in arr[1:]:
        min_val = min(min_val, num)
        max_val = max(max_val, num)

        if max_val - min_val > limit:
            count += 1
            min_val = num
            max_val = num
    
    return count <= M

N, M = map(int, input().split())
arr = list(map(int, input().split()))

min_score, max_score = 0, max(arr) - min(arr)
answer = max_score

while min_score <= max_score:
    mid = (min_score + max_score) // 2

    if is_possible(mid):
        answer = mid
        max_score = mid - 1
    
    else:
        min_score = mid + 1

print(answer)