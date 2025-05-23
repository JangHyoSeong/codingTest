# [13334] 철로

### **난이도**
골드 2
## **📝문제**
집과 사무실을 통근하는 n명의 사람들이 있다. 각 사람의 집과 사무실은 수평선 상에 있는 서로 다른 점에 위치하고 있다. 임의의 두 사람 A, B에 대하여, A의 집 혹은 사무실의 위치가 B의 집 혹은 사무실의 위치와 같을 수 있다. 통근을 하는 사람들의 편의를 위하여 일직선 상의 어떤 두 점을 잇는 철로를 건설하여, 기차를 운행하려고 한다. 제한된 예산 때문에, 철로의 길이는 d로 정해져 있다. 집과 사무실의 위치 모두 철로 선분에 포함되는 사람들의 수가 최대가 되도록, 철로 선분을 정하고자 한다.

양의 정수 d와 n 개의 정수쌍, (hi, oi), 1 ≤ i ≤ n,이 주어져 있다. 여기서 hi와 oi는 사람 i의 집과 사무실의 위치이다. 길이 d의 모든 선분 L에 대하여, 집과 사무실의 위치가 모두 L에 포함되는 사람들의 최대 수를 구하는 프로그램을 작성하시오.

[이미지](https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/13334/1.png)

그림 1. 8 명의 집과 사무실의 위치

그림 1 에 있는 예를 고려해보자. 여기서 n = 8, (h1, o1) = (5, 40), (h2, o2) = (35, 25), (h3, o3) = (10, 20), (h4, o4) = (10, 25), (h5, o5) = (30, 50), (h6, o6) = (50, 60), (h7, o7) = (30, 25), (h8, o8) = (80, 100)이고, d = 30이다. 이 예에서, 위치 10 과 40 사이의 빨간색 선분 L이, 가장 많은 사람들에 대하여 집과 사무실 위치 모두 포함되는 선분 중 하나이다. 따라서 답은 4 이다.
### **입력**
입력은 표준입력을 사용한다. 첫 번째 줄에 사람 수를 나타내는 양의 정수 n (1 ≤ n ≤ 100,000)이 주어진다. 다음 n개의 각 줄에 정수 쌍 (hi, oi)가 주어진다. 여기서 hi와 oi는 −100,000,000이상, 100,000,000이하의 서로 다른 정수이다. 마지막 줄에, 철로의 길이를 나타내는 정수 d (1 ≤ d ≤ 200,000,000)가 주어진다.
### **출력**
출력은 표준출력을 사용한다. 길이 d의 임의의 선분에 대하여, 집과 사무실 위치가 모두 그 선분에 포함되는 사람들의 최대 수를 한 줄에 출력한다. 
### **예제입출력**

**예제 입력1**

```
8
5 40
35 25
10 20
10 25
30 50
50 60
30 25
80 100
30
```

**예제 출력1**

```
4
```

**예제 입력2**

```
4
20 80
70 30
35 65
40 60
10
```

**예제 출력2**

```
0
```

**예제 입력3**

```
5
-5 5
30 40
-5 5
50 40
5 -5
10
```

**예제 출력3**

```
3
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys
from heapq import heappush, heappop

N = int(sys.stdin.readline().rstrip())
sections = []
for _ in range(N):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    sections.append((min(a, b), max(a, b)))

D = int(sys.stdin.readline().rstrip())

sections = [s for s in sections if s[1] - s[0] <= D]
sections.sort(key=lambda x: x[1])

count = 0
pq = []
for start, end in sections:
    while pq and pq[0] < end - D:
        heappop(pq)
    heappush(pq, start)
    count = max(count, len(pq))

print(count)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|123492|264|PyPy3|521
#### **📝해설**

**알고리즘**
```
1. 우선순위 큐
2. 정렬
```

### **다른 풀이**

```python
import sys, gc; gc.disable()
lines = sys.stdin.buffer.readlines()

d = int(lines[-1])*2

A = []
append = A.append

for i in range(1, len(lines)-1):
    x, y = lines[i].split()
    if (x := 2*int(x)) > (y := 2*int(y)):
        if (x := x-d) <= y: append(x); append(y+1)
    elif (y := y-d) <= x: append(y); append(x+1)

A.sort()

x = 0
print(max(((x := (x-1) if v%2 else (x+1)) for v in A), default=0))
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
jiminp|46872|196|Python3|402
#### **📝해설**

```python
import sys
from heapq import heappush, heappop

N = int(sys.stdin.readline().rstrip())
sections = []
# 시작점, 끝점 순으로 입력받음
for _ in range(N):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    sections.append((min(a, b), max(a, b)))

D = int(sys.stdin.readline().rstrip())

# 이미 구간의 길이가 D보다 크다면 포함될수 없으니 제외
sections = [s for s in sections if s[1] - s[0] <= D]

# 끝점 기준으로 정렬
sections.sort(key=lambda x: x[1])

count = 0
# 최소힙 사용을 위한 우선순위 큐
pq = []

# 끝점이 작은 순서대로 확인
for start, end in sections:
    # 힙에 값이 있고, top의 시작점이 현재 끝점 기준으로 포함되지 못한다면 힙에서 제거
    while pq and pq[0] < end - D:
        heappop(pq)
    
    # 현재 종료지점을 기준으로 삼고 힙에 push
    heappush(pq, start)
    # 현재 선분에 포함되어 있는 구간 = len(pq). 최대값을 갱신함
    count = max(count, len(pq))

print(count)
```