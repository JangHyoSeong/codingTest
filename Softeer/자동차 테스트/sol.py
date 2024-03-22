import sys

N, Q = map(int, input().split())
car = list(map(int, input().split()))
car.sort()

def binarySearch(target):
    low = 0
    high = N-1

    while low <= high:
        mid = (low + high) // 2
        if target == car[mid]:
            return mid
        elif target > car[mid]:
            low = mid + 1
        else:
            high = mid - 1

    return False

for _ in range(Q):
    query = int(input())

    middle = binarySearch(query)

    if middle == False:
        cnt = 0
    else:
        cnt = (middle) * (N-middle-1)

    print(cnt)