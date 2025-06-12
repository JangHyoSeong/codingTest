# [24391] 귀찮은 해강이

### **난이도**
골드 5
## **📝문제**
해강이는 앙중대학교에 다닌다. 해강이는 이번 학기에 강의코드 1번부터 N번까지 N개의 강의를 듣고 있다.

모든 강의는 강의코드와 동일한 번호의 건물에서 진행된다. 예를 들어, 강의코드가 1인 강의는 1번 건물에서 진행되고, 강의코드가 N-1인 강의는 N-1번 건물에서 진행된다.

해강이는 밖에 나오는 것을 싫어해서, 강의 시간표 순서대로 모든 강의를 들으면서 한 건물에서 밖으로 나와서 다른 건물로 이동하는 횟수를 최소화하고 싶다. 앙중대학교에는 다행히도 서로 연결되어 있는 건물들이 있어, 이 건물끼리는 밖으로 나오지 않고 이동할 수 있다.

해강이의 강의 시간표가 주어질 때, 밖에 나오는 것을 싫어하는 해강이를 위해 최소 몇 번만 밖에 나오면 되는지 구해보자. 맨 처음 강의를 들으러 이동하는 횟수는 세지 않는다.
### **입력**
첫째 줄에 강의의 개수 N(1 ≤ N ≤ 105)과 연결되어 있는 건물의 쌍의 개수 M(0 ≤ M ≤ 105)이 공백으로 구분되어 주어진다.

두 번째 줄부터는 M줄에 걸쳐 i와 j(1 ≤ i, j ≤ N)가 주어진다. 이는 i번 건물과 j번 건물이 연결되어 있다는 의미이다. 건물이 자기 자신과 연결되거나, 이미 연결된 건물의 쌍이 다시 주어지는 경우는 없다.

마지막 줄에는 N개의 강의코드 Ai(1 ≤ Ai ≤ N)로 이루어진 강의 시간표가 공백으로 구분되어 주어진다.
### **출력**
해강이가 밖에 나와야 하는 최소 횟수를 출력한다.
### **예제입출력**

**예제 입력1**

```
5 3
1 3
2 5
3 4
1 2 3 5 4
```

**예제 출력1**

```
4
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)

    if root_x != root_y:
        if root_x < root_y:
            parent[root_y] = root_x
        else:
            parent[root_x] = root_y


N, M = map(int, sys.stdin.readline().rstrip().split())

parent = list(range(N+1))
for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    union(parent, a, b)

arr = list(map(int, sys.stdin.readline().rstrip().split()))

count = 0
now_node_top = find(parent, arr[0])
for i in range(1, N):
    next_node_top = find(parent, arr[i])
    if now_node_top != next_node_top:
        count += 1
        now_node_top = next_node_top

print(count)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|46516|268|Python3|809
#### **📝해설**

**알고리즘**
```
1. 유니온 파인드
```

### **다른 풀이**

```python
import sys
input = sys.stdin.readline
def solution():
  def find_par(x):
    if par[x] == x:
      return x
    par[x] = find_par(par[x])
    return par[x]

  def union(x, y):
    x, y = find_par(x), find_par(y)
    if x > y:
      par[x] = y
    else:
      par[y] = x

  N, M = map(int, input().split())
  par = [i for i in range(N + 1)]
  for _ in range(M):
    a, b = map(int, input().split())
    union(a, b)
  
  for i in range(1, N + 1):
    find_par(i)
  
  table = tuple(map(int, input().split()))
  result = 0
  for i in range(N - 1):
    if par[table[i]] != par[table[i + 1]]:
      result += 1
  
  print(result)

solution()
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
ssafy10go|45804|228|Python3|636
#### **📝해설**

```python
import sys

# 유니온파인드 부모 찾는 함수
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

# 두 노드를 합치는 함수
def union(parent, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)

    # 숫자가 작은 노드를 부모로 합침
    if root_x != root_y:
        if root_x < root_y:
            parent[root_y] = root_x
        else:
            parent[root_x] = root_y


N, M = map(int, sys.stdin.readline().rstrip().split())

parent = list(range(N+1))

# 입력받은 두 노드의 집합을 합침
for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    union(parent, a, b)

arr = list(map(int, sys.stdin.readline().rstrip().split()))

# 몇 번 이동해야하는지 저장할 변수
count = 0

# 시작 노드의 부모
now_node_top = find(parent, arr[0])

# 차례대로 강의실을 방문할 때
for i in range(1, N):

    # 부모가 다르다면 밖으로나가야함
    next_node_top = find(parent, arr[i])
    if now_node_top != next_node_top:
        count += 1
        now_node_top = next_node_top

print(count)
```