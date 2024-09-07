N = int(input())
arr = list(map(int, input().split()))
arr.sort()

result = []
closest_sum = float('inf')

for i in range(N-2):
    left = i+1
    right = N-1

    while left < right:
        current_sum = arr[i] + arr[left] + arr[right]

        if abs(current_sum) < abs(closest_sum):
            closest_sum = current_sum
            result = [arr[i], arr[left], arr[right]]

        if current_sum > 0:
            right -= 1
        elif current_sum < 0:
            left += 1
        else:
            print(" ".join(map(str, sorted(result))))
            exit()

print(" ".join(map(str, sorted(result))))