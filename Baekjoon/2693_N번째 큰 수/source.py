T = int(input())
for testcase in range(T):
    arr = list(map(int, input().split()))
    arr.sort()
    print(arr[-3])