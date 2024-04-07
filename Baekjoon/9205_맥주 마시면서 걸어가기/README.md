# [9205] 맥주 마시면서 걸어가기

### **난이도**
골드 5
## **📝문제**
송도에 사는 상근이와 친구들은 송도에서 열리는 펜타포트 락 페스티벌에 가려고 한다. 올해는 맥주를 마시면서 걸어가기로 했다. 출발은 상근이네 집에서 하고, 맥주 한 박스를 들고 출발한다. 맥주 한 박스에는 맥주가 20개 들어있다. 목이 마르면 안되기 때문에 50미터에 한 병씩 마시려고 한다. 즉, 50미터를 가려면 그 직전에 맥주 한 병을 마셔야 한다.

상근이의 집에서 페스티벌이 열리는 곳은 매우 먼 거리이다. 따라서, 맥주를 더 구매해야 할 수도 있다. 미리 인터넷으로 조사를 해보니 다행히도 맥주를 파는 편의점이 있다. 편의점에 들렸을 때, 빈 병은 버리고 새 맥주 병을 살 수 있다. 하지만, 박스에 들어있는 맥주는 20병을 넘을 수 없다. 편의점을 나선 직후에도 50미터를 가기 전에 맥주 한 병을 마셔야 한다.

편의점, 상근이네 집, 펜타포트 락 페스티벌의 좌표가 주어진다. 상근이와 친구들이 행복하게 페스티벌에 도착할 수 있는지 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 테스트 케이스의 개수 t가 주어진다. (t ≤ 50)

각 테스트 케이스의 첫째 줄에는 맥주를 파는 편의점의 개수 n이 주어진다. (0 ≤ n ≤ 100).

다음 n+2개 줄에는 상근이네 집, 편의점, 펜타포트 락 페스티벌 좌표가 주어진다. 각 좌표는 두 정수 x와 y로 이루어져 있다. (두 값 모두 미터, -32768 ≤ x, y ≤ 32767)

송도는 직사각형 모양으로 생긴 도시이다. 두 좌표 사이의 거리는 x 좌표의 차이 + y 좌표의 차이 이다. (맨해튼 거리)
### **출력**
각 테스트 케이스에 대해서 상근이와 친구들이 행복하게 페스티벌에 갈 수 있으면 "happy", 중간에 맥주가 바닥나서 더 이동할 수 없으면 "sad"를 출력한다. 
### **예제입출력**

**예제 입력1**

```
2
2
0 0
1000 0
1000 1000
2000 1000
2
0 0
1000 0
2000 1000
2000 2000
```

**예제 출력1**

```
happy
sad
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
T = int(input())

for testcase in range(T):
    N = int(input())
    node = []
    for i in range (N+2):
        node.append(list(map(int, input().split())))

    edge = [[] for _ in range(N+2)]
    for i in range(N+2):
        for j in range(i, N+2):
            if i == j:
                continue

            if abs(node[i][0] - node[j][0]) + abs(node[i][1] - node[j][1]) <= 1000:
                edge[i] += [j]
                edge[j] += [i]

    visited = [False] * (N+2)
    stack = [0]
    visited[0] = True
    flag = False

    while stack:
        now = stack.pop()
        
        if now == N+1:
            flag = True
            break

        for can_go in edge[now]:
            if not visited[can_go]:
                stack.append(can_go)
                visited[can_go] = True
    
    if flag:
        print('happy')
    else:
        print('sad')
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|112320|200|PyPy3|868
#### **📝해설**

**알고리즘**
```
1. 그래프
2. DFS
```

#### **😅개선점**

1. 다른 방법으로도 풀어보자

### **다른 풀이**

```python
import sys

sys.setrecursionlimit(10 ** 5)
si = sys.stdin.readline

t = int(si())


def solution():
    n = int(si())
    start = list(map(int, si().split()))
    stores = [list(map(int, si().split() + [False])) for _ in range(n)]
    end = list(map(int, si().split()))

    def dfs(cur_x, cur_y):
        if abs(cur_x - end[0]) + abs(cur_y - end[1]) <= 1000:
            return True
        ret = False
        for i in stores:
            if i[2]: continue
            if abs(cur_x - i[0]) + abs(cur_y - i[1]) <= 1000:
                i[2] = True
                ret = ret or dfs(i[0], i[1])
        return ret

    print('happy' if dfs(start[0], start[1]) is True else 'sad')

for _ in range(t): solution()
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
melon940925|30616|40|Python3|709
#### **📝해설**

```python
T = int(input())

for testcase in range(T):
    N = int(input())
    node = []

    # 시작지점, 도착지점 까지 총 N+2개의 노드가 존재한다고 생각
    for i in range (N+2):
        node.append(list(map(int, input().split())))

    # 각 노드에서 갈 수 있는 간선의 정보를 저장할 리스트
    edge = [[] for _ in range(N+2)]

    # 각 노드에서 갈 수 있는 편의점(노드)를 리스트에 저장해줌
    for i in range(N+2):
        for j in range(i, N+2):
            if i == j:
                continue

            if abs(node[i][0] - node[j][0]) + abs(node[i][1] - node[j][1]) <= 1000:
                edge[i] += [j]
                edge[j] += [i]

    # 각 편의점의 방문 여부를 저장
    visited = [False] * (N+2)

    # DFS를 위해 스택 선언. 시작값을 넣어줌
    stack = [0]

    # 시작 위치는 방문 표시
    visited[0] = True

    # 도착 지점에 도착했다면 True로 바꾸어줌
    flag = False

    # DFS 시작
    while stack:
        now = stack.pop()
        
        # N+1번째 노드에 도착했다면 == 목표 지점에 도착했다면 종료
        if now == N+1:
            flag = True
            break

        # 현재 위치에서 갈 수 있는 노드를 전부 방문
        # 방문 처리도 동시에 해줌
        for can_go in edge[now]:
            if not visited[can_go]:
                stack.append(can_go)
                visited[can_go] = True
    
    # flag = True 상태로 종료됐다면 happy, 아니라면 sad
    if flag:
        print('happy')
    else:
        print('sad')
```

### **🔖정리**

1. 처음에 로직을 어떻게 짤지 고민했는데, 그래프로 풀 수 있었다.