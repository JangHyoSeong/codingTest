# [2529] 부등호

### **난이도**
실버 1
## **📝문제**
두 종류의 부등호 기호 ‘<’와 ‘>’가 k개 나열된 순서열 A가 있다. 우리는 이 부등호 기호 앞뒤에 서로 다른 한 자릿수 숫자를 넣어서 모든 부등호 관계를 만족시키려고 한다. 예를 들어, 제시된 부등호 순서열 A가 다음과 같다고 하자. 

A ⇒ < < < > < < > < >

부등호 기호 앞뒤에 넣을 수 있는 숫자는 0부터 9까지의 정수이며 선택된 숫자는 모두 달라야 한다. 아래는 부등호 순서열 A를 만족시키는 한 예이다. 

3 < 4 < 5 < 6 > 1 < 2 < 8 > 7 < 9 > 0

이 상황에서 부등호 기호를 제거한 뒤, 숫자를 모두 붙이면 하나의 수를 만들 수 있는데 이 수를 주어진 부등호 관계를 만족시키는 정수라고 한다. 그런데 주어진 부등호 관계를 만족하는 정수는 하나 이상 존재한다. 예를 들어 3456128790 뿐만 아니라 5689023174도 아래와 같이 부등호 관계 A를 만족시킨다. 

5 < 6 < 8 < 9 > 0 < 2 < 3 > 1 < 7 > 4

여러분은 제시된 k개의 부등호 순서를 만족하는 (k+1)자리의 정수 중에서 최댓값과 최솟값을 찾아야 한다. 앞서 설명한 대로 각 부등호의 앞뒤에 들어가는 숫자는 { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 }중에서 선택해야 하며 선택된 숫자는 모두 달라야 한다. 
### **입력**
첫 줄에 부등호 문자의 개수를 나타내는 정수 k가 주어진다. 그 다음 줄에는 k개의 부등호 기호가 하나의 공백을 두고 한 줄에 모두 제시된다. k의 범위는 2 ≤ k ≤ 9 이다. 
### **출력**
여러분은 제시된 부등호 관계를 만족하는 k+1 자리의 최대, 최소 정수를 첫째 줄과 둘째 줄에 각각 출력해야 한다. 단 아래 예(1)과 같이 첫 자리가 0인 경우도 정수에 포함되어야 한다. 모든 입력에 답은 항상 존재하며 출력 정수는 하나의 문자열이 되도록 해야 한다. 
### **예제입출력**

**예제 입력1**

```
2
< >
```

**예제 출력1**

```
897
021
```

**예제 입력2**

```
9
> < < < > > > < <
```

**예제 출력2**

```
9567843012
1023765489
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
K = int(input())
arr = list(input().split())

max_answer = ''
min_answer = ''

visited = [False] * 10

def valid(a, b, op):
    if op == '<':
        return a < b
    else:
        return a > b

def backtrack(depth, result):
    global max_answer, min_answer

    if depth == K+1:
        if not min_answer:
            min_answer = result
        
        else:
            max_answer = result
        
        return
    
    for i in range(10):
        if not visited[i]:
            if depth == 0 or valid(int(result[-1]), i, arr[depth - 1]):
                visited[i] = True
                backtrack(depth + 1, result + str(i))
                visited[i] = False
    
backtrack(0, '')
print(max_answer)
print(min_answer)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|32412|112|Python3|727
#### **📝해설**

**알고리즘**
```
1. 백트래킹
```
### **다른 풀이**

```python
#   https://boj.kr/2529
from itertools import permutations
k = int(input())
A = input().split()

M = []
c = 1
for i in A:
    if i == '>':
        M.append(c)
        c = 1
    else:
        c += 1
M.append(c)
s = e = 10
maxN = []
for i in M:
    s -= i
    for j in range(s, e):
        maxN.append(j)
    e -= i
print(*maxN, sep='')

m = []
c = 1
for i in A:
    if i == '<':
        m.append(c)
        c = 1
    else:
        c += 1
m.append(c)
s = e = -1
minN = []
for i in m:
    s += i
    for j in range(s, e, -1):
        minN.append(j)
    e += i
print(*minN, sep='')
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
dohyahn|31120|32|Python3|578
#### **📝해설**

```python
K = int(input())
arr = list(input().split())

# 최대, 최소값 정답을 문자열로 저장
max_answer = ''
min_answer = ''

# 어떤 숫자를 사용했는지 검사하기 위한 리스트
visited = [False] * 10

# a, b를 비교했을때 가능한 값인지 결과를 출력할 함수
def valid(a, b, op):
    if op == '<':
        return a < b
    else:
        return a > b

# 백트래킹 재귀함수
def backtrack(depth, result):
    global max_answer, min_answer

    # 모든 부등호를 완성했다면
    if depth == K+1:

        # 사전순으로 탐색되기에 가장 먼저 min_result가 나옴
        if not min_answer:
            min_answer = result
        
        # 마지막으로는 max_result가 나옴
        else:
            max_answer = result
        
        return
    
    # 숫자를 모두 사용해보면서
    for i in range(10):

        # 아직 사용하지 않은 숫자의 경우만 사용
        if not visited[i]:

            # 방금 시작했거나, 부등호를 만족하는 경우에 다음으로 넘어감
            if depth == 0 or valid(int(result[-1]), i, arr[depth - 1]):

                # 이번 숫자 사용처리
                visited[i] = True

                # 다음 뎁스로 넘어감
                backtrack(depth + 1, result + str(i))

                # 백트래킹
                visited[i] = False

# 함수 실행 및 출력
backtrack(0, '')
print(max_answer)
print(min_answer)
```