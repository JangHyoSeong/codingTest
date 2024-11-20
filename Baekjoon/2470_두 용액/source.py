N = int(input())
arr = list(map(int, input().split()))

arr.sort()
front, rear = 0, N-1

min_gap = 21e8
x, y = 0, N-1
while front < rear:
    new_gap = arr[front] + arr[rear]

    if min_gap > abs(new_gap):
        min_gap = abs(new_gap)
        x, y = front, rear

    if new_gap == 0:
        x, y = front, rear
        break

    elif new_gap > 0:
        rear -= 1
    
    else:
        front += 1


print(arr[x], arr[y])