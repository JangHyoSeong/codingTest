import math

def find_kth_string(N, M, K):
    def binomial(n, k):
        if k > n:
            return 0
        return math.comb(n, k)
    
    if binomial(N + M, M) < K:
        return -1
    
    result = []
    
    while N > 0 and M > 0:
        
        count_a = binomial(N + M - 1, M)
        
        if K <= count_a:
            result.append('a')
            N -= 1
        else:
            result.append('z')
            M -= 1
            K -= count_a
    
    result.extend(['a'] * N)
    result.extend(['z'] * M)
    
    return ''.join(result)

N, M, K = map(int, input().split())
print(find_kth_string(N, M, K))
