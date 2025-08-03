# [23843] 콘센트

### **난이도**
골드 5
## **📝문제**
광재는 전자기기 대여사업을 시작했다. 퇴근하기 전에 다음날 손님들에게 빌려줄 N개의 전자기기를 충전하려 한다. 사용 가능한 콘센트는 M개가 있고, 성능은 모두 동일하다.

전자기기들은 한 번에 하나의 콘센트에서만 충전이 가능하고, 충전에 필요한 시간은 2k(0 ≤ k ≤ 15, k는 정수) 형태이다.

광재의 빠른 퇴근을 위해 모든 전자기기를 충전하기 위한 최소 시간이 얼마인지 알려주자.
### **입력**
첫째 줄에 전자기기의 개수 N과 콘센트의 개수 M이 주어진다. (1 ≤ N ≤ 10,000, 1 ≤ M ≤ 10)

둘째 줄에 충전에 필요한 시간 ti를 나타내는 N개의 정수가 주어진다. (20 ​≤ ti ≤ 215, ti = 2k (0 ≤ k ≤ 15, k는 정수))
### **출력**
충전에 필요한 최소 시간을 출력한다.
### **예제입출력**

**예제 입력1**

```
5 2
1 4 4 8 1
```

**예제 출력1**

```
9
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys
from heapq import heappush, heappop

N, M = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr.sort(reverse=True)

sockets = [0] * M
idx = 0
for i in range(N):
    if idx == 0:
        sockets[idx] += arr[i]
        idx = (idx + 1) % M
        continue

    sockets[idx] += arr[i]
    if sockets[idx] == sockets[idx - 1]:
        idx = (idx + 1) % M

print(sockets[0])
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|35508|48|Python3|440
#### **📝해설**

**알고리즘**
```
1. 그리디 알고리즘
```

### **다른 풀이**

```python
n, m = map(int, input().split())
a = list(map(int, input().split()))

# a 를 내림차순으로 정렬
a.sort(reverse=True)

# 충전기에 꽂힌 전자기기의 충전시간의 총합을 담고 있을 배열 b 를 선언
b = [0] * m

# a 의 index 를 가리킬 포인터
a_pos = 0

while True:
    # 컨센트에 현재 충전시간이 가장 긴 요소를 꽂아준다. (a 는 내림차순 정렬되어 있다.)
    b[0] += a[a_pos]
    a_pos += 1
    
    # b 를 가리키는 index
    # 1 부터 시작하는 이유는 위에서 0번에 이미 먼저 꽂았기 때문에 남은 자리인 1 부터 시작
    b_pos = 1
    while a_pos < n and b_pos < m:
        b[b_pos] += a[a_pos]
        a_pos += 1

        if b[b_pos] == b[0]:
            b_pos += 1

    if a_pos == n:
        break

    # if b_pos == m:

print(b[0])        
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
qpwoeiworker|31120|36|Python3|839
#### **📝해설**

```python
import sys
from heapq import heappush, heappop

# 입력받기
N, M = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

# 내림차순으로 정렬
arr.sort(reverse=True)

# 각 콘센트에서 사용되는 시간
sockets = [0] * M

# 0번 콘센트부터 차례대로 큰 순서대로 할당
idx = 0
for i in range(N):

    # 0번 콘센트인 경우
    if idx == 0:

        # 남아있는 작업중 가장 큰 시간이 걸리는 것을 할당
        sockets[idx] += arr[i]

        # 다음 콘센트로 이동
        idx = (idx + 1) % M
        continue

    # 0번이 아닌 경우
    # 현재 작업 시간을 더함
    sockets[idx] += arr[i]

    # 이전 작업과 시간이 같은 경우에만 다음 콘센트로 이동
    if sockets[idx] == sockets[idx - 1]:
        idx = (idx + 1) % M

'''
작업에 걸리는 시간이 항상 2^k이므로, 이런 식의 연산이 가능
'''
print(sockets[0])
```