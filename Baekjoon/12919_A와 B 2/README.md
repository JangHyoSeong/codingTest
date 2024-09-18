# [12919] A와 B 2

### **난이도**
골드 5
## **📝문제**
수빈이는 A와 B로만 이루어진 영어 단어 존재한다는 사실에 놀랐다. 대표적인 예로 AB (Abdominal의 약자), BAA (양의 울음 소리), AA (용암의 종류), ABBA (스웨덴 팝 그룹)이 있다.

이런 사실에 놀란 수빈이는 간단한 게임을 만들기로 했다. 두 문자열 S와 T가 주어졌을 때, S를 T로 바꾸는 게임이다. 문자열을 바꿀 때는 다음과 같은 두 가지 연산만 가능하다.

문자열의 뒤에 A를 추가한다.
문자열의 뒤에 B를 추가하고 문자열을 뒤집는다.
주어진 조건을 이용해서 S를 T로 만들 수 있는지 없는지 알아내는 프로그램을 작성하시오. 
### **입력**
첫째 줄에 S가 둘째 줄에 T가 주어진다. (1 ≤ S의 길이 ≤ 49, 2 ≤ T의 길이 ≤ 50, S의 길이 < T의 길이)
### **출력**
S를 T로 바꿀 수 있으면 1을 없으면 0을 출력한다.
### **예제입출력**

**예제 입력1**

```
A
BABA
```

**예제 출력1**

```
1
```

**예제 입력2**

```
BAAAAABAA
BAABAAAAAB
```

**예제 출력2**

```
1
```

**예제 입력3**

```
A
ABBA
```

**예제 출력3**

```
0
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from collections import deque

S = input()
T = input()

S_length = len(S)
visited = {}

q = deque([T])

while q:
    now = q.popleft()

    if now == S:
        print(1)
        break

    if len(now) > S_length:
        if now[-1] == 'A':
            next = now[:-1]
            if visited.get(next) is None:
                q.append(next)
                visited[next] = True
        
        if now[0] == 'B':
            next = now[:0:-1]
            q.append(next)
            visited[next] = True


else:
    print(0)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|34000|60|Python3|523
#### **📝해설**

**알고리즘**
```
1. BFS
```

#### **📝해설**

```python
from collections import deque

# 입력받기
S = input()
T = input()

# 목표로 하는 문자열의 길이를 저장
S_length = len(S)

# 이미 만들었던 문자열은 만들지 않기 위해 딕셔너리 사용
visited = {}

# 시작 문자열 삽입. 큰 문자열에서 작은 문자열로 만듦
q = deque([T])

# BFS
while q:
    now = q.popleft()

    # 만약 만들어야 할 문자열을 찾았다면 break
    if now == S:
        print(1)
        break

    # 만들어야 할 문자열의 길이까지만 탐색
    if len(now) > S_length:

        # 뒤에 A를 추가 한 경우 A를 뺌
        if now[-1] == 'A':
            next = now[:-1]
            if visited.get(next) is None:
                q.append(next)
                visited[next] = True
        
        # B를 추가하고 뒤집은 경우 앞의 B를 뺌
        if now[0] == 'B':
            next = now[:0:-1]
            q.append(next)
            visited[next] = True


else:
    print(0)
```

### **🔖정리**

1. 줄이는 방식으로 만들면 경우의 수가 줄어들어서 메모리 초과를 막을 수 있다!!