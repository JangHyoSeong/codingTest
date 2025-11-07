# [34401] 놀이기구 줄서기

### **난이도**
골드 5
## **📝문제**
민규는 친구들과 테마파크에 갔다가 한 놀이기구에서 빈 좌석을 최대한 줄이고자 작은 그룹을 먼저 찾아 태우는 모습을 보았다. 이것이 회전율을 높이기 위한 운영 방식임을 알게 된 민규는 실제로도 대기 시간이 줄어드는지 궁금해졌다.

놀이기구의 운영 방식은 다음과 같다. 해당 놀이기구에 대한 그룹들의 도착 시각과 인원이 주어진다. 각 그룹은 서로 다른 시각에 대기열에 도착한다. 이 놀이기구는 
$0$초부터 시작하여 
$P$초마다 탑승을 진행하며, 한 번에 최대 
$K$명을 태울 수 있다.

탑승은 먼저 도착한 그룹부터 진행해야 하며, 각 그룹은 대기열에 도착한 시점부터 곧바로 놀이기구에 탑승할 수 있다. 단, 각 그룹은 모든 인원이 한 번에 탑승해야 한다. 따라서 본인보다 앞에 있는 모든 그룹이 현재 빈 좌석의 수보다 인원이 많다면 먼저 탑승할 수 있다. 만약 더 이상 탑승할 수 있는 그룹이 없다면, 빈 좌석이 있더라도 놀이기구는 곧바로 출발한다.

각 그룹의 대기 시간을 
$($ 탑승 시각 
$)-($ 도착 시각 
$)$으로 정의했을 때, 모든 그룹의 대기 시간의 합을 구해보자.
### **입력**
첫 번째 줄에 그룹의 수 
$N$, 놀이기구의 탑승 간격 
$P$와 인원 제한 
$K$가 공백으로 구분되어 주어진다.

두 번째 줄부터 
$N$개의 줄에 걸쳐 각 그룹의 도착 시각 
$t_i$와 인원 
$a_i$가 공백으로 구분되어 주어진다.
### **출력**
모든 그룹의 대기 시간의 합을 출력한다.
### **예제입출력**

**예제 입력1**

```
3 5 4
1 2
2 3
3 1
```

**예제 출력1**

```
14
```

**예제 입력2**

```
2 10 3
25 2
0 1
```

**예제 출력2**

```
5
```

**예제 입력3**

```
3 7 4
1 4
2 2
3 2
```

**예제 출력3**

```
29
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys
from collections import deque
from heapq import heappush, heappop

N, P, K = map(int, sys.stdin.readline().rstrip().split())
groups = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
groups.sort(key=lambda x : x[0])

q = deque()
pq = []

now_time = 0
end_idx = 0
end_teams = 0
answer = 0

while end_teams < N:

    if not q and not pq and end_idx < N:
        if now_time < groups[end_idx][0]:
            now_time = groups[end_idx][0]
            if now_time % P != 0:
                now_time = (now_time // P+1) * P
    
    while end_idx < N and groups[end_idx][0] <= now_time:
        q.append(groups[end_idx])
        end_idx += 1

    capacity = K

    while pq and capacity > 0:
        a, t = pq[0]

        if a <= capacity:
            heappop(pq)
            capacity -= a
            answer += (now_time - t)
            end_teams += 1
        else:
            break
    
    while q and capacity > 0:
        t, a = q.popleft()
        if a <= capacity:
            capacity -= a
            answer += (now_time - t)
            end_teams += 1
        
        else:
            heappush(pq, (a, t))
    
    now_time += P

print(answer)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|133784|240|PyPy3|1188
#### **📝해설**

**알고리즘**
```
1. 큐
2. 구현
```

### **다른 풀이**

```python
import sys
input = sys.stdin.readline

N, P, K = map(int, input().split())
timeline = []
for _ in range(N):
    t, a = map(int, input().split())
    timeline.append((t, a))
timeline.sort()

store = {}
last = -1
ans = 0
next = [0 for _ in range(6)]
for t, a in timeline:
    tt = max(next[a], (t - 1) // P + 1)
    while True:
        if tt not in store:
            store[tt] = 0
        if store[tt] + a <= K:
            store[tt] += a
            next[a] = max(next[a], tt)
            ans += tt * P - t
            break
        tt += 1
print(ans)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
fermion5|130248|144|PyPy3|551