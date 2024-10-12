T = int(input())

for testcase in range(T):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    arr.sort()
    count = 0
    min_gap = float('inf')
    front, rear = 0, n-1

    while front < rear:
        sum = arr[front] + arr[rear]
        if abs(k-sum) == min_gap:
            count += 1
        
        elif abs(sum - k) < min_gap:
            min_gap = abs(sum - k)
            count = 1

        if sum == k:
            front += 1
            rear -= 1

        elif sum > k:
            rear -= 1
        else:
            front += 1

    print(count)