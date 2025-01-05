# 입력
N = int(input())
numbers = list(map(int, input().split()))

# DP 배열 정의
dp = [[0] * N for _ in range(2)]

# 초기값 설정
dp[0][0] = numbers[0]  # 수를 제거하지 않은 상태
dp[1][0] = float('-inf')  # 수를 제거한 상태는 불가능

# DP 점화식 계산
for i in range(1, N):
    dp[0][i] = max(dp[0][i-1] + numbers[i], numbers[i])  # 제거 X
    dp[1][i] = max(dp[1][i-1] + numbers[i], dp[0][i-1])  # 제거 O

result = max(max(dp[0]), max(dp[1]))
print(result)