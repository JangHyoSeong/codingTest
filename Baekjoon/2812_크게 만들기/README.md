# [2812] 크게 만들기

### **난이도**
골드 3
## **📝문제**
N자리 숫자가 주어졌을 때, 여기서 숫자 K개를 지워서 얻을 수 있는 가장 큰 수를 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 N과 K가 주어진다. (1 ≤ K < N ≤ 500,000)

둘째 줄에 N자리 숫자가 주어진다. 이 수는 0으로 시작하지 않는다.
### **출력**
입력으로 주어진 숫자에서 K개를 지웠을 때 얻을 수 있는 가장 큰 수를 출력한다.
### **예제입출력**

**예제 입력1**

```
4 2
1924
```

**예제 출력1**

```
94
```

**예제 입력2**

```
7 3
1231234
```

**예제 출력2**

```
3234
```

**예제 입력3**

```
10 4
4177252841
```

**예제 출력3**

```
775841
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N, K = map(int, input().split())
number = list(input())

count = 0
stack = []

for i in range(N):
    if stack == []:
        stack.append(int(number[i]))
    else:
        while stack and stack[-1] < int(number[i]) and count < K:
            stack.pop()
            count += 1
        stack.append(int(number[i]))
            

if count < K:
    for _ in range(count, K):
        stack.pop()

print("".join(map(str, stack)))
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|57276|388|Python3|425
#### **📝해설**

**알고리즘**
```
1. 그리디 알고리즘
2. 스택
```

### **다른 풀이**

```python
import sys
input =sys.stdin.readline

def find_largest_number(N, K, number):
    stack = []
    num_to_remove = K

    for digit in number:

        while num_to_remove > 0 and stack and stack[-1] < digit:
            stack.pop()
            num_to_remove -= 1
        stack.append(digit)
    # If we haven't removed enough digits, remove the remaining from the end
    if num_to_remove > 0:
        stack = stack[:-num_to_remove]

    return ''.join(stack)

# 입력
N, K = map(int, input().split())
number = input().strip()

# 출력
print(find_largest_number(N, K, number))
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
ckdgh6589|34252|92|Python3|579
#### **📝해설**

```python
N, K = map(int, input().split())
number = list(input())

count = 0
stack = []

# 숫자를 왼쪽부터 차례대로 순회
for i in range(N):

    # 스택이 비어있다면 일단 삽입
    if stack == []:
        stack.append(int(number[i]))
    else:

        # 만약 스택의 top이 현재 숫자보다 작다면 pop
        while stack and stack[-1] < int(number[i]) and count < K:
            stack.pop()
            count += 1

        # 스택이 비거나, 스택의 top이 현재 숫자보다 크다면 push
        stack.append(int(number[i]))
            

# 만약 pop횟수를 채우지 못했다면, top에서 부터 pop
if count < K:
    for _ in range(count, K):
        stack.pop()

print("".join(map(str, stack)))
```