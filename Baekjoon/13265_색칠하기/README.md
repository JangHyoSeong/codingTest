# [13265] 색칠하기

### **난이도**
골드 5
## **📝문제**
어린 토니킴은 색칠공부를 좋아한다.

토니킴은 먼저 여러 동그라미와 동그라미 두 개를 연결하는 직선들 만으로 그림을 그리고 (모든 동그라미들 사이에 직선이 있을 필요는 없다), 연결된 두 동그라미는 서로 색이 다르게 되도록 색을 칠하고자 한다.

이 그림을 색칠하는데 필요한 최소의 색의 개수를 구하는 문제는 어렵기 때문에 토니킴은 2 가지 색상으로 색칠이 가능한지의 여부만을 알고 싶어한다.

동그라미들의 번호와 동그라미들이 서로 연결된 직선에 대한 정보가 주어졌을 때, 이 동그라미들이 2 가지 색상으로 색칠이 가능한지 알아내자.
### **입력**
입력의 첫 줄에는 테스트 케이스의 개수 T 가 주어진다.

그 다음 줄부터 각 테스트 케이스에 대해 동그라미의 개수 n(1 ≤ n ≤ 1000)과 직선들의 개수 m(1 ≤ m ≤ 100,000)이 주어지고, 그 다음 줄부터 m 줄에 걸쳐 동그라미들이 연결된 직선에 대한 정보가 주어진다. (x y)로 주어지면 동그라미 x와 동그라미 y가 직선으로 서로 연결되었다는 의미이다. 동그라미들의 번호는 1 부터 n 까지이다.
### **출력**
각 테스트 케이스에 대해서 possible 이나 impossible 을 출력한다. 2 가지 색상으로 색칠이 가능하면 possible. 불가능하면 impossible 이다.
### **예제입출력**

**예제 입력1**

```
3
4 5
1 2
2 3
3 4
1 3
2 4
6 9
1 4
1 5
1 6
2 4
2 5
2 6
3 4
3 5
3 6
8 8
1 2
2 3
3 4
4 5
5 6
6 7
7 8
8 1
```

**예제 출력1**

```
impossible
possible
possible
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
T = int(input())

def validate_graph(n, m, edges):

    nodes = [0] * (n+1)
    for i in range(1, n+1):

        if nodes[i]:
            continue

        stack = [i]
        nodes[i] = 1

        while stack:
            now = stack.pop()
            now_color = nodes[now]

            for next in edges[now]:
                if nodes[now] == nodes[next]:
                    return 'impossible'
                    
                
                elif nodes[next] == 0:
                    stack.append(next)
                    nodes[next] = 3 - nodes[now]

    return 'possible'
    

for testcase in range(T):
    n, m = map(int, input().split())
    edges = [[] for _ in range(n+1)]

    for _ in range(m):
        a, b = map(int, input().split())

        edges[a].append(b)
        edges[b].append(a)

    print(validate_graph(n, m, edges))
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|132908|404|PyPy3|852
#### **📝해설**

**알고리즘**
```
1. DFS
2. 이분 그래프
```

#### **📝해설**

```python
T = int(input())

def validate_graph(n, m, edges):
    # impossible시 즉시 리턴을 하기 위해 함수로 해결

    # 현재 노드의 색깔 상태. 0은 방문하지않음, 1, 2는 색깔이 칠해짐
    nodes = [0] * (n+1)

    # 모든 노드를 순회하면서
    for i in range(1, n+1):

        # 이미 방문한 노드라면 다음 노드로 넘어감
        if nodes[i]:
            continue
        
        # 방문하지 않은 노드라면 지금 노드부터 DFS 시작
        stack = [i]

        # 일단 1번 색깔을 칠함
        nodes[i] = 1


        # DFS
        while stack:
            now = stack.pop()
            now_color = nodes[now]

            # 방문할 수 있는 노드를 순회
            for next in edges[now]:

                # 만약 다음 노드가 같은 색깔이라면 불가능한 케이스
                if nodes[now] == nodes[next]:
                    return 'impossible'
                    
                
                # 방문하지 않은 노드라면 방문처리
                elif nodes[next] == 0:
                    stack.append(next)

                    # 현재와 다른 색을 칠함
                    nodes[next] = 3 - nodes[now]

    # 불가능한 케이스에 걸리지 않았다면 가능한 케이스
    return 'possible'
    

for testcase in range(T):
    n, m = map(int, input().split())
    edges = [[] for _ in range(n+1)]

    for _ in range(m):
        a, b = map(int, input().split())

        edges[a].append(b)
        edges[b].append(a)

    print(validate_graph(n, m, edges))
```