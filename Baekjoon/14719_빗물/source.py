H, W = map(int, input().split())
arr = list(map(int, input().split()))

rain = 0
for i in range(1, W-1):
    left_max = max(arr[:i])
    right_max = max(arr[i+1:])

    valid_height = min(left_max, right_max)

    if arr[i] < valid_height:
        rain += valid_height - arr[i]

print(rain)