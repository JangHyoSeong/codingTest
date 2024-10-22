# [32248] 더 게임 오브 데스

### **난이도**
실버 1
## **📝문제**
 
$1$번부터 
$N$번까지 번호가 매겨진 
$N$명의 친구들이 더 게임 오브 데스를 한다.

더 게임 오브 데스는 다음의 순서로 진행된다.

- 각각의 친구들이 아무나 한 명씩 지목한다. 
$k$번 친구가 
$A_k$번 친구를 지목했다고 하자.
 
- $1$번 친구가 양의 정수 
$T$를 말한다.
 
- $x=1$로 시작하여 
$x$를 
$A_x$로 바꾸는 것을 
$T$번 반복한다. 이 과정이 끝난 후 
$x$번 친구가 패배한다.  
이 게임에서 패배하는 친구의 번호를 구하는 프로그램을 작성해 보자.
### **입력**
첫째 줄에 게임에 참가하는 친구들의 수를 의미하는 정수 
$N$과 
$1$번 친구가 말할 정수 
$T$가 공백을 사이에 두고 주어진다. (
$1\leq N\leq 100$; 
$1\leq T\leq 10^{18}$)

둘째 줄에 각 친구들이 지목한 친구의 번호 
$A_k$가 공백을 사이에 두고 주어진다. (
$1\leq k\leq N$; 
$1\leq A_k\leq N$)
### **출력**
첫째 줄에 게임 결과 패배하는 친구의 번호를 출력한다.
### **예제입출력**

**예제 입력1**

```
3 6
3 3 2
```

**예제 출력1**

```
2
```

**예제 입력2**

```
3 100
2 3 1
```

**예제 출력2**

```
2
```

**예제 입력3**

```
5 100
1 2 3 4 5
```

**예제 출력3**

```
1
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N, T = map(int, input().split())
arr = list(map(int, input().split()))

visited = [-1] * (N+1)
path = []
current = 1

while visited[current] == -1:
    visited[current] = len(path)
    path.append(current)
    current = arr[current-1]

cycle_start = visited[current]
cycle_length = len(path) - cycle_start

if T < cycle_start:
    print(path[T])
else:
    idx = (T - cycle_start) % cycle_length
    print(path[cycle_start + idx])
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|31120|48|Python3|429
#### **📝해설**

**알고리즘**
```
1. 그래프
```

### **다른 풀이**

```python
import sys
input = sys.stdin.readline

n,t = map(int,input().split())
lst = [0]+list(map(int,input().split()))
cur = 1
nxt = lst[1]
cycle = [1]
while nxt not in cycle:
  cycle.append(nxt)
  nxt = lst[nxt]

idx = cycle.index(nxt)
if t < idx:
  print(cycle[t])
else:
  t-=idx
  cycle = cycle[idx:]
  print(cycle[t%len(cycle)])
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
hwcho98|31120|28|Python3
#### **📝해설**

```python
N, T = map(int, input().split())
arr = list(map(int, input().split()))

# 방문여부기록
visited = [-1] * (N+1)

# 방문 경로를 저장
path = []
current = 1

# 방문한 노드를 만날때까지 경로를 저장
while visited[current] == -1:
    visited[current] = len(path)
    path.append(current)
    current = arr[current-1]

# 사이클 시작점과 길이를 계산
cycle_start = visited[current]
cycle_length = len(path) - cycle_start

# T가 경로 밖에서 끝나면 해당 경로에서 패배자 결정
if T < cycle_start:
    print(path[T])

# 아니라면 사이클을 계산
else:
    idx = (T - cycle_start) % cycle_length
    print(path[cycle_start + idx])
```