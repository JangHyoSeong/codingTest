# [25381] ABBC

### **난이도**
골드 3
## **📝문제**
A, B, C로만 이루어졌고 길이가 |S|인 문자열 S가 있다. 당신은 이 문자열에 다음과 같은 시행을 할 수 있다.

- A와 그 뒤에 있는 B를 지운다.
- B와 그 뒤에 있는 C를 지운다.
각 문자는 최대 한 번만 지울 수 있다.

예를 들어 ABCBA를 보자. 각 문자에 왼쪽부터 1번, 2번, 3번. . . 과 같이 번호를 붙이면 다음과 같이 시행할 수 있다.

- 1번 A와 2번 B를 지운다. 이 경우 시행의 횟수는 1번이고, 남은 문자열은 CBA이다. 어떤 두 문자를 골라도 시행의 조건을 만족시킬 수 없으므로, 더 이상 시행을 할 수 없다.
- 1번 A와 4번 B를 지우고, 이어 2번 B와 3번 C를 지운다. 이 경우 시행의 횟수는 2번이고 남은 문자열은 A이다. 문자열에 남은 문자가 하나이므로, 더 이상 시행을 할 수 없다.  
이외에도 시행을 할 수 있는 여러 경우의 수가 있다.

시행을 할 수 있는 최대 횟수를 구해라.
### **입력**
첫 번째 줄에 문자열 S가 주어진다.
- 1 ≤ |S| ≤ 300 000
- S의 모든 문자는 A, B, C 중 하나이다.
### **출력**
첫 번째 줄에 답을 출력한다.
### **예제입출력**

**예제 입력1**

```
ABCBA
```

**예제 출력1**

```
2
```

**예제 입력2**

```
ABCBBACBABB
```

**예제 출력2**

```
5
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from collections import deque

s = input()

count = 0
a_q = deque()
b_q = deque()
c_q = deque()

for i in range(len(s)-1, -1, -1):
    if s[i] == 'A':
        a_q.append(i)
    elif s[i] == 'B':
        b_q.append(i)
    else:
        c_q.append(i)

while a_q:
    a_idx = a_q.popleft()
    if b_q:
        if a_idx < b_q[0]:
            count += 1
            b_q.popleft()
    else:
        break

while b_q:
    b_idx = b_q.popleft()
    if c_q:
        if b_idx < c_q[0]:
            count += 1
            c_q.popleft()

print(count)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|117840|152|PyPy3|538
#### **📝해설**

**알고리즘**
```
1. 자료구조
2. 그리디 알고리즘
```

### **다른 풀이**

```python
import sys

S = list(map(ord, (sys.stdin.readline().strip())))

def count(left: int, right: int) -> int:
    cnt, lCnt = 0, 0
    for ch in S:
        if (ch == left):
            lCnt += 1
        elif (ch == right and lCnt > 0):
            lCnt -= 1
            cnt += 1
    return cnt

print(min(count(65, 66) + count(66, 67), S.count(66)))

```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
hw0603|33956|88|Python3|345
#### **📝해설**

```python
from collections import deque

s = input()

count = 0

# 각 문자의 인덱스를 저장할 deque를 선언
a_q = deque()
b_q = deque()
c_q = deque()

# 문자의 인덱스를 오름차순으로 저장
for i in range(len(s)-1, -1, -1):
    if s[i] == 'A':
        a_q.append(i)
    elif s[i] == 'B':
        b_q.append(i)
    else:
        c_q.append(i)

# a_queue가 빌 때까지
while a_q:

  # pop (인덱스가 작은 순으로)
    a_idx = a_q.popleft()

    # a보다 뒤에있는 b를 모두 빼줌
    if b_q:
        if a_idx < b_q[0]:
            count += 1
            b_q.popleft()

    # b_q가 다 비었다면 종료
    else:
        break

# b_q가 빌 때까지
while b_q:

    b_idx = b_q.popleft()
    # c의 인덱스와 비교하여 모두 빼줌
    if c_q:
        if b_idx < c_q[0]:
            count += 1
            c_q.popleft()

print(count)
```