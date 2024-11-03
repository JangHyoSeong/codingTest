# [5214] 환승

### **난이도**
골드 2
## **📝문제**
아주 먼 미래에 사람들이 가장 많이 사용하는 대중교통은 하이퍼튜브이다. 하이퍼튜브 하나는 역 K개를 서로 연결한다. 1번역에서 N번역으로 가는데 방문하는 최소 역의 수는 몇 개일까?
### **입력**
첫째 줄에 역의 수 N과 한 하이퍼튜브가 서로 연결하는 역의 개수 K, 하이퍼튜브의 개수 M이 주어진다. (1 ≤ N ≤ 100,000, 1 ≤ K, M ≤ 1000)

다음 M개 줄에는 하이퍼튜브의 정보가 한 줄에 하나씩 주어진다. 총 K개 숫자가 주어지며, 이 숫자는 그 하이퍼튜브가 서로 연결하는 역의 번호이다. 
### **출력**
첫째 줄에 1번역에서 N번역으로 가는데 방문하는 역의 개수의 최솟값을 출력한다. 만약, 갈 수 없다면 -1을 출력한다.
### **예제입출력**

**예제 입력1**

```
9 3 5
1 2 3
1 4 5
3 6 7
5 6 7
6 8 9
```

**예제 출력1**

```
4
```

**예제 입력2**

```
15 8 4
11 12 8 14 13 6 10 7
1 5 8 12 13 6 2 4
10 15 4 5 9 8 14 12
11 12 14 3 5 6 1 13
```

**예제 출력2**

```
3
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from collections import deque

N, K, M = map(int, input().split())

station_to_tube = [[] for _ in range(N+1)]
tube_to_station = []

for i in range(M):
    arr = list(map(int, input().split()))
    tube_to_station.append(arr)
    for station in arr:
        station_to_tube[station].append(i)

queue = deque([(1, 1)])
visited_station = [False] * (N+1)
visited_station[1] = True
visited_tube = [False] * M

while queue:
    now, count = queue.popleft()

    if now == N:
        print(count)
        break

    for tube in station_to_tube[now]:
        if not visited_tube[tube]:
            visited_tube[tube] = True

            for next in tube_to_station[tube]:
                if not visited_station[next]:
                    visited_station[next] = True
                    queue.append((next, count+1))

else:
    print(-1)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|159044|480|PyPy3|830
#### **📝해설**

**알고리즘**
```
1. BFS
```

#### **📝해설**

```python
from collections import deque

N, K, M = map(int, input().split())

# 현재 역에서 이용할수있는 하이퍼튜브의 인덱스를 저장
station_to_tube = [[] for _ in range(N+1)]

# 하이퍼튜브를 저장
tube_to_station = []

# 입력받기
for i in range(M):
    arr = list(map(int, input().split()))

    # 하이퍼튜브의 정보를 저장
    tube_to_station.append(arr)
    for station in arr:
        # 이번 역에서 i번째 하이퍼튜브를 사용할 수 있다는 정보 저장
        station_to_tube[station].append(i)

# BFS를 위한 queue
queue = deque([(1, 1)])

# 역에 도착했는지 여부를 저장
visited_station = [False] * (N+1)
visited_station[1] = True

# 하이퍼튜브를 사용했는지 여부를 저장
visited_tube = [False] * M

# BFS 시작
while queue:
    now, count = queue.popleft()

    # 도착했다면 종료
    if now == N:
        print(count)
        break

    # 현재 역에서 사용할 수 있는 하이퍼튜브를 사용
    for tube in station_to_tube[now]:

        # 사용하지 않았던 하이퍼 튜브의 경우만 사용
        if not visited_tube[tube]:

            # 방문처리
            visited_tube[tube] = True
            
            # 이번 하이퍼튜브에서 갈 수 있는 역 조사
            for next in tube_to_station[tube]:

                # 방문한적 없는 역이라면
                if not visited_station[next]:

                    # 방문
                    visited_station[next] = True
                    queue.append((next, count+1))

# 목적지에 도착못한경우 print(-1)
else:
    print(-1)
```