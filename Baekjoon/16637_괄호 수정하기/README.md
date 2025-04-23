# [16637] 괄호 수정하기

### **난이도**
골드 3
## **📝문제**
길이가 N인 수식이 있다. 수식은 0보다 크거나 같고, 9보다 작거나 같은 정수와 연산자(+, -, ×)로 이루어져 있다. 연산자 우선순위는 모두 동일하기 때문에, 수식을 계산할 때는 왼쪽에서부터 순서대로 계산해야 한다. 예를 들어, 3+8×7-9×2의 결과는 136이다.

수식에 괄호를 추가하면, 괄호 안에 들어있는 식은 먼저 계산해야 한다. 단, 괄호 안에는 연산자가 하나만 들어 있어야 한다. 예를 들어, 3+8×7-9×2에 괄호를 3+(8×7)-(9×2)와 같이 추가했으면, 식의 결과는 41이 된다. 하지만, 중첩된 괄호는 사용할 수 없다. 즉, 3+((8×7)-9)×2, 3+((8×7)-(9×2))은 모두 괄호 안에 괄호가 있기 때문에, 올바른 식이 아니다.

수식이 주어졌을 때, 괄호를 적절히 추가해 만들 수 있는 식의 결과의 최댓값을 구하는 프로그램을 작성하시오. 추가하는 괄호 개수의 제한은 없으며, 추가하지 않아도 된다.
### **입력**
첫째 줄에 수식의 길이 N(1 ≤ N ≤ 19)가 주어진다. 둘째 줄에는 수식이 주어진다. 수식에 포함된 정수는 모두 0보다 크거나 같고, 9보다 작거나 같다. 문자열은 정수로 시작하고, 연산자와 정수가 번갈아가면서 나온다. 연산자는 +, -, * 중 하나이다. 여기서 *는 곱하기 연산을 나타내는 × 연산이다. 항상 올바른 수식만 주어지기 때문에, N은 홀수이다.
### **출력**
첫째 줄에 괄호를 적절히 추가해서 얻을 수 있는 결과의 최댓값을 출력한다. 정답은 $2^{31}$보다 작고, $-2^{31}$보다 크다.
### **예제입출력**

**예제 입력1**

```
9
3+8*7-9*2
```

**예제 출력1**

```
136
```

**예제 입력2**

```
5
8*3+5
```

**예제 출력2**

```
64
```

**예제 입력3**

```
7
8*3+5+2
```

**예제 출력3**

```
66
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N = int(input())
arr = list(input())

max_result = int(-21e8)
def calc(a, op, b):
    if op == '+':
        return a + b

    elif op == '-':
        return a - b
    
    elif op == '*':
        return a * b

def dfs(index, current_result):
    global max_result

    if index >= N:
        max_result = max(max_result, current_result)
        return
    
    op = arr[index-1]
    num = int(arr[index])
    next_result = calc(current_result, op, num)
    dfs(index+2, next_result)

    if index + 2 < N:
        next_num1 = int(arr[index])
        next_op = arr[index + 1]
        next_num2 = int(arr[index + 2])
        bracket_result = calc(next_num1, next_op, next_num2)
        total = calc(current_result, arr[index - 1], bracket_result)
        dfs(index + 4, total)

dfs(2, int(arr[0]))
print(max_result)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|32412|40|Python3|813
#### **📝해설**

**알고리즘**
```
1. 백트래킹
2. 구현
```

### **다른 풀이**

```python
n = int(input())
s = str(input())
maxi = []
def dfs(i, n, s, a):
    global maxi
    if i == n:
        maxi.append(a)
        return
    if i + 2 <= n-2:
        dfs(i+4, n, s, eval(str(a)+s[i]+str(eval(s[i+1:i+4]))))
    if i <= n-2:
        dfs(i+2, n, s, eval(str(a)+s[i:i+2]))

if s == 1:
    print(eval(s))
else:
    dfs(1, len(s), s, s[0])
    print(max(maxi))
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
iy-524|31120|32|Python3|367
#### **📝해설**

```python
N = int(input())
arr = list(input())

# 결과로 사용할 최대 계산 값
max_result = int(-21e8)

# 연산
def calc(a, op, b):
    if op == '+':
        return a + b

    elif op == '-':
        return a - b
    
    elif op == '*':
        return a * b

# DFS와 백트래킹을 통해 최대값 계산
def dfs(index, current_result):
    global max_result

    # 끝까지 계산했다면 값을 갱신
    if index >= N:
        max_result = max(max_result, current_result)
        return
    
    # 현재 인덱스에 맞는 연산자와 숫자를 통해 계산
    op = arr[index-1]
    num = int(arr[index])
    next_result = calc(current_result, op, num)

    # 다음 연산으로 인덱스를 키움
    dfs(index+2, next_result)

    # 괄호를 사용해서 계산하는 경우
    if index + 2 < N:
        # 괄호로 계산할 숫자와 연산자를 뽑아냄
        next_num1 = int(arr[index])
        next_op = arr[index + 1]
        next_num2 = int(arr[index + 2])

        # 값을 계산
        bracket_result = calc(next_num1, next_op, next_num2)

        # 현재 값을 포함해 괄호로 계산된 값을 적용
        total = calc(current_result, arr[index - 1], bracket_result)
        dfs(index + 4, total)

dfs(2, int(arr[0]))
print(max_result)
```