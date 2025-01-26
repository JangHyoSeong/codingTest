N = int(input())
arr = list(map(int, input().split()))

max_score = max(arr)
print(sum(arr)/max_score * 100 / len(arr))