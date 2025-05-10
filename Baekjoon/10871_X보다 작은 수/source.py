N, X = map(int, input().split())
arr = list(map(int, input().split()))
print(" ".join(str(a) for a in arr if a < X))