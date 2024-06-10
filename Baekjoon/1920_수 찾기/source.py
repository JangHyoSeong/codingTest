N = int(input())
arr1 = sorted(list(map(int, input().split())))
M = int(input())
arr2 = list(map(int, input().split()))

for i in range(M):
    left, right= 0, N-1
    while left <= right:
        mid = (left + right) // 2
        if arr2[i] == arr1[mid]:
            print(1)
            break
        elif arr2[i] > arr1[mid]:
            left = mid+1
        else:
            right = mid-1
    else:
        print(0)