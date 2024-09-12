def solution(n):
    answer = 0
    
    dp = [0] * (n)
    dp[0] = 1
    
    if n > 1:
        dp[1] = 2
    
    for i in range(2, n):
        dp[i] = (dp[i-1] + dp[i-2]) % 1000000007
    
    return dp[n-1]