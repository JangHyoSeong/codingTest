# [9489] 사촌

### **난이도**
골드 4
## **📝문제**
증가하는 정수 수열을 이용해서 트리를 만드는 방법은 다음과 같다.

- 첫 번째 정수는 트리의 루트 노드이다.
- 다음에 등장하는 연속된 수의 집합은 루트의 자식을 나타낸다. 이 집합에 포함되는 수의 첫 번째 수는 항상 루트 노드+1보다 크다.
- 그 다음부터는 모든 연속된 수의 집합은 아직 자식이 없는 노드의 자식이 된다. 그러한 노드가 여러 가지 인 경우에는 가장 작은 수를 가지는 노드의 자식이 된다.
- 집합은 수가 연속하지 않는 곳에서 구분된다.

예를 들어, 수열 1 3 4 5 8 9 15 30 31 32를 위의 규칙을 이용해 트리를 만들면 아래 그림과 같이 된다.

![이미지](https://www.acmicpc.net/upload/images/cc.png)

두 노드의 부모는 다르지만, 두 부모가 형제(sibling)일 때 두 노드를 사촌이라고 한다.

수열 특정 노드 번호 k가 주어졌을 때, k의 사촌의 수를 구하는 프로그램을 작성하시오.
### **입력**
입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스의 첫째 줄에는 노드의 수 n과 사촌의 수를 구해야 하는 노드의 번호 k가 주어진다. (1 ≤ n ≤ 1,000, 1 ≤ k ≤ 1,000,000) 다음 줄에는 총 n개의 수가 주어지며, 모든 수는 1보다 크거나 같고, 1,000,000보다 작거나 같다. 입력으로 주어지는 수열은 항상 증가한다. k는 항상 수열에 포함되는 수이다.

입력의 마지막 줄에는 0이 두 개 주어진다.
### **출력**
각 테스트 케이스 마다, k의 사촌의 수를 출력한다.
### **예제입출력**

**예제 입력1**

```
10 15
1 3 4 5 8 9 15 30 31 32
12 9
3 5 6 8 9 10 13 15 16 22 23 25
10 4
1 3 4 5 8 9 15 30 31 32
0 0
```

**예제 출력1**

```
5
1
0
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys
from collections import deque

while True:
    n, k = map(int, sys.stdin.readline().rstrip().split())
    if n == 0 and k == 0:
        break

    arr = list(map(int, sys.stdin.readline().rstrip().split()))

    parent = {arr[0]: -1}
    nodes = deque()
    nodes.append(arr[0])

    idx = 1

    while idx < n:
        start_idx = idx

        while idx + 1 < n and arr[idx + 1] == arr[idx] + 1:
            idx += 1
        
        end_idx = idx

        parent_node = nodes.popleft()
        for i in range(start_idx, end_idx + 1):
            parent[arr[i]] = parent_node
            nodes.append((arr[i]))
        
        idx += 1
    
    if k not in parent:
        print(0)
        continue

    p = parent[k]
    if p == -1 or parent[p] == -1:
        print(0)
        continue

    grand = parent[p]
    cousins = 0
    for node, par in parent.items():
        if par != p and par != -1 and parent.get(par, -1) == grand:
            cousins += 1
    
    print(cousins)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|34976|1580|Python3|992
#### **📝해설**

**알고리즘**
```
1. 트리
```

### **다른 풀이**

```python
import sys
input = sys.stdin.readline

while True:
    N, K = map(int, input().split())            # 노드의 개수, 대상 노드

    if N == 0 and K == 0:
        break

    raw = [-1] + list(map(int, input().split()))
    
    par = [0] * (N + 1)
    par[0] = -1
    index = -1
    for i in range(1, N + 1):
        if raw[i] != raw[i - 1] + 1:
            index += 1

        par[i] = index                          # raw[i]의 부모를 저장한다.

    target = raw.index(K)
    ans = 0
    for i in range(1, N + 1):
        if par[i] != par[target] and par[par[i]] == par[par[target]]:
            ans += 1

    print(ans)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
bokchi|112912|348|PyPy3|634
#### **📝해설**

```python
import sys
from collections import deque

# 0, 0이 입력되기 전까지 계속 반복
while True:
    n, k = map(int, sys.stdin.readline().rstrip().split())
    if n == 0 and k == 0:
        break

    # 입력받기
    arr = list(map(int, sys.stdin.readline().rstrip().split()))

    # 부모가 어느 노드인지 저장할 딕셔너리
    # 루트노드는 -1 저장
    parent = {arr[0]: -1}

    # 현재 자식노드가 없는 노드들을 deque로 저장
    nodes = deque()
    nodes.append(arr[0])

    # 루트노드를 제외하고 확인
    idx = 1

    # 인덱스를 넘지 않을 때까지 반복
    while idx < n:

        # 연속된 숫자의 시작 인덱스
        start_idx = idx

        # 연속된 숫자가 어느 인덱스까지 있는지 확인
        while idx + 1 < n and arr[idx + 1] == arr[idx] + 1:
            idx += 1
        
        end_idx = idx

        # 이 집합을 자식이 없는 노드에 자식으로 삽입
        parent_node = nodes.popleft()
        for i in range(start_idx, end_idx + 1):
            parent[arr[i]] = parent_node

            # 새로 추가된 노드들은 자식이 없으므로 추가
            nodes.append((arr[i]))

        idx += 1
    
    # k가 수열에 포함되지 않는 경우 제외
    if k not in parent:
        print(0)
        continue
    
    # k의 부모를 찾았을 때, 본인, 혹은 부모가 루트노드라면 제외
    p = parent[k]
    if p == -1 or parent[p] == -1:
        print(0)
        continue
    
    # 두 세대 위의 노드를 확인
    grand = parent[p]
    cousins = 0

    # 모든 노드들을 확인하면서 두 세대 위의 부모가 같다면 사촌 수 추가
    for node, par in parent.items():
        if par != p and par != -1 and parent.get(par, -1) == grand:
            cousins += 1
    
    print(cousins)
```