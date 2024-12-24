# [9466] 텀 프로젝트

### **난이도**
골드 3
## **📝문제**
이번 가을학기에 '문제 해결' 강의를 신청한 학생들은 텀 프로젝트를 수행해야 한다. 프로젝트 팀원 수에는 제한이 없다. 심지어 모든 학생들이 동일한 팀의 팀원인 경우와 같이 한 팀만 있을 수도 있다. 프로젝트 팀을 구성하기 위해, 모든 학생들은 프로젝트를 함께하고 싶은 학생을 선택해야 한다. (단, 단 한 명만 선택할 수 있다.) 혼자 하고 싶어하는 학생은 자기 자신을 선택하는 것도 가능하다.

학생들이(s1, s2, ..., sr)이라 할 때, r=1이고 s1이 s1을 선택하는 경우나, s1이 s2를 선택하고, s2가 s3를 선택하고,..., sr-1이 sr을 선택하고, sr이 s1을 선택하는 경우에만 한 팀이 될 수 있다.

예를 들어, 한 반에 7명의 학생이 있다고 하자. 학생들을 1번부터 7번으로 표현할 때, 선택의 결과는 다음과 같다.

1 | 2 | 3 | 4 | 5 | 6 | 7
--|---|---|---|---|---|--
3 | 1 | 3 | 7 | 3 | 4 | 6
위의 결과를 통해 (3)과 (4, 7, 6)이 팀을 이룰 수 있다. 1, 2, 5는 어느 팀에도 속하지 않는다.

주어진 선택의 결과를 보고 어느 프로젝트 팀에도 속하지 않는 학생들의 수를 계산하는 프로그램을 작성하라.
### **입력**
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스의 첫 줄에는 학생의 수가 정수 n (2 ≤ n ≤ 100,000)으로 주어진다. 각 테스트 케이스의 둘째 줄에는 선택된 학생들의 번호가 주어진다. (모든 학생들은 1부터 n까지 번호가 부여된다.)
### **출력**
각 테스트 케이스마다 한 줄에 출력하고, 각 줄에는 프로젝트 팀에 속하지 못한 학생들의 수를 나타내면 된다.
### **예제입출력**

**예제 입력1**

```
2
7
3 1 3 7 3 4 6
8
1 2 3 4 5 6 7 8
```

**예제 출력1**

```
3
0
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
def dfs(node):
    cycle = []
    while not visited[node]:
        visited[node] = True
        cycle.append(node)
        node = arr[node] - 1

    if node in cycle:
        cycle_start = cycle.index(node)
        for i in cycle[cycle_start:]:
            team[i] = True

T = int(input())

for testcase in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    visited = [False] * N
    team = [False] * N

    for i in range(N):
        if not visited[i]:
            dfs(i)
    
    print(N - sum(team))
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|222928|1232|PyPy3|538
#### **📝해설**

**알고리즘**
```
1. DFS
```

### **다른 풀이**

```python
import io, os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

for _ in range(int(input())):
    n = int(input())
    pick = [0] + list(map(int, input().split()))
    selected = [0] * (n+1)
    ans = 0
    for p in pick:
        selected[p] += 1
    nogroup = [x for x in range(1, n+1) if selected[x] == 0]
    while nogroup:
        temp = []
        for x in nogroup:
            selected[pick[x]] -= 1
            if selected[pick[x]] == 0: temp.append(pick[x])
        ans += len(nogroup)
        nogroup = temp
    print(ans)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
eastgi|249384|608|PyPy3|543
#### **📝해설**

```python
def dfs(node):
    # 기준 노드를 시작으로 DFS를 하는 함수

    # 시작 노드를 기준으로 사이클이 존재하는지 검사
    cycle = []

    # 방문하지 않는 노드가 나올때까지 DFS
    while not visited[node]:
        visited[node] = True
        cycle.append(node)
        node = arr[node] - 1

    # 만약 이번 노드가 사이클에 존재한다면
    if node in cycle:

        # 사이클에 있는 노드를 팀에 속한다고 방문처리
        cycle_start = cycle.index(node)
        for i in cycle[cycle_start:]:
            team[i] = True

T = int(input())

for testcase in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    # 방문 여부, 팀 여부
    visited = [False] * N
    team = [False] * N

    # 모든 노드를 검사
    for i in range(N):
        if not visited[i]:
            dfs(i)
    
    print(N - sum(team))
```