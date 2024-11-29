# [18513] 샘터

### **난이도**
골드 4
## **📝문제**
일직선 상의 공간에 N개의 샘터가 존재하며, K채의 집을 짓고자 한다. 모든 샘터 및 집이 존재하는 위치는 항상 정수 형태이다. 이때 일직선 상의 공간에서 N개의 샘터 및 K채의 집들은 모두 서로 다른 위치에 존재한다. 다시 말해 하나의 위치에는 샘터가 있거나, 집이 있거나, 혹은 아무것도 없다.

K채의 집을 지을 때, 가능하면 샘터의 주변에 집들을 지어서 K채의 모든 집에 대한 불행도의 합이 최소가 되도록 짓고자 한다. 이때 특정한 집에 대한 불행도란, 가장 가까운 샘터까지의 거리(Distance)로 정의된다. 예를 들어 특정한 집이 1에 위치하고, 그 집과 가장 가까운 샘터가 -5에 위치한다고 하면, 이 집의 불행도는 6이다.

N=2, K=5일 때, 모든 집에 대한 불행도의 합이 최소가 되도록 집을 짓는 경우를 고려해보자. 아래 그림과 같이 두 개의 샘터가 0, 3의 위치에 존재한다고 가정하자.



이때 다음과 같이 5채의 집을 설치하면, 각 집의 불행도의 합이 2+1+1+1+1=6로 최소가 된다. 집을 짓는 가능한 경우의 수는 여러 가지가 될 수 있지만, 불행도의 합을 6보다 작게 만드는 방법은 없다.


### **입력**
첫째 줄에 자연수 N과 K가 공백을 기준으로 구분되어 주어진다. (1 ≤ N, K ≤ 100,000) 둘째 줄에 N개의 샘터의 위치가 공백을 기준으로 구분되어 정수 형태로 주어진다. (-100,000,000 ≤ 샘터의 위치 ≤ 100,000,000) 단, 모든 N개의 샘터의 위치들은 서로 다르게 주어진다.
### **출력**
첫째 줄에 모든 집에 대한 불행도의 합의 최솟값을 출력한다.
### **예제입출력**

**예제 입력1**

```
2 5
0 3
```

**예제 출력1**

```
6
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from collections import deque

N, K = map(int, input().split())
ponds = list(map(int, input().split()))

visited = set(ponds)
q = deque()

for pond in ponds:
    q.append((pond, 0))

house_count = 0
total_unhappiness = 0

while house_count < K:
    current_pos, current_dist = q.popleft()

    for next_pos in [current_pos - 1, current_pos + 1]:
        if next_pos not in visited:
            visited.add(next_pos)
            total_unhappiness += current_dist + 1
            house_count += 1

            if house_count == K:
                break

            q.append((next_pos, current_dist + 1))

print(total_unhappiness)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|59224|244|Python3|628
#### **📝해설**

**알고리즘**
```
1. BFS
```

### **다른 풀이**

```python
n,k = map(int, input().split())
a = []
s = set()
for v in map(int, input().split()):
    s.add(v)
    a.append(v+1)

d = 2
ans = 0
while k:
    a = [v + 1 for v in a if not v in s]
    m = min(len(a), k)
    k -= m
    ans += d // 2 * m
    d += 1
print(ans)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
rootcucu|49964|160|Python3|259
#### **📝해설**

```python
from collections import deque

N, K = map(int, input().split())
ponds = list(map(int, input().split()))

# 방문위치를 set으로 저장
visited = set(ponds)
q = deque()

# q에 현재 연못의 위치, 연못까지 떨어진 거리를 삽입
for pond in ponds:
    q.append((pond, 0))


# 현재 지은 집, 총 불행도
house_count = 0
total_unhappiness = 0


# 집을 모두 지을 때까지 BFS
while house_count < K:

    # 현재 연못위치, 떨어진 거리를 q에서 pop
    current_pos, current_dist = q.popleft()

    # 현재 연못 기준으로 양옆으로 떨어진 거리 두개를 확인
    for next_pos in [current_pos - 1, current_pos + 1]:

      # 비어있는 장소라면
        if next_pos not in visited:

          # 집을 지음
            visited.add(next_pos)
            total_unhappiness += current_dist + 1
            house_count += 1

            if house_count == K:
                break
          
            q.append((next_pos, current_dist + 1))

print(total_unhappiness)
```