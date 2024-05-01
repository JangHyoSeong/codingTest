N = int(input())

# 각각 마지막 숫자가 0으로 끝난 경우의수, 1로 끝난 경우의 수
# 두 리스트의 값을 더하면 총 경우의 수
end_with_zero = [0] * N
end_with_one = [0] * N

# N이 1일때 0으로 끝난 수 1개
end_with_one[0] = 1
if N > 1:
    # N이 2일때 0으로 끝난 수 1개
    end_with_zero[1] = 1

# N이 1, 2일때는 무조건 1개. 그 이후부터 계산
# 1로 끝난다면 다음 수는 무조건 0이 나와야함
# 따라서 이전 숫자가 1로 끝났다면 다음 숫자가 0으로 끝난 경우의 수와 같음

# 0으로 끝난다면 다음 숫자는 1로 끝나거나 0으로 끝날 수 있음
# 따라서 다음에 0이 붙는 경우의 수는 이전 숫자의 모든 경우의수와 같음
for i in range(2, N):
    end_with_one[i] = end_with_zero[i-1]
    end_with_zero[i] = end_with_one[i-1] + end_with_zero[i-1]

print(end_with_zero[N-1] + end_with_one[N-1])