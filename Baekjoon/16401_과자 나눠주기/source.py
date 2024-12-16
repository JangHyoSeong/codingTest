M, N = map(int, input().split())
snacks = list(map(int, input().split()))

min_length, max_length = 1, max(snacks)
result = 0

while min_length <= max_length:
    mid = (min_length + max_length) // 2

    total_count = sum(snack // mid for snack in snacks if mid > 0)

    if total_count >= M:
        result = mid
        min_length = mid + 1
    
    else:
        max_length = mid - 1

print(result)