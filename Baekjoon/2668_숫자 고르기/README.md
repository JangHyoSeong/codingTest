# [2668] 숫자 고르기

### **난이도**
골드 5
## **📝문제**
세로 두 줄, 가로로 N개의 칸으로 이루어진 표가 있다. 첫째 줄의 각 칸에는 정수 1, 2, …, N이 차례대로 들어 있고 둘째 줄의 각 칸에는 1이상 N이하인 정수가 들어 있다. 첫째 줄에서 숫자를 적절히 뽑으면, 그 뽑힌 정수들이 이루는 집합과, 뽑힌 정수들의 바로 밑의 둘째 줄에 들어있는 정수들이 이루는 집합이 일치한다. 이러한 조건을 만족시키도록 정수들을 뽑되, 최대로 많이 뽑는 방법을 찾는 프로그램을 작성하시오. 예를 들어, N=7인 경우 아래와 같이 표가 주어졌다고 하자.

![이미지](https://www.acmicpc.net/upload/images/u5JZnfExdtFXjmR.png)

이 경우에는 첫째 줄에서 1, 3, 5를 뽑는 것이 답이다. 첫째 줄의 1, 3, 5밑에는 각각 3, 1, 5가 있으며 두 집합은 일치한다. 이때 집합의 크기는 3이다. 만약 첫째 줄에서 1과 3을 뽑으면, 이들 바로 밑에는 정수 3과 1이 있으므로 두 집합이 일치한다. 그러나, 이 경우에 뽑힌 정수의 개수는 최대가 아니므로 답이 될 수 없다.
### **입력**
첫째 줄에는 N(1≤N≤100)을 나타내는 정수 하나가 주어진다. 그 다음 줄부터는 표의 둘째 줄에 들어가는 정수들이 순서대로 한 줄에 하나씩 입력된다.
### **출력**
첫째 줄에 뽑힌 정수들의 개수를 출력하고, 그 다음 줄부터는 뽑힌 정수들을 작은 수부터 큰 수의 순서로 한 줄에 하나씩 출력한다.
### **예제입출력**

**예제 입력1**

```
7
3
1
1
5
5
4
6
```

**예제 출력1**

```
3
1
3
5
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N = int(input())

arr = [0]
for _ in range(N):
    num = int(input())
    arr.append(num)

visited = [False] * (N + 1)
cycle = set()

def dfs(start: int, current: int, path: list):
    visited[current] = True
    path.append(current)
    next_node = arr[current]

    if not visited[next_node]:
        dfs(start, next_node, path)
    
    else:
        if next_node in path:
            idx = path.index(next_node)
            for node in path[idx:]:
                cycle.add(node)

for i in range(1, N+1):
    if not visited[i]:
        dfs(i, i, [])

print(len(cycle))
for num in sorted(cycle):
    print(num)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|32412|40|Python3|613
#### **📝해설**

**알고리즘**
```
1. DFS
```
### **다른 풀이**

```python
import sys


def dfs(start: int, num: int):
    visited.add(num)

    if arr[num] not in visited:
        dfs(start, arr[num])
    elif arr[num] in visited and start == arr[num]:
        answer.append(start)


n = int(sys.stdin.readline())
arr = [0] + [int(sys.stdin.readline()) for _ in range(n)]
answer = []
for i in range(1, n + 1):
    visited = set()
    dfs(i, i)

print(len(answer))
for a in answer:
    print(a)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
junjange|31120|28|Python3|420
#### **📝해설**

```python
N = int(input())

# 인덱싱을 위해 0을 넣고 시작
arr = [0]
for _ in range(N):
    num = int(input())
    arr.append(num)

# 방문 여부를 저장할 리스트
visited = [False] * (N + 1)

# 사이클이 존재한다면, 어떤 노드들이 포함되는지 저장할 set
cycle = set()


# 재귀적으로 호출되면서 DFS를 하는 함수
def dfs(start: int, current: int, path: list):

    # 현재 노드에 방문 처리
    visited[current] = True
    
    # 현재까지 방문한 노드들의 경로
    path.append(current)

    # 다음으로 방문할 노드
    next_node = arr[current]

    # 다음 방문할 노드가 아직 방문하기 전이라면 방문
    if not visited[next_node]:
        dfs(start, next_node, path)
    
    # 이미 방문했었다면
    else:

        # 지나온 길에 있다면
        if next_node in path:

            # 그 노드 이후부터 사이클에 포함
            idx = path.index(next_node)
            for node in path[idx:]:
                cycle.add(node)

# 모든 노드에서부터 DFS
for i in range(1, N+1):
    if not visited[i]:
        dfs(i, i, [])

# 출력
print(len(cycle))
for num in sorted(cycle):
    print(num)
```