# [1966] 프린터 큐

### **난이도**
실버 3
## **📝문제**
여러분도 알다시피 여러분의 프린터 기기는 여러분이 인쇄하고자 하는 문서를 인쇄 명령을 받은 ‘순서대로’, 즉 먼저 요청된 것을 먼저 인쇄한다. 여러 개의 문서가 쌓인다면 Queue 자료구조에 쌓여서 FIFO - First In First Out - 에 따라 인쇄가 되게 된다. 하지만 상근이는 새로운 프린터기 내부 소프트웨어를 개발하였는데, 이 프린터기는 다음과 같은 조건에 따라 인쇄를 하게 된다.

1. 현재 Queue의 가장 앞에 있는 문서의 ‘중요도’를 확인한다.
2. 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치 한다. 그렇지 않다면 바로 인쇄를 한다.

예를 들어 Queue에 4개의 문서(A B C D)가 있고, 중요도가 2 1 4 3 라면 C를 인쇄하고, 다음으로 D를 인쇄하고 A, B를 인쇄하게 된다.

여러분이 할 일은, 현재 Queue에 있는 문서의 수와 중요도가 주어졌을 때, 어떤 한 문서가 몇 번째로 인쇄되는지 알아내는 것이다. 예를 들어 위의 예에서 C문서는 1번째로, A문서는 3번째로 인쇄되게 된다.
### **입력**
첫 줄에 테스트케이스의 수가 주어진다. 각 테스트케이스는 두 줄로 이루어져 있다.

테스트케이스의 첫 번째 줄에는 문서의 개수 N(1 ≤ N ≤ 100)과, 몇 번째로 인쇄되었는지 궁금한 문서가 현재 Queue에서 몇 번째에 놓여 있는지를 나타내는 정수 M(0 ≤ M < N)이 주어진다. 이때 맨 왼쪽은 0번째라고 하자. 두 번째 줄에는 N개 문서의 중요도가 차례대로 주어진다. 중요도는 1 이상 9 이하의 정수이고, 중요도가 같은 문서가 여러 개 있을 수도 있다.
### **출력**
각 테스트 케이스에 대해 문서가 몇 번째로 인쇄되는지 출력한다.
### **예제입출력**

**예제 입력1**

```
3
1 0
5
4 2
1 2 3 4
6 0
1 1 9 1 1 1
```

**예제 출력1**

```
1
2
5
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from collections import deque

T = int(input())

for testcase in range(T):
    N, M = map(int, input().split())
    priorities = list(map(int, input().split()))
    q = deque((priority, idx) for idx, priority in enumerate(priorities))

    count = 0
    while q:
        cur = q.popleft()
        if any(cur[0] < other[0] for other in q):
            q.append(cur)
        else:
            count += 1
            if cur[1] == M:
                print(count)
                break
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|34908|64|Python3|480
#### **📝해설**

**알고리즘**
```
1. 큐
```

### **다른 풀이**

```python
import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    val = list(map(int, input().split()))
    arr = [(i, val[i]) for i in range(n)]
    val.sort(reverse=True)

    i = 0
    count = 0

    while True:
        if arr[i][1] == val[count]:
            if arr[i][0] == m:
                print(count + 1)
                break
            count += 1

        else:
            arr.append((arr[i]))

        i += 1

```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
jhhh222|31120|32|Python3|477
#### **📝해설**

```python
from collections import deque

T = int(input())

for testcase in range(T):
    N, M = map(int, input().split())
    priorities = list(map(int, input().split()))

    # 큐에 우선순위와 인덱스를 같이 저장
    q = deque((priority, idx) for idx, priority in enumerate(priorities))

    count = 0
    while q:
        cur = q.popleft()

        # 뒤에 우선순위가 더 큰게 있다면 큐 맨 뒤에 삽입
        if any(cur[0] < other[0] for other in q):
            q.append(cur)

        # 우선순위가 큰게 없다면 count를 늘리고 빼냄
        else:
            count += 1
            if cur[1] == M:
                print(count)
                break
```