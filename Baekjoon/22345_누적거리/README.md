# [22345] 누적거리

### **난이도**
골드 2
## **📝문제**
KOI 나라는 수직선 위에 놓인 N개의 마을로 구성되어 있다. 이 중 i (1 ≤ i ≤ N)번째 마을은 xi 위치에 놓여 있으며 ai명이 거주 중이다. 또한 서로 다른 두 마을이 같은 위치에 놓인 경우는 없다.

KOI 나라는 모든 국민이 참여하는 모임을 개최하려고 한다. 모든 사람들이 모임 장소에 도착하기 위해 이동해야 하는 거리의 합을 누적 거리라고 부르고, 모임 장소가 x일 때의 누적 거리를 f(x)로 나타내자.

i번째 마을에 사는 사람이 x 위치에서 열리는 모임에 참가하기 위해서 이동해야 하는 거리는 |xi − x|이다. i번째 마을에는 ai명이 거주 중이므로 i번째 마을에 사는 사람들의 이동 거리의 합은 ai|xi − x|가 된다. 이 값을 모든 마을에 대해 합한 값이 모임 장소가 x일 때의 누적 거리가 될 것이다. 즉, f(x) = a1 × |x1 − x| + a2 × |x2 − x| + · · · + an × |xn − x|이다.

예를 들어 마을의 위치가 x1 = 1, x2 = 3, x3 = 6이고, 각 마을에 거주하는 사람들의 수가 a1 = 2, a2 = 1, a3 = 3이라고 하면, 모임 장소가 x = 4일 때의 누적 거리는 f(4) = 2 × |1 − 4| + 1 × |3 − 4| + 3 × |6 − 4| = 13 이다.

KOI 나라는 모임이 개최될 장소의 후보를 Q개 준비해 두었다. 이 때 j (1 ≤ j ≤ Q)번째 후보 장소의 위치는 qj이다. 이 때 서로 다른 두 후보 장소의 위치가 같은 경우는 없으나 마을의 위치와 후보 장소의 위치가 같을 수 있다. 각각의 후보 장소에 대해 누적 거리를 계산하는 프로그램을 작성하라.
### **입력**
첫 번째 줄에 N과 Q가 공백을 사이에 두고 차례로 주어진다.

다음 N개의 줄에는 마을에 대한 정보가 주어진다. 이 중 i (1 ≤ i ≤ N)번째 줄에는 ai와 xi가 공백을 사이에 두고 차례로 주어진다.

다음 Q개의 줄에는 모임 장소 후보에 대한 정보가 주어진다. 이 중 j (1 ≤ j ≤ Q)번째 줄에는 qj가 주어진다.
### **출력**
j (1 ≤ j ≤ Q)번째 줄에 모임 장소가 j번째 후보 모임 장소인 qj일 때의 누적 거리, 즉 f(qj)의 값을 출력한다.

### **제한**
- 1 ≤ N ≤ 200 000
- 모든 i (1 ≤ i ≤ N)에 대해, 1 ≤ ai ≤ 1 000
- 모든 i (1 ≤ i ≤ N)에 대해, −109 ≤ xi ≤ 109
- 1 ≤ Q ≤ 200 000
- 모든 j (1 ≤ j ≤ Q)에 대해, −109 ≤ qj ≤ 109
- 1 ≤ i1 < i2 ≤ N에 대해 xi1 ≠ xi2. 즉, 모든 마을의 위치는 서로 다르다.
- 1 ≤ j1 < j2 ≤ Q에 대해 qj1 ≠ qj2. 즉, 모든 후보 장소의 위치는 서로 다르다.
- 주어지는 모든 수는 정수이다.
### **예제입출력**

**예제 입력1**

```
3 1
2 1
1 3
3 6
4
```

**예제 출력1**

```
13
```

**예제 입력2**

```
4 5
3 -4
1 -10
2 11
4 6
6
-5
1
-12
14
```

**예제 출력2**

```
56
84
66
144
116
```
### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys
import bisect

N, Q = map(int, sys.stdin.readline().rstrip().split())
towns = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
queries = [int(sys.stdin.readline().rstrip()) for _ in range(Q)]

towns.sort(key=lambda x: x[1])
town_positions = [x for _, x in towns]

prefix_population = [0] * (N+1)
prefix_weighted_distance = [0] * (N+1)

for i in range(1, N+1):
    a, x = towns[i-1]
    prefix_population[i] = prefix_population[i-1] + a
    prefix_weighted_distance[i] = prefix_weighted_distance[i-1] + a*x

results = []
for q in queries:
    idx = bisect.bisect_left(town_positions, q)

    left_population = prefix_population[idx]
    left_distance = prefix_weighted_distance[idx]
    left_cost = left_population * q - left_distance

    right_population = prefix_population[N] - left_population
    right_distance = prefix_weighted_distance[N] - left_distance
    right_cost = right_distance - right_population * q

    results.append(left_cost + right_cost)

print("\n".join(map(str, results)))
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|162220|516|PyPy3|1033
#### **📝해설**

**알고리즘**
```
1. 누적합
2. 이분탐색
```

### **다른 풀이**

```python
import sys, bisect
input = sys.stdin.readline


n, q = map(int, input().split())
line = []
p = []
r = []
ps = [0]
prs = [0]
for i in range(n):
    a, b = map(int, input().split())
    line.append([a, b])
line.sort(key=lambda x: x[1])
for i in line:
    ps.append(ps[-1] + i[0])
    prs.append(prs[-1] + i[0] * i[1])
    p.append(i[0])
    r.append(i[1])
for i in range(q):
    c = int(input())
    d = bisect.bisect_left(r, c)
    print(ps[d] * c - prs[d] + (prs[-1] - prs[d]) - (ps[-1] - ps[d]) * c)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
quartz_ore|204700|844|PyPy3|501
#### **📝해설**

```python
import sys
import bisect

# 입력받기
N, Q = map(int, sys.stdin.readline().rstrip().split())
towns = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
queries = [int(sys.stdin.readline().rstrip()) for _ in range(Q)]

# 거리를 기준으로 정렬
towns.sort(key=lambda x: x[1])

# 이분탐색에 사용할 위치 좌표
town_positions = [x for _, x in towns]

# 누적합 배열
prefix_population = [0] * (N+1) # 인구 누적 합
prefix_weighted_distance = [0] * (N+1) # (인구 * 거리) 누적 합

# 누적합 계산
for i in range(1, N+1):
    a, x = towns[i-1]
    prefix_population[i] = prefix_population[i-1] + a
    prefix_weighted_distance[i] = prefix_weighted_distance[i-1] + a*x

# 결과 출력을 위한 배열
results = []

# 주어진 위치에 대해 순회
for q in queries:

    # 이진탐색을 통해 후보 위치를 찾음
    idx = bisect.bisect_left(town_positions, q)

    # 후보위치를 기준으로 왼쪽의 누적 합
    left_population = prefix_population[idx]
    left_distance = prefix_weighted_distance[idx]
    left_cost = left_population * q - left_distance # 모든 왼쪽 마을의 이동 비용

    # 오른쪽 누적 합
    right_population = prefix_population[N] - left_population
    right_distance = prefix_weighted_distance[N] - left_distance
    right_cost = right_distance - right_population * q # 모든 오른쪽 마을의 이동 비용

    # 총 비용
    results.append(left_cost + right_cost)

print("\n".join(map(str, results)))
```