count = 0

def f(i, N, S):
    global count

    if i == N:
        subset_sum = 0
        for j in range(N):
            if bit[j]:
                subset_sum += numbers[j]

        if subset_sum == S:
            count += 1

    else:
        for j in range(1, -1, -1):
            bit[i] = j
            f(i+1, N, S)


N, S = map(int, input().split())

numbers = list(map(int, input().split()))
bit = [0] * N

f(0, N, S)
if S == 0:
    count -= 1

print(count)