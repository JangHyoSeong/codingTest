# [16562] 친구비

### **난이도**
골드 4
## **📝문제**
19학번 이준석은 학생이 N명인 학교에 입학을 했다. 준석이는 입학을 맞아 모든 학생과 친구가 되고 싶어한다. 하지만 준석이는 평생 컴퓨터랑만 대화를 하며 살아왔기 때문에 사람과 말을 하는 법을 모른다. 그런 준석이에게도 희망이 있다. 바로 친구비다!

학생 i에게 Ai만큼의 돈을 주면 그 학생은 1달간 친구가 되어준다! 준석이에게는 총 k원의 돈이 있고 그 돈을 이용해서 친구를 사귀기로 했다. 막상 친구를 사귀다 보면 돈이 부족해질 것 같다는 생각을 하게 되었다. 그래서 준석이는 “친구의 친구는 친구다”를 이용하기로 했다.

준석이는 이제 모든 친구에게 돈을 주지 않아도 된다!

위와 같은 논리를 사용했을 때, 가장 적은 비용으로 모든 사람과 친구가 되는 방법을 구하라.
### **입력**
첫 줄에 학생 수 N (1 ≤ N ≤ 10,000)과 친구관계 수 M (0 ≤ M ≤ 10,000), 가지고 있는 돈 k (1 ≤ k ≤ 10,000,000)가 주어진다.

두번째 줄에 N개의 각각의 학생이 원하는 친구비 Ai가 주어진다. (1 ≤ Ai ≤ 10,000, 1 ≤ i ≤ N)

다음 M개의 줄에는 숫자 v, w가 주어진다. 이것은 학생 v와 학생 w가 서로 친구라는 뜻이다. 자기 자신과 친구일 수도 있고, 같은 친구 관계가 여러 번 주어질 수도 있다.
### **출력**
준석이가 모든 학생을 친구로 만들 수 있다면, 친구로 만드는데 드는 최소비용을 출력한다. 만약 친구를 다 사귈 수 없다면, “Oh no”(따옴표 제거)를 출력한다.
### **예제입출력**

**예제 입력1**

```
5 3 20
10 10 20 20 30
1 3
2 4
5 4
```

**예제 출력1**

```
20
```

**예제 입력2**

```
5 3 10
10 10 20 20 30
1 3
2 4
5 4
```

**예제 출력2**

```
Oh no
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
    rootX = find(parent, x)
    rootY = find(parent, y)

    if rootX != rootY:
        if rank[rootX] > rank[rootY]:
            parent[rootY] = rootX
        elif rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        else:
            parent[rootY] = rootX
            rank[rootX] += 1

N, M, k = map(int, input().split())
money = list(map(int, input().split()))
edges = [list(map(int, input().split())) for _ in range(M)]

parent = [i for i in range(N)]
rank = [0] * N

for v, w in edges:
    union(parent, rank, v-1, w-1)

root_min_cost = {}
for i in range(N):
    root = find(parent, i)
    if root not in root_min_cost:
        root_min_cost[root] = money[i]
    else:
        root_min_cost[root] = min(root_min_cost[root], money[i])

total_cost = sum(root_min_cost.values())

print(total_cost if total_cost <= k else "Oh no")
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|33164|304|Python3|989
#### **📝해설**

**알고리즘**
```
1. 유니온 파인드
```

#### **📝해설**

```python
def find(parent, x):
    # 분리집합의 부모를 찾는 함수
    if parent[x] != x:
        parent[x] = find(parent, parent[x])

    return parent[x]

def union(parent, rank, x, y):
    # 두 분리집합을 합치는 과정

    # 각 노드의 최상단 노드를 찾음
    rootX = find(parent, x)
    rootY = find(parent, y)

    # 두 노드의 부모가 같지 않다면 합침
    if rootX != rootY:

        # 랭크를 기준으로 합침
        if rank[rootX] > rank[rootY]:
            parent[rootY] = rootX
        elif rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        else:
            parent[rootY] = rootX
            rank[rootX] += 1

N, M, k = map(int, input().split())
money = list(map(int, input().split()))
edges = [list(map(int, input().split())) for _ in range(M)]

# 부모 노드 정보
parent = [i for i in range(N)]

# 각 노드의 랭크
rank = [0] * N

# 간선을 모두 합침
for v, w in edges:
    union(parent, rank, v-1, w-1)

# 각 노드의 최소값을 저장할 딕셔너리
root_min_cost = {}

# 모든 노드를 검사하면서
for i in range(N):
    root = find(parent, i)

    # 아직 정보가 저장되지 않은 노드라면 저장
    if root not in root_min_cost:
        root_min_cost[root] = money[i]

    # 정보가 저장되어있는 노드라면 최소값을 갱신
    else:
        root_min_cost[root] = min(root_min_cost[root], money[i])

# 모든 값을 더함
total_cost = sum(root_min_cost.values())

# 출력
print(total_cost if total_cost <= k else "Oh no")
```