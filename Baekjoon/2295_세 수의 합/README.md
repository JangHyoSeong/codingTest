# [2295] 세 수의 합

### **난이도**
골드 4
## **📝문제**
N(5 ≤ N ≤ 1,000)개의 자연수들로 이루어진 집합 U가 있다. 이 중에서 적당히 세 수를 골랐을 때, 그 세 수의 합 d도 U안에 포함되는 경우가 있을 수 있다. 이러한 경우들 중에서, 가장 큰 d를 찾으라.

예를 들어 {2, 3, 5, 10, 18}와 같은 집합이 있다고 하자. 2+3+5 = 10이 되고, 이 수는 집합에 포함된다. 하지만 3+5+10 = 18이 되고, 이 경우가 세 수의 합이 가장 커지는 경우이다.
### **입력**
첫째 줄에 자연수 N이 주어진다. 다음 N개의 줄에 차례로 U의 원소가 하나씩 주어진다. 주어진 U는 집합이 되므로 입력되는 두 수가 같아서는 안 된다. U의 원소는 200,000,000보다 작거나 같은 자연수이다. 답이 항상 존재하는 경우만 입력으로 주어진다.
### **출력**
우리가 x번째 수, y번째 수, z번째 수를 더해서 k번째 수를 만들었다라고 하자. 위의 예제에서 2+3+5=10의 경우는 x, y, z, k가 차례로 1, 2, 3, 4가 되며, 최적해의 경우는 2, 3, 4, 5가 된다. k번째 수가 최대가 되도록 하는 것이 목적이다. x, y, z, k가 서로 같아도 된다. 이때, k번째 수를 출력하면 된다.
### **예제입출력**

**예제 입력1**

```
5
2
3
5
10
18
```

**예제 출력1**

```
18
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N = int(input())
numbers = [int(input()) for _ in range(N)]
numbers.sort()

two_sum = set()
for i in range(N):
    for j in range(i, N):
        two_sum.add(numbers[i] + numbers[j])

for i in range(N-1, -1, -1):
    for j in range(i+1):
        if numbers[i] - numbers[j] in two_sum:
            print(numbers[i])
            exit()
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|191816|172|PyPy3|332
#### **📝해설**

**알고리즘**
```
1. 해쉬
```
#### **📝해설**

```python
N = int(input())
numbers = [int(input()) for _ in range(N)]
numbers.sort()

# 두 숫자를 더한 값을 모두 집합에 저장
two_sum = set()

for i in range(N):
    for j in range(i, N):
        two_sum.add(numbers[i] + numbers[j])

# 큰 수에서 작은수를 빼면서, 집합에 있는지 검사
for i in range(N-1, -1, -1):
    for j in range(i+1):

        # 가장 먼저 나온 값이 제일 큰 값
        if numbers[i] - numbers[j] in two_sum:
            print(numbers[i])
            exit()
```