# [17352] 여러분의 다리가 되어드리겠습니다!

### **난이도**
골드 5
## **📝문제**
선린월드에는 N개의 섬이 있다. 섬에는 1, 2, ..., N의 번호가 하나씩 붙어 있다. 그 섬들을 N - 1개의 다리가 잇고 있으며, 어떤 두 섬 사이든 다리로 왕복할 수 있다.

어제까지는 그랬다.

"왜 다리가 N - 1개밖에 없냐, 통행하기 불편하다"며 선린월드에 불만을 갖던 욱제가 다리 하나를 무너뜨렸다! 안 그래도 불편한 통행이 더 불편해졌다. 서로 왕복할 수 없는 섬들이 생겼기 때문이다. 일단 급한 대로 정부는 선린월드의 건축가를 고용해, 서로 다른 두 섬을 다리로 이어서 다시 어떤 두 섬 사이든 왕복할 수 있게 하라는 지시를 내렸다.

그런데 그 건축가가 당신이다! 안 그래도 천하제일 코딩대회에 참가하느라 바쁜데...
### **입력**
첫 줄에 정수 N이 주어진다. (2 ≤ N ≤ 300,000)

그 다음 N - 2개의 줄에는 욱제가 무너뜨리지 않은 다리들이 잇는 두 섬의 번호가 주어진다.
### **출력**
다리로 이을 두 섬의 번호를 출력한다. 여러 가지 방법이 있을 경우 그 중 아무거나 한 방법만 출력한다.
### **예제입출력**

**예제 입력1**

```
4
1 2
1 3
```

**예제 출력1**

```
1 4
```

**예제 입력2**

```
2
```

**예제 출력2**

```
1 2
```

**예제 입력3**

```
5
1 2
2 3
4 5
```

**예제 출력3**

```
3 4
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

def union(x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)

    if root_x != root_y:
        if root_x < root_y:
            parent[root_y] = root_x
        
        else:
            parent[root_x] = root_y        

N = int(sys.stdin.readline().rstrip())

parent = list(range(N+1))

for _ in range(N-2):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    union(a, b)

root_set = set()
for i in range(1, N+1):
    root_set.add(find(parent, i))

print(" ".join(map(str, root_set)))
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|44992|576|Python3|635
#### **📝해설**

**알고리즘**
```
1. 유니온 파인드
```

### **다른 풀이**

```python
import io, os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
def main():
    N = int(input())
    parent = [*range(N + 1)]
    def find(x):
        while x != parent[x]:
            parent[x] = x = parent[parent[x]]
        return x
    for _ in range(N - 2):
        x, y = map(int, input().split())
        x, y = find(x), find(y)
        if x == y: continue
        if x < y: x, y = y, x
        parent[x] = y
    root = find(1)
    for i in range(2, N + 1):
        if find(i) != root:
            print(1, i)
            return
main()
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
minskai|121572|224|PyPy3|553
#### **📝해설**

```python
import sys

# 유니온파인드 루트노드 찾는 함수
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    
    return parent[x]

# 두 노드의 집합을 합치는 함수
def union(x, y):

    # 현재 루트노드를 찾음
    root_x = find(parent, x)
    root_y = find(parent, y)

    # 루트 노드가 다른 경우 합침
    if root_x != root_y:

        # 노드 번호가 작은게 우선이 되도록
        if root_x < root_y:
            parent[root_y] = root_x
        
        else:
            parent[root_x] = root_y        

N = int(sys.stdin.readline().rstrip())

# 부모노드를 저장할 리스트
parent = list(range(N+1))

# 간선을 입력하면서 집합을 합침
for _ in range(N-2):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    union(a, b)

# 두 집합으로 분리됐을 때, 두 집합에서 각각 하나의 노드씩을 꺼내서 이으면 모두 이어짐
root_set = set()

# 모든 노드의 루트노드를 찾고, 루트노드끼리 잇기
for i in range(1, N+1):
    root_set.add(find(parent, i))

print(" ".join(map(str, root_set)))
```