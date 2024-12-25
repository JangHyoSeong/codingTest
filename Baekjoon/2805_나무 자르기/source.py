N, M = map(int, input().split())
trees = list(map(int, input().split()))

max_height,min_height = max(trees), 0

while max_height >= min_height:
    mid = (max_height + min_height) // 2

    now_sum = 0
    for tree in trees:
        if tree > mid:
            now_sum += tree - mid
    
    if now_sum >= M:
        min_height = mid + 1
    else:
        max_height = mid - 1

print(max_height)