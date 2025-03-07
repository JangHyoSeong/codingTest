from bisect import bisect_left

N = int(input())
arr = list(map(int, input().split()))

arr.sort()
result = 0

for i in range(N-2):
    left, right = i+1, N-1

    while left < right:
        score_sum = arr[i] + arr[left] + arr[right]

        if score_sum > 0:
            right -= 1
        else:
            if score_sum == 0:
                if arr[left] == arr[right]:
                    result += (right - left)
                else:
                    idx = bisect_left(arr, arr[right])
                    result += (right - idx + 1)
            left += 1

print(result)