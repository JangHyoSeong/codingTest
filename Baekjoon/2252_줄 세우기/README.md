# [2252] 줄 세우기

### **난이도**
골드 3
## **📝문제**
N명의 학생들을 키 순서대로 줄을 세우려고 한다. 각 학생의 키를 직접 재서 정렬하면 간단하겠지만, 마땅한 방법이 없어서 두 학생의 키를 비교하는 방법을 사용하기로 하였다. 그나마도 모든 학생들을 다 비교해 본 것이 아니고, 일부 학생들의 키만을 비교해 보았다.

일부 학생들의 키를 비교한 결과가 주어졌을 때, 줄을 세우는 프로그램을 작성하시오.
### **입력**
첫째 줄에 N(1 ≤ N ≤ 32,000), M(1 ≤ M ≤ 100,000)이 주어진다. M은 키를 비교한 회수이다. 다음 M개의 줄에는 키를 비교한 두 학생의 번호 A, B가 주어진다. 이는 학생 A가 학생 B의 앞에 서야 한다는 의미이다.

학생들의 번호는 1번부터 N번이다.
### **출력**
첫째 줄에 학생들을 앞에서부터 줄을 세운 결과를 출력한다. 답이 여러 가지인 경우에는 아무거나 출력한다.
### **예제입출력**

**예제 입력1**

```
3 2
1 3
2 3
```

**예제 출력1**

```
1 2 3
```

**예제 입력2**

```
4 2
4 2
3 1
```

**예제 출력2**

```
4 2 3 1
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from collections import deque

N, M = map(int, input().split())

q = deque()
inDegree = [0] * (N+1)
edge = [[] for _ in range (N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    edge[a].append(b)
    inDegree[b] += 1

for idx in range(1, N+1):
    if inDegree[idx] == 0:
        q.append(idx)

result = []
while q:
    now_node = q.popleft()
    result.append(now_node)

    for next_node in edge[now_node]:

        inDegree[next_node] -= 1
        if inDegree[next_node] == 0:
            q.append(next_node)
            
print(" ".join(map(str, result)))
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|120196|204|PyPy3|573
#### **📝해설**

**알고리즘**
```
1. 단방향 비순환 그래프
2. 위상 정렬
```

#### **📝해설**

```python
from collections import deque


'''
문제를 통해 주어진 그래프가 단방향 비순환 그래프인것을 파악 가능
'''
N, M = map(int, input().split())

# 위상 정렬을 사용하기 위해 queue 선언
q = deque()

# 각 노드의 진입차수를 저장
inDegree = [0] * (N+1)

# 간선 정보를 저장
edge = [[] for _ in range (N+1)]


# 인풋을 받음
for _ in range(M):
    a, b = map(int, input().split())
    edge[a].append(b)
    inDegree[b] += 1

# 차수가 0인 노드를 큐에 삽입
for idx in range(1, N+1):
    if inDegree[idx] == 0:
        q.append(idx)

# 결과를 저장할 리스트
result = []

# 큐가 빌때까지 반복
while q:

    # 큐에서 pop
    now_node = q.popleft()

    # 결과에 삽입
    result.append(now_node)


    # 갈수있는 모든 노드를 탐색
    for next_node in edge[now_node]:

        # 현재 노드까지 가는 길을 없앰 (진입 차수를 --)
        inDegree[next_node] -= 1

        # 진입차수가 0이라면 큐에 삽입
        if inDegree[next_node] == 0:
            q.append(next_node)
            
print(" ".join(map(str, result)))
```

### **🔖정리**

1. 위상 정렬, 유향 비순환 그래프에 대한 설명 링크
[위상 정렬](https://m.blog.naver.com/ndb796/221236874984)  
[유향 비순환 그래프](https://algorfati.tistory.com/145)