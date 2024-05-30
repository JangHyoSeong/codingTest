# [12851] 숨바꼭질 2

### **난이도**
골드 4
## **📝문제**
수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 그리고, 가장 빠른 시간으로 찾는 방법이 몇 가지 인지 구하는 프로그램을 작성하시오.
### **입력**
첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.
### **출력**
첫째 줄에 수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

둘째 줄에는 가장 빠른 시간으로 수빈이가 동생을 찾는 방법의 수를 출력한다.
### **예제입출력**

**예제 입력1**

```
5 17
```

**예제 출력1**

```
4
2
```

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from collections import deque

N, K = map(int, input().split())
q = deque([[N, 0]])

visited = [100000] * 100002

min_cnt = 100000
result = 0

if K < N:
    print(N-K)
    print(1)
else:
    while q:
        now, now_cnt = q.popleft()

        if now == K:
            if min_cnt == 100000 or min_cnt == now_cnt:
                result += 1
                min_cnt = now_cnt
            else:
                break

        for next in [now-1, now+1, now*2]:
            if 0 <= next <= 100001 and visited[next] >= now_cnt:
                if next == K:
                    q.append([next, now_cnt+1])
                else:
                    q.append([next, now_cnt+1])
                    visited[next] = now_cnt

    print(min_cnt)
    print(result)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|139124|208|PyPy3|753
#### **📝해설**

**알고리즘**
```
1. BFS
```

#### **📝해설**

```python
from collections import deque

N, K = map(int, input().split())
# queue를 사용. 처음 위치와 이동 횟수를 삽입
q = deque([[N, 0]])

# visited는 그 위치에 도달하기 까지의 이동 횟수가 저장됨
visited = [100000] * 100002

# 도착지에 도착했을 때 이동 횟수가 될 변수
min_cnt = 100000

# 도착지에 도착하는 경우의 수를 나타냄
result = 0

# 만약 뒤로 가야하는 경우, 이 경우의 수밖에 없음
if K < N:
    print(N-K)
    print(1)

# 앞으로 간다면
else:
    # q가 빌 때까지
    while q:

        # 현재위치, 현재 이동횟수
        now, now_cnt = q.popleft()

        # 도착지에 도착했다면
        if now == K:

            # 한번도 도착한 적 없거나, 같은 이동횟수로 도착했다면
            if min_cnt == 100000 or min_cnt == now_cnt:
                # 경우의수 ++
                result += 1
                # 현재 이동횟수가 최소횟수(BFS)
                min_cnt = now_cnt
            else:
                break

        # 갈 수 있는 곳들을 순회하며
        for next in [now-1, now+1, now*2]:
            # 이동 범위를 벗어나지 않고, 이번 이동횟수가 최소라면
            if 0 <= next <= 100001 and visited[next] >= now_cnt:

                # 도착지라면 방문처리를 따로 하지 않음
                if next == K:
                    q.append([next, now_cnt+1])

                # 도착지가 아니라면 방문처리를 함
                else:
                    q.append([next, now_cnt+1])
                    visited[next] = now_cnt

    print(min_cnt)
    print(result)
```