# [1325] 효율적인 해킹

### **난이도**
실버 1
## **📝문제**
해커 김지민은 잘 알려진 어느 회사를 해킹하려고 한다. 이 회사는 N개의 컴퓨터로 이루어져 있다. 김지민은 귀찮기 때문에, 한 번의 해킹으로 여러 개의 컴퓨터를 해킹 할 수 있는 컴퓨터를 해킹하려고 한다.

이 회사의 컴퓨터는 신뢰하는 관계와, 신뢰하지 않는 관계로 이루어져 있는데, A가 B를 신뢰하는 경우에는 B를 해킹하면, A도 해킹할 수 있다는 소리다.

이 회사의 컴퓨터의 신뢰하는 관계가 주어졌을 때, 한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호를 출력하는 프로그램을 작성하시오.
### **입력**
첫째 줄에, N과 M이 들어온다. N은 10,000보다 작거나 같은 자연수, M은 100,000보다 작거나 같은 자연수이다. 둘째 줄부터 M개의 줄에 신뢰하는 관계가 A B와 같은 형식으로 들어오며, "A가 B를 신뢰한다"를 의미한다. 컴퓨터는 1번부터 N번까지 번호가 하나씩 매겨져 있다.
### **출력**
첫째 줄에, 김지민이 한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호를 오름차순으로 출력한다.
### **예제입출력**

**예제 입력1**

```
5 4
3 1
3 2
4 3
5 3
```

**예제 출력1**

```
1 2
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
edges = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    edges[b].append(a)

max_count = 0
result = []
for i in range(1, N+1):
    visited = [False] * (N + 1)

    count = 1
    stack = [i]
    visited[i] = True

    while stack:
        now = stack.pop()

        for next in edges[now]:
            if not visited[next]:
                count += 1
                stack.append(next)
                visited[next] = True
    
    if max_count < count:
        result = [i]
        max_count = count
    
    elif max_count == count:
        result.append(i)

print(" ".join(map(str, result)))
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|149736|9360|PyPy3|722
#### **📝해설**

**알고리즘**
```
1. DFS
```

#### **📝해설**

```python
import sys

# 입력받기
N, M = map(int, sys.stdin.readline().rstrip().split())
edges = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    edges[b].append(a)

max_count = 0
result = []

# 모든 노드에서부터 DFS로 검사
for i in range(1, N+1):
    visited = [False] * (N + 1)

    count = 1
    stack = [i]
    visited[i] = True

    while stack:
        now = stack.pop()

        for next in edges[now]:
            if not visited[next]:
                count += 1
                stack.append(next)
                visited[next] = True
    
    if max_count < count:
        result = [i]
        max_count = count
    
    elif max_count == count:
        result.append(i)

print(" ".join(map(str, result)))
```