# [1149] RGB 거리

### **난이도**
실버 1
## **📝문제**
RGB거리에는 집이 N개 있다. 거리는 선분으로 나타낼 수 있고, 1번 집부터 N번 집이 순서대로 있다.

집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야 한다. 각각의 집을 빨강, 초록, 파랑으로 칠하는 비용이 주어졌을 때, 아래 규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값을 구해보자.

- 1번 집의 색은 2번 집의 색과 같지 않아야 한다.
- N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
- i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.
### **입력**
첫째 줄에 집의 수 N(2 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 각 집을 빨강, 초록, 파랑으로 칠하는 비용이 1번 집부터 한 줄에 하나씩 주어진다. 집을 칠하는 비용은 1,000보다 작거나 같은 자연수이다.
### **출력**
첫째 줄에 모든 집을 칠하는 비용의 최솟값을 출력한다.
### **예제입출력**

**예제 입력1**

```
3
26 40 83
49 60 57
13 89 99
```

**예제 출력1**

```
96
```

**예제 입력2**

```
3
1 100 100
100 1 100
100 100 1
```

**예제 출력2**

```
3
```

**예제 입력3**

```
3
1 100 100
100 100 100
1 100 100
```

**예제 출력3**

```
102
```

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

costs = [[0] * 3 for _ in range(N+1)]

for i in range(1, N+1, 1):
    costs[i][0] = min(costs[i-1][1], costs[i-1][2]) + arr[i-1][0]
    costs[i][1] = min(costs[i-1][2], costs[i-1][0]) + arr[i-1][1]
    costs[i][2] = min(costs[i-1][0], costs[i-1][1]) + arr[i-1][2]
    
print(min(costs[-1]))
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|110272|132|PyPy3|367
#### **📝해설**

**알고리즘**
```
1. DP
```

### **다른 풀이**

```python
import sys
input = sys.stdin.readline

N = int(input())
RGB = [0] * 3
for _ in range(N):
    r, g, b = map(int, input().split())
    RGB = [r + min(RGB[1], RGB[2]), g + min(RGB[0], RGB[2]), b + min(RGB[0], RGB[1])]
print(min(RGB))
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
hsmk0076|30616|36|Python3|230
#### **📝해설**

```python
N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

costs = [[0] * 3 for _ in range(N+1)]

# 처음에 R, G, B를 고르는 경우 모두 계산하여, 항상 최소값을 고른다
for i in range(1, N+1, 1):
    costs[i][0] = min(costs[i-1][1], costs[i-1][2]) + arr[i-1][0]
    costs[i][1] = min(costs[i-1][2], costs[i-1][0]) + arr[i-1][1]
    costs[i][2] = min(costs[i-1][0], costs[i-1][1]) + arr[i-1][2]
    
print(min(costs[-1]))
```