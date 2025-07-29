import sys

input = sys.stdin.readline
N, M = map(int, input().split())

a = {input().strip() for _ in range(N)}
b = {input().strip() for _ in range(M)}

result = sorted(a & b)

print(len(result))
print(*result, sep='\n')