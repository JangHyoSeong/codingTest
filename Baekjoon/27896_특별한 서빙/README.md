# [27896] 특별한 서빙

### **난이도**
골드 5
## **📝문제**
???: 가지라니, 비슷하지도 않잖아요...

NLCS Jeju에서는 파묻튀(파마산을 묻혀 튀긴 소고기)를 서빙하는 것을 좋아한다.

그러나, 학생들은 파묻튀보다는 신선한 가지를 먹고 싶어한다!

급식실에 
$N$명의 학생들이 차례로 서 있다. 줄의 앞에서부터 
$i$번째 학생이 가지 대신 파묻튀를 받았을 경우 
$x_i$만큼 불만도가 늘어나고, 가지를 받았을 경우에는 
$x_i$만큼 불만도가 내려간다. 단, 불만도의 초깃값은 
$0$이다.

음식을 앞에 서있는 학생부터 순서대로 서빙할 때, 어떤 한 순간이라도 불만도가 
$M$ 이상이 되면 학생들은 ‘가지 운동’을 일으키게 된다.

가지 운동을 일으키지 않게 하기 위한 가지의 최소 개수를 구하는 프로그램을 작성하시오.
### **입력**
첫 번째 줄에 
$N$과 
$M$이 공백으로 구분되어 주어진다.

두 번째 줄에 
$x_i$를 나타내는 
$N$개의 정수가 공백으로 구분되어 주어진다.

 
- $1 \leq N \leq 200\,000$ 
 
- $1 \leq M \leq 10^9$ 
 
- $0 \leq x_i \leq 10^9$ 
### **출력**
첫 번째 줄에 학생들이 가지 운동을 일으키지 않게 하기 위한 가지의 최소 개수를 출력한다.
### **예제입출력**

**예제 입력1**

```
5 3
0 0 2 0 2
```

**예제 출력1**

```
1
```

**예제 입력2**

```
10 90
14 6 12 16 14 6 20 19 16 12
```

**예제 출력2**

```
2
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from  heapq import heappop, heappush

N, M = map(int, input().split())
arr = list(map(int, input().split()))

pq = []
upset = 0
count = 0
for i in range(N):
    heappush(pq, (-arr[i]))

    upset += arr[i]
    if upset >= M:
        if pq:
            num = -heappop(pq)
        upset -= num * 2
        count += 1

print(count)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|57228|208|Python3|329
#### **📝해설**

**알고리즘**
```
1. 우선순위 큐
```

### **다른 풀이**

```python
import heapq
import sys 
input = sys.stdin.readline

def sol(sum_, result, heap):
    _,M = map(int,input().split())
    for x in map(int,input().split()):
        heapq.heappush(heap,-x)
        sum_ += x
        if sum_ >= M:
            result += 1
            sum_ += 2*heapq.heappop(heap)    
    return result     

print(sol(0,0,[]))
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
ekqls5264|54428|172|Python3|340
#### **📝해설**

```python
from  heapq import heappop, heappush

# 입력받기
N, M = map(int, input().split())
arr = list(map(int, input().split()))

# 우선순위 큐 선언
pq = []
# 학생의 실시간 불만도
upset = 0

# 가지 횟수
count = 0

# 배열을 순회하면서
for i in range(N):
  
    # 일단 우선순위큐에 삽입. 가지를 먹었다고 가정
    heappush(pq, (-arr[i]))

    # 불만도 증가
    upset += arr[i]

    # 만약 불만도가 M을 넘었다면
    if upset >= M:
      # 우선순위 큐에서 기존 먹었던 가지중에 불만도가 가장 높았던것을 빼냄
        if pq:
            num = -heappop(pq)

        # 불만도를 원래대로 되돌림
        upset -= num * 2
        count += 1

print(count)
```