N, K = map(int, input().split())

def count(n):
    return bin(n).count('1')

answer = 0
while count(N) > K:
    add = N & -N
    N += add
    answer += add

print(answer)