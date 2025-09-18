# [14267] 회사 문화 1

### **난이도**
골드 4
## **📝문제**
영선회사에는 매우 좋은 문화가 있는데, 바로 상사가 직속 부하를 칭찬하면 그 부하가 부하의 직속 부하를 연쇄적으로 칭찬하는 내리 칭찬이 있다. 즉, 상사가 한 직속 부하를 칭찬하면 그 부하의 모든 부하들이 칭찬을 받는다.

모든 칭찬에는 칭찬의 정도를 의미하는 수치가 있는데, 이 수치 또한 부하들에게 똑같이 칭찬 받는다.

직속 상사와 직속 부하관계에 대해 주어지고, 칭찬에 대한 정보가 주어질 때, 각자 얼마의 칭찬을 받았는지 출력하시오,
### **입력**
첫째 줄에는 회사의 직원 수 n명, 최초의 칭찬의 횟수 m이 주어진다. 직원은 1번부터 n번까지 번호가 매겨져 있다. (2 ≤ n, m ≤ 100,000)

둘째 줄에는 직원 n명의 직속 상사의 번호가 주어진다. 직속 상사의 번호는 자신의 번호보다 작으며, 최종적으로 1번이 사장이다. 1번의 경우, 상사가 없으므로 -1이 입력된다.

다음 m줄에는 직속 상사로부터 칭찬을 받은 직원 번호 i, 칭찬의 수치 w가 주어진다. (2 ≤ i ≤ n, 1 ≤ w ≤ 1,000)

사장은 상사가 없으므로 칭찬을 받지 않는다.
### **출력**
1번부터 n번의 직원까지 칭찬을 받은 정도를 출력하시오.
### **예제입출력**

**예제 입력1**

```
5 3
-1 1 2 3 4
2 2
3 4
5 6
```

**예제 출력1**

```
0 2 6 6 12
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split())
arr = [0] + list(map(int, sys.stdin.readline().rstrip().split()))

edges = [[] for _ in range(N+1)]
for i in range(2, N + 1):
    edges[arr[i]].append(i)


score = [0] * (N + 1)
for _ in range(M):
    i, w = map(int, sys.stdin.readline().rstrip().split())
    score[i] += w

q = deque([1])
while q:
    now_node = q.popleft()

    for next_node in edges[now_node]:
        q.append(next_node)
        score[next_node] += score[now_node]

print(" ".join(map(str, score[1:])))
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|134876|192|PyPy3|571
#### **📝해설**

**알고리즘**
```
1. 트리
2. DP
```

### **다른 풀이**

```python
import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    boss = [0] + [*map(int, input().split())]
    praise = [0] * (n + 1)
    for _ in range(m):
        i, w = map(int, input().split())
        praise[i] += w
    for i in range(2, n + 1):
        praise[i] += praise[boss[i]]
    print(*praise[1:])

solve()
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
tkqmfp26|43484|140|Python3
#### **📝해설**

```python
import sys
from collections import deque

# 입력받기
N, M = map(int, sys.stdin.readline().rstrip().split())
arr = [0] + list(map(int, sys.stdin.readline().rstrip().split()))

# 상사 기준, 자신의 부하 직원이 누구인지 저장할 리스트
edges = [[] for _ in range(N+1)]

# 부하직원 정보를 저장
for i in range(2, N + 1):
    edges[arr[i]].append(i)


# 칭찬 점수
score = [0] * (N + 1)

# 칭찬점수 입력받기
for _ in range(M):
    i, w = map(int, sys.stdin.readline().rstrip().split())
    score[i] += w

# 사장부터 시작해서 BFS
q = deque([1])

while q:
    now_node = q.popleft()

    # 부하직원으로 내려가면서 점수를 더해줌
    for next_node in edges[now_node]:
        q.append(next_node)
        score[next_node] += score[now_node]

print(" ".join(map(str, score[1:])))
```