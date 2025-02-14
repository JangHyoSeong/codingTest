# [19598] 최소 회의실 개수

### **난이도**
골드 5
## **📝문제**
서준이는 아빠로부터 N개의 회의를 모두 진행할 수 있는 최소 회의실 개수를 구하라는 미션을 받았다. 각 회의는 시작 시간과 끝나는 시간이 주어지고 한 회의실에서 동시에 두 개 이상의 회의가 진행될 수 없다. 단, 회의는 한번 시작되면 중간에 중단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다. 회의의 시작 시간은 끝나는 시간보다 항상 작다. N이 너무 커서 괴로워 하는 우리 서준이를 도와주자.
### **입력**
첫째 줄에 배열의 크기 N(1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N+1 줄까지 공백을 사이에 두고 회의의 시작시간과 끝나는 시간이 주어진다. 시작 시간과 끝나는 시간은 231−1보다 작거나 같은 자연수 또는 0이다.
### **출력**
첫째 줄에 최소 회의실 개수를 출력한다.
### **예제입출력**

**예제 입력1**

```
3
0 40
15 30
5 10
```

**예제 출력1**

```
2
```

**예제 입력2**

```
2
10 20
5 10
```

**예제 출력2**

```
1
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from heapq import heappop, heappush

N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]
meetings.sort()

pq = []
room = 0
max_room = 0
for meeting in meetings:
    heappush(pq, meeting[1])
    room += 1
    
    while pq:
        now_meeting = heappop(pq)

        if meeting[0] >= now_meeting:
            room -= 1
        else:
            heappush(pq, now_meeting)
            break
    
    max_room = max(max_room, room)

print(max_room)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|126760|552|PyPy3|472
#### **📝해설**

**알고리즘**
```
1. 그리디 알고리즘
2. 우선순위 큐
```

### **다른 풀이**

```python
import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    start, end = [], []
    for _ in range(N):
        s, e = map(int, input().split())
        start.append(s)
        end.append(e)
    start.sort()
    end.sort()
    ans, cnt = 0, 0
    e = 0
    for s in start:
        cnt += 1
        if e < len(end) and end[e] <= s:
            cnt -= 1
            e += 1
        if ans < cnt:
            ans = cnt
    print(ans)

solve()
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
tkqmfp26|39220|200|Python3|454
#### **📝해설**

```python
from heapq import heappop, heappush

# 입력받은 후 시작 시간을 기준으로 정렬
N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]
meetings.sort()

# 종료시간을 저장해 둘 우선순위 큐
pq = []

# 현재 사용중인 회의실의 개수
room = 0

# 최대로 필요한 회의실의 개수
max_room = 0

# 시작시간 기준으로 정렬된 회의 시간을 순회
for meeting in meetings:

    # 이번 회의의 종료시간을 우선순위 큐에 삽입
    heappush(pq, meeting[1])
    # 필요한 방의 개수 ++
    room += 1
    
    # 우선순위 큐에서 값을 하나씩 빼면서
    while pq:
        now_meeting = heappop(pq)

        # 만약 이번 회의가 앞서 했던 회의가 종료된 뒤라면
        if meeting[0] >= now_meeting:

            # 방의 개수를 하나 뺌
            room -= 1

        # 만약 아직 종료되지 못한 회의를 만난다면
        else:
            # 종료되지 않은 회의를 다시 우선순위 큐에 삽입
            heappush(pq, now_meeting)

            # 반복 종료
            break
    
    # 최대로 필요한 회의실의 개수를 갱신
    max_room = max(max_room, room)

# 출력
print(max_room)
```