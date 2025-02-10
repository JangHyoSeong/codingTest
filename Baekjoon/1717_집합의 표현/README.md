# [1717] 집합의 표현

### **난이도**
골드 5
## **📝문제**
초기에 
$n+1$개의 집합 
$\{0\}, \{1\}, \{2\}, \dots , \{n\}$이 있다. 여기에 합집합 연산과, 두 원소가 같은 집합에 포함되어 있는지를 확인하는 연산을 수행하려고 한다.

집합을 표현하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 $n$, $m$이 주어진다. $m$은 입력으로 주어지는 연산의 개수이다. 다음 $m$개의 줄에는 각각의 연산이 주어진다. 합집합은 $0$ $a$ $b$의 형태로 입력이 주어진다. 이는 $a$가 포함되어 있는 집합과, $b$가 포함되어 있는 집합을 합친다는 의미이다. 두 원소가 같은 집합에 포함되어 있는지를 확인하는 연산은 $1$ $a$ $b$의 형태로 입력이 주어진다. 이는 $a$와 $b$가 같은 집합에 포함되어 있는지를 확인하는 연산이다.
### **출력**
1로 시작하는 입력에 대해서 
$a$와 
$b$가 같은 집합에 포함되어 있으면 "YES" 또는 "yes"를, 그렇지 않다면 "NO" 또는 "no"를 한 줄에 하나씩 출력한다.
### **예제입출력**

**예제 입력1**

```
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1
```

**예제 출력1**

```
NO
NO
YES
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

N, M = map(int, sys.stdin.readline().rstrip().split())

parent = list(range(N+1))
rank = [1] * (N+1)
for _ in range(M):
    operator, a, b = map(int, sys.stdin.readline().rstrip().split())

    if operator == 0:
        union(parent, rank, a, b)
    else:
        if find(parent, a) == find(parent, b):
            print("YES")
        else:
            print("NO")
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|128612|252|PyPy3|837
#### **📝해설**

**알고리즘**
```
1. 유니온 파인드
```
#### **📝해설**

```python
import sys

# 부모를 찾는 함수
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

# 두 집합을 합치는 함수 
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

N, M = map(int, sys.stdin.readline().rstrip().split())

parent = list(range(N+1))
rank = [1] * (N+1)
for _ in range(M):
    operator, a, b = map(int, sys.stdin.readline().rstrip().split())

    if operator == 0:
        union(parent, rank, a, b)
    else:
        if find(parent, a) == find(parent, b):
            print("YES")
        else:
            print("NO")
```

### **🔖정리**

1. 배운점