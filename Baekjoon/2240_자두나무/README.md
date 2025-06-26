# [2240] 자두나무

### **난이도**
골드 4
## **📝문제**
자두는 자두를 좋아한다. 그래서 집에 자두나무를 심어두고, 여기서 열리는 자두를 먹고는 한다. 하지만 자두는 키가 작아서 자두를 따먹지는 못하고, 자두가 떨어질 때까지 기다린 다음에 떨어지는 자두를 받아서 먹고는 한다. 자두를 잡을 때에는 자두가 허공에 있을 때 잡아야 하는데, 이는 자두가 말랑말랑하여 바닥에 떨어지면 못 먹을 정도로 뭉개지기 때문이다.

매 초마다, 두 개의 나무 중 하나의 나무에서 열매가 떨어지게 된다. 만약 열매가 떨어지는 순간, 자두가 그 나무의 아래에 서 있으면 자두는 그 열매를 받아먹을 수 있다. 두 개의 나무는 그다지 멀리 떨어져 있지 않기 때문에, 자두는 하나의 나무 아래에 서 있다가 다른 나무 아래로 빠르게(1초보다 훨씬 짧은 시간에) 움직일 수 있다. 하지만 자두는 체력이 그다지 좋지 못해서 많이 움직일 수는 없다.

자두는 T(1≤T≤1,000)초 동안 떨어지게 된다. 자두는 최대 W(1≤W≤30)번만 움직이고 싶어 한다. 매 초마다 어느 나무에서 자두가 떨어질지에 대한 정보가 주어졌을 때, 자두가 받을 수 있는 자두의 개수를 구해내는 프로그램을 작성하시오. 자두는 1번 자두나무 아래에 위치해 있다고 한다.
### **입력**
첫째 줄에 두 정수 T, W가 주어진다. 다음 T개의 줄에는 각 순간에 자두가 떨어지는 나무의 번호가 1 또는 2로 주어진다.
### **출력**
첫째 줄에 자두가 받을 수 있는 자두의 최대 개수를 출력한다.
### **예제입출력**

**예제 입력1**

```
7 2
2
1
1
2
2
1
1
```

**예제 출력1**

```
6
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
T, W = map(int, input().split())
arr = [int(input()) for _ in range(T)]

dp = [[0] * (T+1) for _ in range(W+1)]

for t in range(1, T+1):
    fruit = arr[t-1]

    for w in range(W+1):
        if w == 0:
            dp[w][t] = dp[w][t-1] + (1 if fruit == 1 else 0)
        
        else:
            current_tree = (w % 2) + 1
            dp[w][t] = max(dp[w][t-1], dp[w-1][t-1]) + (1 if fruit == current_tree else 0)

print(max(dp[w][t] for w in range(W+1)))
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|32412|52|Python3|458
#### **📝해설**

**알고리즘**
```
1. DP
```

### **다른 풀이**

```python
import sys
read = sys.stdin.readline

t, w = map(int, read().split())

cnt, pos = [0], 1
for i in range(t):
    if int(read()) == pos:
        cnt[-1] += 1

    else:
        cnt.append(1)
        pos = (pos % 2) + 1

b_len = len(cnt) + 1
w_len = min(b_len, w + 2)
board = [[0]*b_len for _ in range(w_len)]
board[1][1] = cnt[0]

for i in range(2, b_len):
    if i % 2:
        board[1][i] = board[1][i-2] + cnt[i-1]

for i in range(2, w_len):
    for j in range(i, b_len, 2):
        board[i][j] = max(board[i-1][j-1], board[i][j-2]) + cnt[j-1]

print(max(max(i) for i in board))
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
tjtjdals|31120|32|Python3|579
#### **📝해설**

```python
T, W = map(int, input().split())
arr = [int(input()) for _ in range(T)]

# dp[w][t] : w번 움직였을 때 t초까지 자두를 최대로 받을 수 있는 수
dp = [[0] * (T+1) for _ in range(W+1)]

# 1에서 t초까지 검사
for t in range(1, T+1):
    fruit = arr[t-1]

    # 한번씩 움직일 때
    for w in range(W+1):

        # 아직 한 번도 이동하지 않았다면
        if w == 0:

            # 1번 나무 아래
            dp[w][t] = dp[w][t-1] + (1 if fruit == 1 else 0)
        
        # 한 번이라도 이동했다면
        else:

            # 현재 나무 위치
            current_tree = (w % 2) + 1

            # 이동했을때와 이동하지 않았을 때 중 최대값을 저장
            dp[w][t] = max(dp[w][t-1], dp[w-1][t-1]) + (1 if fruit == current_tree else 0)

# 최대값 출력
print(max(dp[w][t] for w in range(W+1)))
```