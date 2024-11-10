N = int(input())
arr = list(map(int, input().split()))

arr.sort()
result = 0
before = 0
for i in range(N):
    before += arr[i]
    result += before
print(result)