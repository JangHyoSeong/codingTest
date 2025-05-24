# [11000] 강의실 배정

### **난이도**
골드 5
## **📝문제**
수강신청의 마스터 김종혜 선생님에게 새로운 과제가 주어졌다. 

김종혜 선생님한테는 Si에 시작해서 Ti에 끝나는 N개의 수업이 주어지는데, 최소의 강의실을 사용해서 모든 수업을 가능하게 해야 한다. 

참고로, 수업이 끝난 직후에 다음 수업을 시작할 수 있다. (즉, Ti ≤ Sj 일 경우 i 수업과 j 수업은 같이 들을 수 있다.)

수강신청 대충한 게 찔리면, 선생님을 도와드리자!
### **입력**
첫 번째 줄에 N이 주어진다. (1 ≤ N ≤ 200,000)

이후 N개의 줄에 Si, Ti가 주어진다. (0 ≤ Si < Ti ≤ 109)
### **출력**
강의실의 개수를 출력하라.
### **예제입출력**

**예제 입력1**

```
3
1 3
2 4
3 5
```

**예제 출력1**

```
2
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys
from heapq import heappush, heappop

N = int(sys.stdin.readline().rstrip())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

arr.sort(key= lambda x : x)

pq = []
for s, t in arr:
    if pq and pq[0] <= s:
        heappop(pq)
    
    heappush(pq, t)

print(len(pq))
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|142544|448|PyPy3|308
#### **📝해설**

**알고리즘**
```
1. 정렬
2. 우선순위 큐
```

#### **📝해설**

```python
import sys
from heapq import heappush, heappop

# 입력받기
N = int(sys.stdin.readline().rstrip())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

# 시작시간 기준으로 정렬
arr.sort(key= lambda x : x)

# 최소 힙
pq = []

# 시작시간이 빠른것부터 확인하면서
for s, t in arr:

    # 만약, 이미 강의실을 사용하고 있는데, 끝나는 시점이 이번 시작시점보다 빠르다면
    if pq and pq[0] <= s:
        # 그 강의실을 비움
        heappop(pq)
    
    # 강의실을 사용
    heappush(pq, t)

# pq에 남아있는 갯수만큼 강의실이 필요함
print(len(pq))
```