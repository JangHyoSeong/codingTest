# [19640] 화장실의 규칙

### **난이도**
골드 4
## **📝문제**
데카는 회사의 화장실을 이용하려고 했다. 하지만 수도 시설 고장으로 회사 내의 모든 화장실 사용이 금지됐고, 사원들은 단 하나의 임시 화장실을 이용해야 했다. 

임시 화장실의 앞에 데카를 포함한 N명의 사원이 대기하고 있다. 데카는 N명의 줄에서 K + 1번째로 줄을 섰다. 즉, 데카보다 먼저 도착한 사람이 K명이 있다. 줄이 길어지자 사장은 M개의 줄로 나눠서 대기하라 하였다.

N명의 사원은 순서대로 M개의 줄로 나눠 섰다. 기존 줄의 1번째 사원은 1번째 줄에, 2번째 사원은 2번째 줄에, ... M번째 사원은 M번째 줄에, 그리고 M + 1번째 사원은 1번째 줄의 뒤에 서는 방식이다. 

M개의 줄로 나눠 선 것을 본 사장은 매우 흡족해하며 자리를 떠났다.

M개의 줄의 사원들은 암묵적으로 다음의 규칙에 따라 화장실을 이용하기로 하였다.

- 선두란, 어떤 줄에서 가장 먼저 와서, 가장 앞에 선 사람을 말한다.
- M개의 줄의 선두 중 근무 일수 Di가 가장 높은 선두가 화장실을 이용한다.
- M개의 줄의 선두 중 근무 일수 Di가 가장 높은 선두가 둘 이상인 경우, 해당 선두들 중 화장실이 급한 정도 Hi가 가장 높은 선두가 화장실을 이용한다.
- M개의 줄의 선두 중 근무 일수 Di가 가장 높은 선두가 둘 이상이며, 해당 선두들의 화장실이 급한 정도 Hi도 모두 같다면, 해당 선두 중 줄의 번호가 가장 낮은 줄에 선 선두가 화장실을 이용한다.  
과연 몇 명의 사원이 화장실을 이용하고 나서야 데카의 차례가 올까? 매우 초조해지기 시작한 데카를 대신해 계산해주자.
### **입력**
첫 번째 줄에는 임시 화장실에 대기하고 있는 사원의 수 N (1 ≤ N ≤ 105), 사장이 지시한 새로운 줄의 수 M (2 ≤ M ≤ 105), 데카가 화장실에 도착했을 때 자신의 앞에 서 있던 사원의 수 K (0 ≤ K ≤ N − 1)가 빈칸을 사이에 두고 주어진다.

두 번째 줄부터 각 N개의 줄에 임시 화장실에 i번째로 줄을 섰던 사원의 근무 일수 Di (0 ≤ Di ≤ 36,500), 화장실이 급한 정도를 나타내는 정수 Hi (0 ≤ Hi ≤ 108)가 가장 먼저 도착한 사원부터 빈칸을 사이에 두고 주어진다.
### **출력**
데카가 화장실을 이용하기까지 몇 명의 사원이 화장실을 이용할 것인지 출력한다.
### **예제입출력**

**예제 입력1**

```
6 3 2
3000 100
1500 200
1000 500
1500 100
1500 100
1500 100
```

**예제 출력1**

```
4
```

**예제 입력2**

```
1 2 0
100 100
```

**예제 출력2**

```
0
```

**예제 입력3**

```
3 10 2
450 1000
450 500
450 1000
```

**예제 출력3**

```
1
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys
from heapq import heappop, heappush
from collections import deque

N, M, K = map(int, input().split())

# 각 줄을 나타내는 큐 생성
lines = [deque() for _ in range(M)]
for i in range(N):
    d, h = map(int, sys.stdin.readline().rstrip().split())
    lines[i % M].append((d, h, i))

# 힙 초기화
heap = []
for i in range(M):
    if lines[i]:
        d, h, idx = lines[i].popleft()
        heappush(heap, (-d, -h, i, idx))  # (근무일수, 화장실 급함 정도, 줄 번호, 원래 인덱스)

count = 0
while heap:
    d, h, line_idx, idx = heappop(heap)

    # 데카의 차례인지 확인
    if idx == K:
        break

    # 현재 줄에서 다음 사람을 힙에 추가
    if lines[line_idx]:
        d, h, idx = lines[line_idx].popleft()
        heappush(heap, (-d, -h, line_idx, idx))
    
    count += 1

print(count)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|205628|532|PyPy3|854
#### **📝해설**

**알고리즘**
```
1. 우선순위 큐
2. 큐
```
### **다른 풀이**

```python
import sys
import heapq
input = sys.stdin.readline

n,m,k = map(int,input().split())

m = min(n,m)

employees = []

for i in range(n):
    Di,Hi = map(int,input().split())
    employees.append((Di,Hi,i%m,i))

line_shell = [0]*m # 현재 줄이 몇번째 껍질인지 알기 위함.

heap = []

for i in range(m):
    Di = employees[i][0]
    Hi = employees[i][1]
    line_num = employees[i][2]
    index = employees[i][3]
    heapq.heappush(heap,(-Di,-Hi,line_num,index))
turn = 0
while(heap):
    employee = heapq.heappop(heap)
    index = employee[3]
    if index == k:
        break
    turn += 1
    if index+m<len(employees):
        next_employ = employees[index+m]
        heapq.heappush(heap,(-next_employ[0],-next_employ[1],next_employ[2],index+m))

print(turn)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
chlghksdud24|70072|408|Python3|770
