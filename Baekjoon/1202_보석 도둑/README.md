# [1202] 보석 도둑

### **난이도**
골드 2
## **📝문제**
세계적인 도둑 상덕이는 보석점을 털기로 결심했다.

상덕이가 털 보석점에는 보석이 총 N개 있다. 각 보석은 무게 Mi와 가격 Vi를 가지고 있다. 상덕이는 가방을 K개 가지고 있고, 각 가방에 담을 수 있는 최대 무게는 Ci이다. 가방에는 최대 한 개의 보석만 넣을 수 있다.

상덕이가 훔칠 수 있는 보석의 최대 가격을 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 N과 K가 주어진다. (1 ≤ N, K ≤ 300,000)

다음 N개 줄에는 각 보석의 정보 Mi와 Vi가 주어진다. (0 ≤ Mi, Vi ≤ 1,000,000)

다음 K개 줄에는 가방에 담을 수 있는 최대 무게 Ci가 주어진다. (1 ≤ Ci ≤ 100,000,000)

모든 숫자는 양의 정수이다.
### **출력**
첫째 줄에 상덕이가 훔칠 수 있는 보석 가격의 합의 최댓값을 출력한다.
### **예제입출력**

**예제 입력1**

```
2 1
5 10
100 100
11
```

**예제 출력1**

```
10
```

**예제 입력2**

```
3 2
1 65
5 23
2 99
10
2
```

**예제 출력2**

```
164
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from sys import stdin
from heapq import heappush, heappop

N, K = map(int, stdin.readline().rstrip().split())
jewels = [list(map(int, stdin.readline().rstrip().split())) for _ in range(N)]
bags = []
for _ in range(K):
    bags.append(int(stdin.readline().rstrip()))

bags.sort()
jewels.sort(key=lambda x : x[0])

pq = []
result = 0

jewel_idx = 0
for bag in bags:
    while jewel_idx < N:
        if bag >= jewels[jewel_idx][0]:
            heappush(pq, -jewels[jewel_idx][1])
            jewel_idx += 1
        else:
            break
    if pq:
        result -= heappop(pq)
    
print(result)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|188780|936|PyPy3|595
#### **📝해설**

**알고리즘**
```
1. 그리디 알고리즘
2. 우선순위 큐
```

#### **📝해설**

```python
from sys import stdin
from heapq import heappush, heappop

# 입력받기
N, K = map(int, stdin.readline().rstrip().split())
jewels = [list(map(int, stdin.readline().rstrip().split())) for _ in range(N)]
bags = []
for _ in range(K):
    bags.append(int(stdin.readline().rstrip()))

# 가방을 용량이 작은 순서대로 정렬
bags.sort()

# 보석을 무게가 작은 순서대로 정렬
jewels.sort(key=lambda x : x[0])

# 우선순위를 위한 리스트(힙)
pq = []

# 결과값 변수
result = 0

# 현재 몇 번째 보석인지 셀 인덱스
jewel_idx = 0

# 가방을 용량이 작은 순서부터 순회하면서
for bag in bags:

    # 보석의 인덱스를 넘기지 않을 때까지
    while jewel_idx < N:

        # 이번 가방에 담을 수 있는 보석이라면 우선순위큐에 담음(최대힙)
        if bag >= jewels[jewel_idx][0]:
            heappush(pq, -jewels[jewel_idx][1])
            jewel_idx += 1
        
        # 이번 가방에 담을 수 없다면 우선순위큐 push 종료
        else:
            break

    # 만약 우선순위 큐에 값이 보석이 있다면 pop
    # 가방에 담을 수 있는 보석 중에 가장 비싼 보석이 나옴
    if pq:
        result -= heappop(pq)
    
print(result)
```