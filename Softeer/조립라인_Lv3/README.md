# 조립라인

### **난이도**
Lv.3
## **📝문제**
https://softeer.ai/practice/6287
## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys

N = int(input())
task = []

for i in range(N):
    task.append(list(map(int, input().split())))

dp = [[0, 0] for _ in range(N)]
dp[0] = [task[0][0], task[0][1]]

for i in range(1, N):
    dp[i][0] = task[i][0] + min(dp[i-1][0], dp[i-1][1] + task[i-1][3])
    dp[i][1] = task[i][1] + min(dp[i-1][1], dp[i-1][0] + task[i-1][2])

print(min(dp[N-1]))
```

#### **📝해설**

**알고리즘**
```
1. DP
```

#### **📝해설**

```python
import sys

N = int(input())
task = []

for i in range(N):
    task.append(list(map(int, input().split())))

# 처음에 A에서 시작한 경우, B에서 시작한 경우를 계산하기 위해 dp리스트를 2차원 리스트로 선언
dp = [[0, 0] for _ in range(N)]

# 각각 A작업시간, B작업시간
dp[0] = [task[0][0], task[0][1]]

# 1번 인덱스부터 순회하면서
for i in range(1, N):
    # 현재 라인에서 생산하는 것과, 다른 라인에서 생산하다가 이동하는 것 중 최소값을 선택
    dp[i][0] = task[i][0] + min(dp[i-1][0], dp[i-1][1] + task[i-1][3])
    dp[i][1] = task[i][1] + min(dp[i-1][1], dp[i-1][0] + task[i-1][2])

print(min(dp[N-1]))
```