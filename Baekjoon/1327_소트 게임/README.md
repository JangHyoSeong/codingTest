# [1327] 소트 게임

### **난이도**
골드 4
## **📝문제**
홍준이는 소트 게임을 하려고 한다. 소트 게임은 1부터 N까지 정수로 이루어진 N자리의 순열을 이용한다. 이 게임에선 K가 주어진다. 어떤 수를 뒤집으면, 그 수부터 오른쪽으로 K개의 수를 뒤집어야 한다. 예를 들어, 순열이 5 4 3 2 1 이었고, 여기서 K가 3일 때, 4를 뒤집으면 5 2 3 4 1이 된다. 반드시 K개의 수를 뒤집어야하기 때문에, 처음 상태에서 2나 1을 선택하는 것은 불가능하다.

입력으로 들어온 순열을 오름차순으로 만들려고 한다. 게임을 최대한 빨리 끝내고 싶을 때, 수를 최소 몇 개 선택해야 하는지 구해보자.
### **입력**
첫째 줄에 순열의 크기 N과 K가 주어진다. 둘째 줄에 순열에 들어가는 수가 주어진다.
### **출력**
첫째 줄에 정답을 출력한다. 만약 오름차순으로 만들 수 없으면 -1을 출력한다.
### **예제입출력**

**예제 입력1**

```
3 3
3 2 1
```

**예제 출력1**

```
1
```

**예제 입력2**

```
5 2
5 4 3 2 1
```

**예제 출력2**

```
10
```

**예제 입력3**

```
5 4
3 2 4 1 5
```

**예제 출력3**

```
-1
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from collections import deque

N, K = map(int, input().split())
arr = list(map(int, input().split()))

sorted_arr = sorted(arr)

already_make = {}
q = deque([[arr, 0]])

while q:
    now, count = q.popleft()

    if now == sorted_arr:
        print(count)
        break

    for i in range(N-K+1):
        temp_arr = now[i:i+K]
        new = now[:i] + temp_arr[::-1] + now[i+K:]
        tuple_new = tuple(new)
        if already_make.get(tuple_new) is None:
            q.append([new, count+1])
            already_make[tuple_new] = True
else:
    print(-1)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|140740|328|PyPy3|557
#### **📝해설**

**알고리즘**
```
1. BFS
```

### **다른 풀이**

```python
from collections import deque
def bfs():
    q = deque()
    q.append((0, s))
    while q:
        c, curr = q.popleft()
        if curr in visited:
            continue
        else:
            visited.add(curr)
        if curr == ans:
            return c
        for j in range(n-k+1):
            t = 0
            for x in range(j):
                t |= curr & 0b111 << 3*x
            for x in range(j, j+k):
                t |= (curr & 0b111 << 3*x) >> 3*x << 3*(2*j + k - 1-x)
            for x in range(j+k, n):
                t |= curr & 0b111 << 3*x
            q.append((c+1, t))
    return -1

n, k = map(int, input().split())
visited = set()
d = list(map(int, input().split()))
sort_d = sorted(d)
s = 0
ans = 0
for i in range(n):
    s |= d[i]-1 << 3*i
    ans |= sort_d[i]-1 << 3*i
print(bfs())
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
awj1204|124592|208|PyPy3|812
#### **📝해설**

```python
from collections import deque

N, K = map(int, input().split())
arr = list(map(int, input().split()))

# 오름차순 정렬된 리스트를 만들고 정답과 비교함
sorted_arr = sorted(arr)

# 이미 만든 arr는 만들지 않기 위해 딕셔너리를 통해 방문 여부를 검사
already_make = {}
# BFS를 위해 queue를 선언
# 현재 arr와, count를 담고 있음
q = deque([[arr, 0]])


# BFS 시작
while q:
    # 현재 arr, count
    now, count = q.popleft()

    # 오름차순 정렬되었다면 count를 출력하고 종료
    if now == sorted_arr:
        print(count)
        break

    # 아니라면 BFS, 모든 경우를 전부 검사함
    for i in range(N-K+1):
        # K개 만큼 뒤집기 위해서 사용
        temp_arr = now[i:i+K]

        # K개 만큼 뒤집은 새로운 arr
        new = now[:i] + temp_arr[::-1] + now[i+K:]

        # 딕셔너리의 key값으로 쓰기 위해 튜플(불변)으로 만듦
        tuple_new = tuple(new)

        # 만약 딕셔너리에 존재하지 않는다면

        if already_make.get(tuple_new) is None:
            # q에 삽입, 방문처리를 해줌
            q.append([new, count+1])
            already_make[tuple_new] = True
# break되지 않고 끝났다면 -1 출력
else:
    print(-1)
```

### **🔖정리**

1. 리스트 슬라이싱은 제대로 쓰자