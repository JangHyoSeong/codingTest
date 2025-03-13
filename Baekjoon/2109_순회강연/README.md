# [2109] 순회강연

### **난이도**
골드 3
## **📝문제**
한 저명한 학자에게 n(0 ≤ n ≤ 10,000)개의 대학에서 강연 요청을 해 왔다. 각 대학에서는 d(1 ≤ d ≤ 10,000)일 안에 와서 강연을 해 주면 p(1 ≤ p ≤ 10,000)만큼의 강연료를 지불하겠다고 알려왔다. 각 대학에서 제시하는 d와 p값은 서로 다를 수도 있다. 이 학자는 이를 바탕으로, 가장 많은 돈을 벌 수 있도록 순회강연을 하려 한다. 강연의 특성상, 이 학자는 하루에 최대 한 곳에서만 강연을 할 수 있다.

예를 들어 네 대학에서 제시한 p값이 각각 50, 10, 20, 30이고, d값이 차례로 2, 1, 2, 1 이라고 하자. 이럴 때에는 첫째 날에 4번 대학에서 강연을 하고, 둘째 날에 1번 대학에서 강연을 하면 80만큼의 돈을 벌 수 있다.
### **입력**
첫째 줄에 정수 n이 주어진다. 다음 n개의 줄에는 각 대학에서 제시한 p값과 d값이 주어진다.
### **출력**
첫째 줄에 최대로 벌 수 있는 돈을 출력한다.
### **예제입출력**

**예제 입력1**

```
7
20 1
2 1
10 3
100 2
8 2
5 20
50 10
```

**예제 출력1**

```
185
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys
from heapq import heappop, heappush

N = int(sys.stdin.readline().rstrip())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

arr.sort(key= lambda x : x[1])

pq = []
for p, d in arr:
    heappush(pq, p)
    if len(pq) > d:
        heappop(pq)

print(sum(pq))
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|36532|56|Python3|300
#### **📝해설**

**알고리즘**
```
1. 그리디 알고리즘
2. 우선순위 큐
```

### **다른 풀이**

```python
import sys
input = sys.stdin.readline

def find_root(n, R):
    if R[n] != n:
        R[n] = find_root(R[n], R)
    return R[n]

def solve():
    n = int(input())
    proposals = sorted([tuple(map(int, input().split())) for _ in range(n)], reverse=True)
    R = [i for i in range(10001)]
    ans = 0
    for p, d in proposals:
        r = find_root(d, R)
        if r > 0:
            ans += p
            nxt = find_root(r - 1, R)
            R[r] = nxt
    print(ans)

solve()
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
tkqmfp26|32140|48|Python3|478
#### **📝해설**

```python
import sys
from heapq import heappop, heappush

# 입력받기
N = int(sys.stdin.readline().rstrip())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

# 마감 기한을 기준으로 정렬
arr.sort(key= lambda x : x[1])

# 최소힙 사용
pq = []

# 모든 강연을 검사하면서
for p, d in arr:

    # 우선순위 큐에 삽입
    heappush(pq, p)

    # 만약 이미 기한날짜가 지났다면 큐에서 제거
    if len(pq) > d:
        heappop(pq)

# 최대로 벌 수 있는 돈
print(sum(pq))
```