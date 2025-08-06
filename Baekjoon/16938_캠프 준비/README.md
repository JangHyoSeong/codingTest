# [16938] 캠프 준비

### **난이도**
골드 5
## **📝문제**
알고리즘 캠프를 열려면 많은 준비가 필요하다. 그 중 가장 중요한 것은 문제이다. 오늘은 백준이를 도와 알고리즘 캠프에 사용할 문제를 고르려고 한다.

백준이는 문제를 N개 가지고 있고, 모든 문제의 난이도를 정수로 수치화했다. i번째 문제의 난이도는 Ai이다.

캠프에 사용할 문제는 두 문제 이상이어야 한다. 문제가 너무 어려우면 학생들이 멘붕에 빠지고, 문제가 너무 쉬우면 학생들이 실망에 빠지게 된다. 따라서, 문제 난이도의 합은 L보다 크거나 같고, R보다 작거나 같아야 한다. 또, 다양한 문제를 경험해보기 위해 가장 어려운 문제와 가장 쉬운 문제의 난이도 차이는 X보다 크거나 같아야 한다.

캠프에 사용할 문제를 고르는 방법의 수를 구해보자.
### **입력**
첫째 줄에 N, L, R, X가 주어진다.

둘째 줄에는 문제의 난이도 A1, A2, ..., AN이 주어진다.
### **출력**
캠프에 사용할 문제를 고르는 방법의 수를 출력한다.
### **예제입출력**

**예제 입력1**

```
3 5 6 1
1 2 3
```

**예제 출력1**

```
2
```

**예제 입력2**

```
4 40 50 10
10 20 30 25
```

**예제 출력2**

```
2
```

**예제 입력3**

```
5 25 35 10
10 10 20 10 20
```

**예제 출력3**

```
6
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N, L, R, X = map(int, input().split())
arr = list(map(int, input().split()))

result = 0

def backtrack(index, selected):
    global result
    if len(selected) >= 2:
        total = sum(selected)
        if L <= total <= R and max(selected) - min(selected) >= X:
            result += 1

    for i in range(index, N):
        backtrack(i + 1, selected + [arr[i]])

backtrack(0, [])
print(result)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|32412|64|Python3|396
#### **📝해설**

**알고리즘**
```
1. 백트래킹
```

### **다른 풀이**

```python
from itertools import*
N,L,R,X=map(int,input().split())
S=sorted(list(map(int,input().split())))
t=0
for i in range(2,N+1):
 for a in combinations(S,i):
  if L<=sum(a)<=R and a[-1]-a[0]>=X:t+=1
print(t)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
joysteve|31120|44|Python3|202
#### **📝해설**

```python
N, L, R, X = map(int, input().split())
arr = list(map(int, input().split()))

result = 0

# 백트래킹으로 각 문제를 골랐을 때, 안골랐을 때를 나누어 탐색
def backtrack(index, selected):
    global result

    # 고른 문제가 2가지 이상이라면 조건을 검사
    if len(selected) >= 2:

        # 총합
        total = sum(selected)

        # 주어진 조건을 만족하면 += 1
        if L <= total <= R and max(selected) - min(selected) >= X:
            result += 1

    # 현재 상태에서, 다음 문제들을 골랐을 경우 탐색
    for i in range(index, N):
        backtrack(i + 1, selected + [arr[i]])

backtrack(0, [])
print(result)
```