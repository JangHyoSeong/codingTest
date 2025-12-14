arr = list(map(int, input()))
N = len(arr)

prefix = [0] * (N + 1)
for i in range(N):
    prefix[i+1] = prefix[i] + arr[i]

answer = 0
for length in range(N if N % 2 == 0 else N-1, 1, -2):
    half = length // 2

    for start in range(N - length + 1):
        mid = start + half
        end = start + length

        left_sum = prefix[mid] - prefix[start]
        right_sum = prefix[end] - prefix[mid]

        if left_sum == right_sum:
            answer = length
            print(answer)
            exit()

print(0)