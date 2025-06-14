# [15903] 카드 합체 놀이

### **난이도**
실버 1
## **📝문제**
석환이는 아기다. 아기 석환이는 자연수가 쓰여져있는 카드를 갖고 다양한 놀이를 하며 노는 것을 좋아한다. 오늘 아기 석환이는 무슨 놀이를 하고 있을까? 바로 카드 합체 놀이이다!

아기 석환이는 자연수가 쓰여진 카드를 n장 갖고 있다. 처음에 i번 카드엔 ai가 쓰여있다. 카드 합체 놀이는 이 카드들을 합체하며 노는 놀이이다. 카드 합체는 다음과 같은 과정으로 이루어진다.

1. x번 카드와 y번 카드를 골라 그 두 장에 쓰여진 수를 더한 값을 계산한다. (x ≠ y)
2. 계산한 값을 x번 카드와 y번 카드 두 장 모두에 덮어 쓴다.
이 카드 합체를 총 m번 하면 놀이가 끝난다. m번의 합체를 모두 끝낸 뒤, n장의 카드에 쓰여있는 수를 모두 더한 값이 이 놀이의 점수가 된다. 이 점수를 가장 작게 만드는 것이 놀이의 목표이다.

아기 석환이는 수학을 좋아하긴 하지만, 아직 아기이기 때문에 점수를 얼마나 작게 만들 수 있는지를 알 수는 없었다(어른 석환이는 당연히 쉽게 알 수 있다). 그래서 문제 해결 능력이 뛰어난 여러분에게 도움을 요청했다. 만들 수 있는 가장 작은 점수를 계산하는 프로그램을 만들어보자.
### **입력**
첫 번째 줄에 카드의 개수를 나타내는 수 n(2 ≤ n ≤ 1,000)과 카드 합체를 몇 번 하는지를 나타내는 수 m(0 ≤ m ≤ 15×n)이 주어진다.

두 번째 줄에 맨 처음 카드의 상태를 나타내는 n개의 자연수 a1, a2, …, an이 공백으로 구분되어 주어진다. (1 ≤ ai ≤ 1,000,000)
### **출력**
첫 번째 줄에 만들 수 있는 가장 작은 점수를 출력한다.
### **예제입출력**

**예제 입력1**

```
3 1
3 2 6
```

**예제 출력1**

```
16
```

**예제 입력2**

```
4 2
4 2 3 1
```

**예제 출력2**

```
19
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys
from heapq import heappush, heappop

N, M = map(int, sys.stdin.readline().rstrip().split())
cards = list(map(int, sys.stdin.readline().rstrip().split()))

pq = []
for card in cards:
    heappush(pq, card)

for i in range(M):
    a, b = heappop(pq), heappop(pq)
    card_sum = a + b
    heappush(pq, card_sum)
    heappush(pq, card_sum)

print(sum(pq))
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|35508|56|Python3|362
#### **📝해설**

**알고리즘**
```
1. 우선순위 큐
```

### **다른 풀이**

```python
from heapq import heapify, heappop, heappush

n, m = map(int, input().split())
c = [*map(int, input().split())]
heapify(c)

for _ in range(m):
    x = heappop(c)+heappop(c)
    heappush(c, x); heappush(c, x)

print(sum(c))
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
mhc|33188|44|Python3|222
#### **📝해설**

```python
import sys
from heapq import heappush, heappop

# 입력받기
N, M = map(int, sys.stdin.readline().rstrip().split())
cards = list(map(int, sys.stdin.readline().rstrip().split()))

# 초기 카드 값을 모두 우선순위 큐에 삽입
pq = []
for card in cards:
    heappush(pq, card)

# M번 반복하면서
for i in range(M):
    # 가장 작은 수 두개를 pop
    a, b = heappop(pq), heappop(pq)

    # 그 두 수를 더한 뒤 다시 우선순위 큐에 삽입
    card_sum = a + b
    heappush(pq, card_sum)
    heappush(pq, card_sum)

    # 이 과정을 통해 항상 가장 작은 카드만이 더해짐

print(sum(pq))
```