# [7490] 0 만들기

### **난이도**
골드 5
## **📝문제**
1부터 N까지의 수를 오름차순으로 쓴 수열 1 2 3 ... N을 생각하자.

그리고 '+'나 '-', 또는 ' '(공백)을 숫자 사이에 삽입하자(+는 더하기, -는 빼기, 공백은 숫자를 이어 붙이는 것을 뜻한다). 이렇게 만든 수식의 값을 계산하고 그 결과가 0이 될 수 있는지를 살피자.

N이 주어졌을 때 수식의 결과가 0이 되는 모든 수식을 찾는 프로그램을 작성하라.
### **입력**
첫 번째 줄에 테스트 케이스의 개수가 주어진다(<10).

각 테스트 케이스엔 자연수 N이 주어진다(3 <= N <= 9).
### **출력**
각 테스트 케이스에 대해 ASCII 순서에 따라 결과가 0이 되는 모든 수식을 출력한다. 각 테스트 케이스의 결과는 한 줄을 띄워 구분한다.
### **예제입출력**

**예제 입력1**

```
2
3
7
```

**예제 출력1**

```
1+2-3

1+2-3+4-5-6+7
1+2-3-4+5+6-7
1-2 3+4+5+6+7
1-2 3-4 5+6 7
1-2+3+4-5+6-7
1-2-3-4-5+6+7
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
def calc(expr):
    expr = expr.replace(' ', '')
    total = 0
    num = ' '
    sign = 1

    for ch in expr:
        if ch in '+-':
            total += sign * int(num)
            num= ''
            sign = 1 if ch == '+' else -1
        else:
            num += ch
    
    total += sign * int(num)
    return total

def dfs(idx, expr, N, answers):
    if idx == N:
        if calc(expr) == 0:
            answers.append(expr)
        
        return
    
    for op in [' ', '+', '-']:
        dfs(idx + 1, expr + op + str(idx + 1), N, answers)


T = int(input())

for testcase in range(T):
    N = int(input())
    answers = []

    dfs(1, "1", N, answers)
    answers.sort()
    for answer in answers:
        print(answer)
    print()
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|32412|52|Python3|742
#### **📝해설**

**알고리즘**
```
1. 백트래킹
```

### **다른 풀이**

```python
import sys
input = sys.stdin.readline

def make_zero(n,val,cnt,string):
    if n == bound:
        if val == 0: print(string)
        return

    if cnt > 0: make_zero(n+1,val+9*cnt+n,10*cnt+n,f"{string} {n}")
    else: make_zero(n+1,val+9*cnt-n,10*cnt-n,f"{string} {n}")

    make_zero(n+1,val+n,n,f"{string}+{n}")
    make_zero(n+1,val-n,-n,f"{string}-{n}")
    
for _ in range(int(input())):
    N = int(input())
    bound = N+1
    make_zero(2,1,1,"1")
    print()
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
iwantappdev|31120|32|Python3|468
#### **📝해설**

```python

# 수식이 주어졌을 때 계산하는 함수
def calc(expr):

    # 공백을 제거하고 하나의 숫자로 합침
    expr = expr.replace(' ', '')

    # 수식의 결과
    total = 0

    # 연산해야 할 숫자
    num = ' '

    # +, - 부호
    sign = 1

    # 수식을 검사하면서
    for ch in expr:

        # 현재 단어가 부호라면
        if ch in '+-':

            # 앞에 나왔던 숫자를 계산
            total += sign * int(num)

            # 부호니까 숫자는 다시 초기화
            num= ''

            # 현재 부호에 맞게 음수, 양수인지를 설정
            sign = 1 if ch == '+' else -1
        
        # 현재 단어가 숫자라면 계산해야 할 숫자로 저장
        else:
            num += ch
    
    # 마지막에 닿았을 때, 마지막 숫자를 계산
    total += sign * int(num)
    return total

# 백트래킹을 위한 함수
def dfs(idx, expr, N, answers): # 현재 인덱스, 현재까지 만든 수식, 전체 길이, 정답을 담을 리스트
    
    # 마지막까지 수식을 만들었을 때
    if idx == N:

        # 계산 결과가 0이라면 결과로 추가
        if calc(expr) == 0:
            answers.append(expr)
        
        return
    
    # 공백, +, -를 모두 넣어보면서 DFS
    for op in [' ', '+', '-']:
        dfs(idx + 1, expr + op + str(idx + 1), N, answers)


T = int(input())

for testcase in range(T):
    N = int(input())
    answers = []

    dfs(1, "1", N, answers)
    answers.sort()
    for answer in answers:
        print(answer)
    print()
```