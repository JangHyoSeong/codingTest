# [2405] 문제제목

### **난이도**
골드 4
## **📝문제**
n개의 정수 A[1], A[2], …, A[n]이 있다. 서로 다른 세 정수 i, j, k에 대해서 a = A[i], b = A[j], c = A[k]라 하자. 세 수의 중위(Median)값은 정렬했을 때 가운데에 오는 수가 된다. 세 수의 평균(Mean)값은 (a+b+c)÷3이 된다.

만약 세 수가 5, 2, 5라면 중위값은 5, 평균값은 4가 된다. 세 수가 2, 3, 1이라면 중위값은 2, 평균값도 2가 된다.

n개의 수들이 주어졌을 때, 위와 같이 세 수를 선택하여(i, j, k가 서로 다르도록) 중위값과 평균값의 차이가 최대가 되도록 해 보시오.
### **입력**
첫째 줄에 정수 n(3 ≤ n ≤ 100,000)이 주어진다. 다음 n개의 줄에는 n개의 정수들이 주어진다. 각 수들의 절댓값은 100,000,000을 넘지 않는다.
### **출력**
첫째 줄에 중위값과 평균값의 차이를 세 배 한 값을 출력한다.
### **예제입출력**

**예제 입력1**

```
5
100
234
430
120
489
```

**예제 출력1**

```
349
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys

N = int(input())
numbers = []
for _ in range(N):
    number = int(sys.stdin.readline().rstrip())
    numbers.append(number)

numbers.sort()

max_gap = 0
for i in range(1, N-1):
    avg_min = (numbers[0] + numbers[i] + numbers[i+1])
    avg_max = (numbers[i-1] + numbers[i] + numbers[N-1])

    max_gap = max(max_gap, abs(avg_max - numbers[i]*3), abs(avg_min - numbers[i]*3))

print(max_gap)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|117444|128|PyPy3|402
#### **📝해설**

**알고리즘**
```
1. 그리디 알고리즘
```

### **다른 풀이**

```python
# 2405 세 수, 두 M G4

import sys


def solution() :
    input = sys.stdin.readline
    n = int(input())
    nums = [int(input()) for _ in range(n)]
    nums.sort()
    answer = 0
    for i in range(1, n-1) :
        answer = max(answer, abs(nums[i-1] - nums[i]*2 + nums[-1]), abs(nums[0] - nums[i]*2 + nums[i+1]))
    return answer


if __name__ == "__main__" :
    print(solution())
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
kkp0639|35304|132|Python3|387
#### **📝해설**

```python
import sys

# 입력받기
N = int(input())
numbers = []
for _ in range(N):
    number = int(sys.stdin.readline().rstrip())
    numbers.append(number)

# 정렬
numbers.sort()

# 최대 차이를 구하기 위해 초기값 선언
max_gap = 0
for i in range(1, N-1):

    # numbers[i]를 중간값으로 두고, 이때 가능한 최소 평균값, 최대 평균값을 구함
    avg_min = (numbers[0] + numbers[i] + numbers[i+1])
    avg_max = (numbers[i-1] + numbers[i] + numbers[N-1])

    # 최대평균, 최소평균을 통해 최대 차이를 갱신함
    max_gap = max(max_gap, abs(avg_max - numbers[i]*3), abs(avg_min - numbers[i]*3))

print(max_gap)
```