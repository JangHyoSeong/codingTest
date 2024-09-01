# [2294] 동전 2

### **난이도**
골드 5
## **📝문제**
n가지 종류의 동전이 있다. 이 동전들을 적당히 사용해서, 그 가치의 합이 k원이 되도록 하고 싶다. 그러면서 동전의 개수가 최소가 되도록 하려고 한다. 각각의 동전은 몇 개라도 사용할 수 있다.
### **입력**
첫째 줄에 n, k가 주어진다. (1 ≤ n ≤ 100, 1 ≤ k ≤ 10,000) 다음 n개의 줄에는 각각의 동전의 가치가 주어진다. 동전의 가치는 100,000보다 작거나 같은 자연수이다. 가치가 같은 동전이 여러 번 주어질 수도 있다.
### **출력**
첫째 줄에 사용한 동전의 최소 개수를 출력한다. 불가능한 경우에는 -1을 출력한다.
### **예제입출력**

**예제 입력1**

```
3 15
1
5
12
```

**예제 출력1**

```
3
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]

INF = 21e8
dp = [0] * (K+1)

for coin in coins:
    if coin <= K:
        dp[coin] = 1

for i in range(K+1):
    if dp[i] == 0:
        continue
    for coin in coins:
        if i+coin <= K:
            if dp[i+coin] == 0:
                dp[i+coin] = dp[i] + 1
            else:
                dp[i+coin] = min(dp[i+coin], dp[i] + 1)

if dp[K]:
    print(dp[K])
else:
    print(-1)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|31120|456|Python3|459
#### **📝해설**

**알고리즘**
```
1. DP
```

### **다른 풀이**

```python
import sys
from collections import deque
read=sys.stdin.readline

n,k = map(int,read().split())

# set로 받는 이유는 같은 coin이 들어올 수 있기 때문
coins = list(i for i in set(int(read()) for _ in range(n)) if i <=k)

if k in coins:
    print(1)
    exit()

# deque([(0, 1), (1, 5), (2, 12)])
que = deque([(i, coin) for i, coin in enumerate(coins)])
visit = [0]* (k + 1)

for i in coins:
    visit[i] = 1

cnt = 1
while que:
    for _ in range(len(que)):
        index, coin_sum = que.popleft()
                
        # 왜 시작이 index냐면 5,12 더하는 것과 12,5 더하는 건 같기 때문. 5면 5, 12 더하고 12 면 12만 해주면됨
        # 소수 찾기에서 2*3 이랑 3*2랑 중복되는 부분 피해주는거랑 비슷한 개념
        for i in range(index, len(coins)):
            new_sum = coin_sum + coins[i]
            if new_sum == k:
                print(cnt + 1)
                exit(0)          
            if new_sum <= k and not visit[new_sum]:
                que.append((i, new_sum))
                visit[new_sum] = 1
    cnt +=1

print(-1)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
capjohnlee|34176|80|Python3|1103
#### **📝해설**

```python
N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]

# K원을 만들 때 최소가 되는 동전개수를 저장할 DP배열
dp = [0] * (K+1)

# DP배열 초기값 삽입
for coin in coins:
    if coin <= K:
        dp[coin] = 1

# K까지 순회하면서
for i in range(K+1):

    # 만약 초기값이 들어있지 않다면(만들 수 없다면)
    if dp[i] == 0:
        # 이번 인덱스는 넘김
        continue

    # 모든 동전을 검사하면서
    for coin in coins:
        # 인덱스를 넘지 않을 때
        if i+coin <= K:
            # 만들어지지 않았던 경우라면 +1(이번 코인을 더함)
            if dp[i+coin] == 0:
                dp[i+coin] = dp[i] + 1
            
            # 만들어졌던 경우라면, 최소값이 갱신 가능할 때 갱신
            else:
                dp[i+coin] = min(dp[i+coin], dp[i] + 1)

# K원을 만들수 없는 경우 -1 출력
if dp[K]:
    print(dp[K])
else:
    print(-1)
```