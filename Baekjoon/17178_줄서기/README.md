# [17178] 줄서기

### **난이도**
골드 5
## **📝문제**
N줄에 0 이상 9 이하의 숫자가 세 개씩 적혀 있다. 내려가기 게임을 하고 있는데, 이 게임은 첫 줄에서 시작해서 마지막 줄에서 끝나게 되는 놀이이다.

먼저 처음에 적혀 있는 세 개의 숫자 중에서 하나를 골라서 시작하게 된다. 그리고 다음 줄로 내려가는데, 다음 줄로 내려갈 때에는 다음과 같은 제약 조건이 있다. 바로 아래의 수로 넘어가거나, 아니면 바로 아래의 수와 붙어 있는 수로만 이동할 수 있다는 것이다. 이 제약 조건을 그림으로 나타내어 보면 다음과 같다.



별표는 현재 위치이고, 그 아랫 줄의 파란 동그라미는 원룡이가 다음 줄로 내려갈 수 있는 위치이며, 빨간 가위표는 원룡이가 내려갈 수 없는 위치가 된다. 숫자표가 주어져 있을 때, 얻을 수 있는 최대 점수, 최소 점수를 구하는 프로그램을 작성하시오. 점수는 원룡이가 위치한 곳의 수의 합이다.
### **입력**
첫째 줄에 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 N개의 줄에는 숫자가 세 개씩 주어진다. 숫자는 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 중의 하나가 된다.
### **출력**
첫째 줄에 얻을 수 있는 최대 점수와 최소 점수를 띄어서 출력한다.
### **예제입출력**

**예제 입력1**

```
3
1 2 3
4 5 6
4 9 0
```

**예제 출력1**

```
18 6
```

**예제 입력2**

```
3
0 0 0
0 0 0
0 0 0
```

**예제 출력2**

```
0 0
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N = int(input())

prev_max = list(map(int, input().split()))
prev_min = prev_max[:]

for _ in range(1, N):
    current = list(map(int, input().split()))
    max0 = max(prev_max[0], prev_max[1]) + current[0]
    max1 = max(prev_max) + current[1]
    max2 = max(prev_max[1], prev_max[2]) + current[2]
    
    min0 = min(prev_min[0], prev_min[1]) + current[0]
    min1 = min(prev_min) + current[1]
    min2 = min(prev_min[1], prev_min[2]) + current[2]

    prev_max = [max0, max1, max2]
    prev_min = [min0, min1, min2]

print(max(prev_max), min(prev_min))
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|31120|2504|Python3|555
#### **📝해설**

**알고리즘**
```
1. DP
```

### **다른 풀이**

```python
import sys
input = sys.stdin.readline
n = int(input())

max_dp = [0, 0, 0]
min_dp = [0, 0, 0]

for i in range(n):
    a, b, c = map(int, input().rstrip().split())
    if i == 0:
        max_dp = [a, b, c]
        min_dp = [a, b, c]
    else:
        temp_max = max_dp[:]
        max_dp[0] = max(temp_max[:2]) + a
        max_dp[1] = max(temp_max) + b
        max_dp[2] = max(temp_max[1:]) + c

        temp_min = min_dp[:]
        min_dp[0] = min(temp_min[:2]) + a
        min_dp[1] = min(temp_min) + b
        min_dp[2] = min(temp_min[1:]) + c

print(max(max_dp), min(min_dp))
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
110552|144|PyPy3|577
#### **📝해설**

```python
N = int(input())

# 한 줄을 dp 배열로 저장
prev_max = list(map(int, input().split()))
prev_min = prev_max[:]

for _ in range(1, N):
    # 이전 줄에 대해서 최대, 최소 찾는 DP 진행
    current = list(map(int, input().split()))
    max0 = max(prev_max[0], prev_max[1]) + current[0]
    max1 = max(prev_max) + current[1]
    max2 = max(prev_max[1], prev_max[2]) + current[2]
    
    min0 = min(prev_min[0], prev_min[1]) + current[0]
    min1 = min(prev_min) + current[1]
    min2 = min(prev_min[1], prev_min[2]) + current[2]

    prev_max = [max0, max1, max2]
    prev_min = [min0, min1, min2]

print(max(prev_max), min(prev_min))
```

### **🔖정리**

1. 배운점