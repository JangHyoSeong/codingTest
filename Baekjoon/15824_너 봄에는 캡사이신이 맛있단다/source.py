import sys

MOD = 10**9 + 7

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

pow2 = [1] * N
for i in range(1, N):
    pow2[i] = pow2[i - 1] * 2 % MOD

result = 0
for i in range(N):
    max_count = pow2[i]
    min_count = pow2[N-1-i]
    contribution = (max_count - min_count) * arr[i] % MOD
    result = (result + contribution) % MOD

print(result)