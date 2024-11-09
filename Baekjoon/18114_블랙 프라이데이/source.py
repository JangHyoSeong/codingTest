import sys

N, C = map(int, input().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

arr.sort()

def binary_search(left, right, target):
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return False

def check(N, C):
    if C in arr:
        return True

    front, rear = 0, N - 1
    while front < rear:
        now_sum = arr[front] + arr[rear]
        
        if now_sum == C:
            return True
        elif now_sum > C:
            rear -= 1
        else:
            target = C - now_sum
            if arr[front] != target and arr[rear] != target and binary_search(front + 1, rear - 1, target):
                return True
            front += 1

    return False

print(1 if check(N, C) else 0)