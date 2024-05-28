N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

count = 0
for i in range(0, N):
    front, rear = 0, N-1
    
    while front < rear:

        sum_num = numbers[front] + numbers[rear]

        if sum_num < numbers[i]:
            front += 1

        elif sum_num > numbers[i]:
            rear -= 1

        else:
            if front == i:
                front += 1
            elif rear == i:
                rear -= 1
            
            else:
                count += 1
                break

print(count)