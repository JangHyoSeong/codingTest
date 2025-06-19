# [2230] 수 고르기

### **난이도**
골드 5
## **📝문제**
N개의 정수로 이루어진 수열 A[1], A[2], …, A[N]이 있다. 이 수열에서 두 수를 골랐을 때(같은 수일 수도 있다), 그 차이가 M 이상이면서 제일 작은 경우를 구하는 프로그램을 작성하시오.

예를 들어 수열이 {1, 2, 3, 4, 5}라고 하자. 만약 M = 3일 경우, 1 4, 1 5, 2 5를 골랐을 때 그 차이가 M 이상이 된다. 이 중에서 차이가 가장 작은 경우는 1 4나 2 5를 골랐을 때의 3이 된다.
### **입력**
첫째 줄에 두 정수 N, M이 주어진다. 다음 N개의 줄에는 차례로 A[1], A[2], …, A[N]이 주어진다.
### **출력**
첫째 줄에 M 이상이면서 가장 작은 차이를 출력한다. 항상 차이가 M이상인 두 수를 고를 수 있다.
### **예제입출력**

**예제 입력1**

```
3 3
1
5
3
```

**예제 출력1**

```
4
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
arr = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

arr.sort()
min_gap = float('inf')

front, rear = 0, 0

while front < N and rear < N:
    gap = arr[rear] - arr[front]

    if gap < M:
        rear += 1
    else:
        min_gap = min(min_gap, gap)
        front += 1

print(min_gap)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|36264|168|Python3|362
#### **📝해설**

**알고리즘**
```
1. 투 포인터
```

### **다른 풀이**

```python
""" Solution 1) Binary Search """
# from bisect import bisect_left
# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# a = sorted(int(input()) for _ in range(n))

# mn = 2_000_000_000
# for i in a:
#     j = bisect_left(a, i+m)
#     if j<n: mn = min(mn, a[j]-i)

# print(mn)

""" Solution 2) Two pointer """
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = sorted(set(int(input()) for _ in range(n)))

l, r = 0, 1

mn = 2_000_000_000
while r < len(a):
    diff = a[r]-a[l]
    if diff == m: print(m); exit()
    if diff > m:
        if diff < mn: mn = diff
        l += 1
    else:
        r += 1

print(mn)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
mhc|33684|84|Python3|663
#### **📝해설**

```python
import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
arr = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

# 정렬
arr.sort()
min_gap = float('inf')

# 투포인터. 시작지점을 가장 작은수로 설정
front, rear = 0, 0

# 인덱스를 벗어나지 않으면서
while front < N and rear < N:
    gap = arr[rear] - arr[front]

    # M보다 작다면 뒤쪽 인덱스를 늘림
    if gap < M:
        rear += 1

    # M보다 작지 않은 경우
    else:

        # 갱신 가능하다면 갱신
        min_gap = min(min_gap, gap)

        # 앞쪽 인덱스를 늘림
        front += 1

print(min_gap)
```