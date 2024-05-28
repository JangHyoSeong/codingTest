# [1253] 좋다

### **난이도**
골드 4
## **📝문제**
N개의 수 중에서 어떤 수가 다른 수 두 개의 합으로 나타낼 수 있다면 그 수를 “좋다(GOOD)”고 한다.

N개의 수가 주어지면 그 중에서 좋은 수의 개수는 몇 개인지 출력하라.

수의 위치가 다르면 값이 같아도 다른 수이다.
### **입력**
첫째 줄에는 수의 개수 N(1 ≤ N ≤ 2,000), 두 번째 줄에는 i번째 수를 나타내는 Ai가 N개 주어진다. (|Ai| ≤ 1,000,000,000, Ai는 정수)
### **출력**
좋은 수의 개수를 첫 번째 줄에 출력한다.
### **예제입출력**

**예제 입력1**

```
10
1 2 3 4 5 6 7 8 9 10
```

**예제 출력1**

```
8
```

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
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
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|31120|980|Python3|542
#### **📝해설**

**알고리즘**
```
1. 투 포인터
```


#### **📝해설**

```python
N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
# 수를 먼저 정렬한다

count = 0
for i in range(0, N):
    # 맨 앞과 맨 뒤의 인덱스를 지정함
    front, rear = 0, N-1
    
    # 인덱스가 겹치지 않을 때까지
    while front < rear:

        # 이번 탐색에서의 합
        sum_num = numbers[front] + numbers[rear]

        # 만약 두 숫자의 합이 현재 숫자보다 작다면
        if sum_num < numbers[i]:
            # 앞쪽의 인덱스를 증가
            front += 1

        # 만약 두 숫자의 합이 현재 숫자보다 크다면
        elif sum_num > numbers[i]:
            # 뒤쪽의 인덱스를 감소
            rear -= 1

        # 만약 두 숫자의 합이 현재 숫자와 같다면
        else:
            # 인덱스가 현재 숫자와 같다면 포함하지 않아야함
            if front == i:
                front += 1
            elif rear == i:
                rear -= 1
            
            # 인덱스가 현재 인덱스와 다르다면
            # 숫자를 1 증가
            else:
                count += 1
                break

print(count)
```