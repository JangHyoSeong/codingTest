# [1781] 컵라면

### **난이도**
골드 2
## **📝문제**
상욱 조교는 동호에게 N개의 문제를 주고서, 각각의 문제를 풀었을 때 컵라면을 몇 개 줄 것인지 제시 하였다. 하지만 동호의 찌를듯한 자신감에 소심한 상욱 조교는 각각의 문제에 대해 데드라인을 정하였다.

문제 번호	1	2	3	4	5	6	7
데드라인	1	1	3	3	2	2	6
컵라면 수	6	7	2	1	4	5	1
위와 같은 상황에서 동호가 2, 6, 3, 1, 7, 5, 4 순으로 숙제를 한다면 2, 6, 3, 7번 문제를 시간 내에 풀어 총 15개의 컵라면을 받을 수 있다.

문제는 동호가 받을 수 있는 최대 컵라면 수를 구하는 것이다. 위의 예에서는 15가 최대이다.

문제를 푸는데는 단위 시간 1이 걸리며, 각 문제의 데드라인은 N이하의 자연수이다. 또, 각 문제를 풀 때 받을 수 있는 컵라면 수와 최대로 받을 수 있는 컵라면 수는 모두 231보다 작은 자연수이다.
### **입력**
첫 줄에 숙제의 개수 N (1 ≤ N ≤ 200,000)이 들어온다. 다음 줄부터 N+1번째 줄까지 i+1번째 줄에 i번째 문제에 대한 데드라인과 풀면 받을 수 있는 컵라면 수가 공백으로 구분되어 입력된다.
### **출력**
첫 줄에 동호가 받을 수 있는 최대 컵라면 수를 출력한다.
### **예제입출력**

**예제 입력1**

```
7
1 6
1 7
3 2
3 1
2 4
2 5
6 1
```

**예제 출력1**

```
15
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from heapq import heappush, heappop

N = int(input())
problems = [list(map(int, input().split())) for _ in range(N)]

problems.sort(key= lambda x : (x[0], -x[1]))

pq = []
day = 0

for problem in problems:
    heappush(pq, problem[1])
    day += 1

    if day > problem[0]:
        heappop(pq)
        day -= 1

print(sum(pq))
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|96028|5592|Python3|326
#### **📝해설**

**알고리즘**
```
1. 우선순위 큐
2. 그리디 알고리즘
```

### **다른 풀이**

```python
import sys
from heapq import heappush, heappop
input = sys.stdin.readline

def main():
    N = int(input())
    heap = []

    for i in range(N):
        dead, cup = map(int,input().split())
        heap.append((dead,cup))

    heap.sort(key = lambda x : x[0])
    solve = []
    day = 1

    for dead,cup in heap:
        if day <= dead:
            heappush(solve,cup)
            day += 1

        elif solve[0] < cup: 
            heappop(solve)
            heappush(solve,cup)
            
    print(sum(solve))
        
main()
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
uiuh5534|61052|284|Python3|532
#### **📝해설**

```python
from heapq import heappush, heappop

N = int(input())
problems = [list(map(int, input().split())) for _ in range(N)]

# 문제를 데드라인 순으로 오름차순정렬
problems.sort(key= lambda x : (x[0], -x[1]))

# 우선순위 큐를 위한 리스트 선언
pq = []
day = 0

# 문제를 순회하며
for problem in problems:

    # 일단 문제를 푼다고 가정
    heappush(pq, problem[1])
    day += 1

    # 이번 문제가 풀 수 없는 문제라면
    if day > problem[0]:

      # 이전에 푼 문제 중 가장 컵라면을 적게받는 문제를 풀지않음
        heappop(pq)
        day -= 1

# 힙에 남아있는 컵라면의 개수를 더함
print(sum(pq))
```