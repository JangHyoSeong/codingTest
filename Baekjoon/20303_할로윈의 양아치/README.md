# [20303] 할로윈의 양아치

### **난이도**
골드 3
## **📝문제**
Trick or Treat!!

10월 31일 할로윈의 밤에는 거리의 여기저기서 아이들이 친구들과 모여 사탕을 받기 위해 돌아다닌다. 올해 할로윈에도 어김없이 많은 아이가 할로윈을 즐겼지만 단 한 사람, 일찍부터 잠에 빠진 스브러스는 할로윈 밤을 즐길 수가 없었다. 뒤늦게 일어나 사탕을 얻기 위해 혼자 돌아다녀 보지만 이미 사탕은 바닥나 하나도 얻을 수 없었다.

단단히 화가 난 스브러스는 거리를 돌아다니며 다른 아이들의 사탕을 빼앗기로 마음을 먹는다. 다른 아이들보다 몸집이 큰 스브러스에게 사탕을 빼앗는 건 어렵지 않다. 또한, 스브러스는 매우 공평한 사람이기 때문에 한 아이의 사탕을 뺏으면 그 아이 친구들의 사탕도 모조리 뺏어버린다. (친구의 친구는 친구다?!)

사탕을 빼앗긴 아이들은 거리에 주저앉아 울고 
$K$명 이상의 아이들이 울기 시작하면 울음소리가 공명하여 온 집의 어른들이 거리로 나온다. 스브러스가 어른들에게 들키지 않고 최대로 뺏을 수 있는 사탕의 양을 구하여라.

스브러스는 혼자 모든 집을 돌아다녔기 때문에 다른 아이들이 받은 사탕의 양을 모두 알고 있다. 또한, 모든 아이는 스브러스를 피해 갈 수 없다.
### **입력**
첫째 줄에 정수 
$N$, 
$M$, 
$K$가 주어진다. 
$N$은 거리에 있는 아이들의 수, 
$M$은 아이들의 친구 관계 수, 
$K$는 울음소리가 공명하기 위한 최소 아이의 수이다. (
$1 \leq N \leq 30\ 000$, 
$0 \leq M \leq 100\ 000$, 
$1 \leq K \leq \min\left\{N, 3\ 000\right\}$)

둘째 줄에는 아이들이 받은 사탕의 수를 나타내는 정수 
$c_1, c_2, \cdots, c_N$이 주어진다. (
$1 \leq c_i \leq 10\ 000$)

셋째 줄부터 
$M$개 줄에 갈쳐 각각의 줄에 정수 
$a$, 
$b$가 주어진다. 이는 
$a$와 
$b$가 친구임을 의미한다. 같은 친구 관계가 두 번 주어지는 경우는 없다. (
$1 \leq a, b \leq N$, 
$a \neq b$)
### **출력**
스브러스가 어른들에게 들키지 않고 아이들로부터 뺏을 수 있는 최대 사탕의 수를 출력한다.
### **예제입출력**

**예제 입력1**

```
10 6 6
9 15 4 4 1 5 19 14 20 5
1 3
2 5
4 9
6 2
7 8
6 10
```

**예제 출력1**

```
57
```

**예제 입력2**

```
5 4 4
9 9 9 9 9
1 2
2 3
3 4
4 5
```

**예제 출력2**

```
0
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)

    if root_x != root_y:
        if rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        elif rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

N, M, K = map(int, input().split())
candies = list(map(int, input().split()))

parent = [i for i in range(N)]
rank = [0] * N

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    union(parent, rank, a, b)

component = {}
for i in range(N):
    root = find(parent, i)
    if root not in component:
        component[root] = {'count': 0, 'candies': 0}
    component[root]['count'] += 1
    component[root]['candies'] += candies[i]

dp = [0] * K

for comp in component.values():
    count = comp['count']
    candy_sum = comp['candies']

    for j in range(K - 1, count - 1, -1):
        dp[j] = max(dp[j], dp[j - count] + candy_sum)

print(dp[K - 1])
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|122708|596|PyPy3|1137
#### **📝해설**

**알고리즘**
```
1. 유니온 파인드
2. DP
```

### **다른 풀이**

```python
import sys

def union(x,y):
    a, b = get(x), get(y)
    if a == b: return
    if a < b : a,b = b,a
    cnt[b] += cnt[a]
    c[b] += c[a]
    p[a] = b

def get(x):
    if p[x] !=x : 
        p[x] = get(p[x])
    return p[x]

input = lambda:map(int, sys.stdin.readline().split())
n, m, k = input()
c = [0]+ list(input())
p = [i for i in range(n+1)]
dp = [0 for i in range(k+1)]
cnt = [1 for i in range(n+1)]
dp[0] = 0

for i in range(m):
    a,b = input()
    union(a,b)

lst = []
for i in range(1,n+1):
    if p[i] == i:
        lst.append((cnt[i], c[i]))

lst.sort()

for c, cst in lst:
    for v in range(k-1, c-1, -1):
        dp[v] = max(dp[v], dp[v - c] + cst)

print(dp[k-1])
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
sunhong|114760|372|PyPy3|683
#### **📝해설**

```python
def find(parent, x):
    # 부모노드를 찾는 함수
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    # 두 집합을 합치는 함수
    root_x = find(parent, x)
    root_y = find(parent, y)

    if root_x != root_y:
        if rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        elif rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

N, M, K = map(int, input().split())
candies = list(map(int, input().split()))

# 각 인덱스의 부모 노드
parent = [i for i in range(N)]

# 자식 수
rank = [0] * N

# 입력받기
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    union(parent, rank, a, b)

# 각 요소별 사탕과 인원수를 저장
component = {}
for i in range(N):
    root = find(parent, i)
    if root not in component:
        component[root] = {'count': 0, 'candies': 0}
    component[root]['count'] += 1
    component[root]['candies'] += candies[i]

# DP배열. k명의 아이에서 받는 사탕의 수 최대값
dp = [0] * K

# 각 연결요소를 통해 DP 업데이트
for comp in component.values():
    count = comp['count']
    candy_sum = comp['candies']

    # 배낭문제를 위해 역순으로 DP갱신
    for j in range(K - 1, count - 1, -1):
        dp[j] = max(dp[j], dp[j - count] + candy_sum)

print(dp[K - 1])
```