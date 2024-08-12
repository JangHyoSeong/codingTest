N = int(input())

arr = [input() for _ in range(N)]
arr = list(set(arr))
arr.sort(key=lambda x : (len(x), x))

for a in arr:
    print(a)