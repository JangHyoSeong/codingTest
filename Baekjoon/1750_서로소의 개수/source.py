from math import gcd

MOD = 10000003

def count_gcd_one_subsets(S):
    N = len(S)

    # 숫자의 최대값이 100000
    max_g = 100000

    # dp 수열 초기화
    dp = [0] * (max_g + 1)
    dp[0] = 1

    # 각 원소 s에 대해
    for s in S:

        # 새로운 dp 배열을 생성
        new_dp = dp[:]

        # dp를 역순으로 순회하면서
        for g in range(max_g, 0, -1):

            if dp[g] > 0:
                # 현재 수와 dp배열의 최대공약수를 찾음
                new_g = gcd(g, s)
                # 최소 공약수 개수를 더해줌
                new_dp[new_g] = (new_dp[new_g] + dp[g]) % MOD
        
        # 나누기
        new_dp[s] = (new_dp[s] + dp[0]) % MOD
        dp = new_dp
    
    return dp[1]

# 입력 받기
N = int(input())
S = [int(input()) for _ in range(N)]

# 결과 출력
result = count_gcd_one_subsets(S)
print(result)
