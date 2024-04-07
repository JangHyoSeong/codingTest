# [13913] 숨바꼭질 4

### **난이도**
골드 4
## **📝문제**
수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.
### **입력**
첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.
### **출력**
첫째 줄에 수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

둘째 줄에 어떻게 이동해야 하는지 공백으로 구분해 출력한다.
### **예제입출력**

**예제 입력1**

```
5 17
```

**예제 출력1**

```
4
5 10 9 18 17
```

**예제 입력2**

```
5 17
```

**예제 출력2**

```
4
5 4 8 16 17
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from collections import deque

N, K = map(int,input().split())

visited = [None] * 100001
footprints = [None] * 100001

q = deque()
q.append(N)
visited[N] = 0

while q:
    N = q.popleft()

    if N == K:
        break

    for new_N in [N*2, N+1, N-1]:
        if 0 <= new_N < 100001:
            if visited[new_N] is None:
                q.append(new_N)
                visited[new_N] = visited[N] + 1
                footprints[new_N] = N

print(visited[K])
result = [K]

for i in range(visited[K]):
    result.append(footprints[result[-1]])

for i in range(len(result)-1, -1, -1):
    print(result[i], end=" ")
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|124980|180|PyPy3|615
#### **📝해설**

**알고리즘**
```
1. BFS
2. 그래프
```

### **다른 풀이**

```python
from sys import stdin


def dfs(n: int, k: int):
    if n >= k:
        return n - k, [*range(n, k - 1, -1)]
    elif k == 1:
        return 1, [0, 1]
    elif k & 1 == 1:
        opt1, route1 = dfs(n, k - 1)
        opt2, route2 = dfs(n, k + 1)
        if opt1 <= opt2:
            return opt1 + 1, route1 + [k]
        else:
            return opt2 + 1, route2 + [k]
    else:
        opt, route = dfs(n, k // 2)
        if k - n <= opt + 1:
            return k - n, [*range(n, k + 1)]
        else:
            return opt + 1, route + [k]


def main():
    n, k = map(int, stdin.readline().split())
    opt, route = dfs(n, k)
    print(opt)
    print(" ".join(map(str, route)))


if __name__ == "__main__":
    main()
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
pilmokim99|42476|64|Python3|721
#### **📝해설**

```python
from collections import deque

N, K = map(int,input().split())

# 방문 여부와, 방문 시 몇번째 이동인지 기록할 리스트
visited = [None] * 100001

# 몇번에서 왔는지 기록할 리스트
# 예를들어 5에서 10으로 이동한 경우 footpirnts[10] = 5
footprints = [None] * 100001

# BFS의 시작 세팅
q = deque()
q.append(N)
visited[N] = 0

# BFS 실행
while q:
    N = q.popleft()

    # 목표지점에 도착했다면 종료
    if N == K:
        break

    # N*2, N+1, N-1을 진행
    for new_N in [N*2, N+1, N-1]:
        # 범위를 벗어나지 않고
        if 0 <= new_N < 100001:

            # 방문한 적 없다면
            if visited[new_N] is None:
                # q에 삽입, visited를 현재 이동 횟수로 설정, footprints에 발자취 남김
                q.append(new_N)
                visited[new_N] = visited[N] + 1
                footprints[new_N] = N

# visited[K]는 몇 번 이동했는지 기록되어 있음
print(visited[K])

# 어떻게 움직였는지 기록할 리스트
# 움직임의 역순으로 기록됨
result = [K]

# 발자취를 거슬러 올라가면서 result에 기록
for i in range(visited[K]):
    result.append(footprints[result[-1]])

# 출력
for i in range(len(result)-1, -1, -1):
    print(result[i], end=" ")
```

### **🔖정리**

1. 시간 초과를 조심하자