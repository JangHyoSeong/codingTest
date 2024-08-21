# [32133] 가위바위보

### **난이도**
골드 5
## **📝문제**
피돌이는 
$N$명의 친구들에게 선물을 주려고 한다. 하지만 가난했던 피돌이는 선물을 
$K$개
$(K < N)$ 밖에 준비하지 못했다.

그럼에도 불구하고 최대한 공평하게 선물을 분배하기 위해 가위바위보로 
$K$명 이하의 인원을 뽑은 뒤 선물을 
$1$개씩 나누어 주려고 한다.

여러 명이서 동시에 가위바위보를 하면 비길 확률이 너무 높기 때문에, 피돌이는 자신을 이기는 사람만 살아남는 방식으로 뽑으려고 한다.

더 구체적으로 총 
$M$번의 라운드를 진행하는데, 처음에 
$N$명으로 시작하여 라운드마다 가위바위보로 피돌이를 이긴 사람만 다음 라운드를 계속 진행한다. 그러다가 남은 사람이 
$K$명 이하가 되면 즉시 종료하고 선물을 나누어 준다. 만일 아무도 남아있지 않거나 마지막 라운드 이후에도 
$K$명 넘게 남았다면 선물을 나누어 주지 못한다.

피돌이는 가위바위보를 하기 귀찮기 때문에 최대한 빠르게 뽑으려고 한다. 이를 위해 독심술을 써서 각 친구가 
$i$번째
$(1 \le i \le M)$ 라운드에 무엇을 낼 지 모두 파악해 두었다.

라운드를 최소한으로 진행하고 선물을 나누어 주려면 피돌이가 가위바위보를 어떻게 내는 것이 가장 좋을지 구하시오.
### **입력**
첫째 줄에 친구들의 수 
$N$, 최대 라운드 수 
$M$, 준비한 선물의 개수 
$K$가 공백을 사이에 두고 주어진다. 
$(1 \le K < N \le 50;$ 
$1 \le M \le 50)$ 

둘째 줄부터 
$N$개의 줄에 걸쳐 각 친구가 무엇을 낼지 의미하는 문자열 
$a_1a_2\dots a_M$이 주어진다. 
$a_i$는 
$i$번째 라운드에 낼 것을 의미하며 S는 가위, R은 바위, P는 보이다. 
$(a_i \in \{R,S,P\}$; 
$1 \le i \le M)$ 
### **출력**
만일 피돌이가 어떻게 내도 선물을 나누어 줄 수 없다면 첫째 줄에 -1을 출력하고 종료한다.

나누어 줄 수 있다면 첫째 줄에 선물을 나누어 주기 위해 필요한 최소 라운드 수 
$P$을 출력한다. 
$(1 \le P \le M)$ 

둘째 줄에 그때 피돌이가 어떻게 내야 하는지 의미하는 문자열 
$b_1b_2\dots b_P$를 출력한다. 
$b_i$는 
$i$번째 라운드에 낼 것을 의미하며 S는 가위, R은 바위, P는 보이다. 
$(b_i \in \{R,S,P\}$; 
$1 \le i \le P)$ 가능한 답이 여러개 있다면 아무거나 하나 출력한다.
### **예제입출력**

**예제 입력1**

```
4 3 1
RSP
RSS
SPS
SRP
```

**예제 출력1**

```
2
PR
```

**예제 입력2**

```
2 3 1
PSR
PSR
```

**예제 출력2**

```
-1
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from collections import deque

def solve():
    N, M, K = map(int, input().split())
    arr = [input().strip() for _ in range(N)]

    # BFS로 각 상태를 탐색
    queue = deque([(0, list(range(N)), [])])
    
    while queue:
        round, remaining, moves = queue.popleft()
        
        if len(remaining) == 0:
            continue

        if len(remaining) <= K:
            print(round)
            print("".join(moves))
            return
        
        if round == M:
            continue

        
        # 가능한 피돌이의 선택을 모두 시도 (R, S, P)
        if round < M:
            for move in ['R', 'S', 'P']:
                new_remaining = []
                for i in remaining:
                    # 피돌이가 무엇을 내야 친구 i가 탈락하는지 계산
                    if (move == 'R' and arr[i][round] == 'P') or \
                    (move == 'S' and arr[i][round] == 'R') or \
                    (move == 'P' and arr[i][round] == 'S'):
                        new_remaining.append(i)
                        
                
                queue.append((round + 1, new_remaining, moves + [move]))
    
    # 가능한 모든 경우를 시도했지만 방법이 없는 경우
    print(-1)

solve()
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|34088|52|Python3|1260
#### **📝해설**

**알고리즘**
```
1. 브루트포스 알고리즘
```

### **다른 풀이**

```python
n,m,k=map(int,input().split())
a=[]
for i in range(n):a.append(input())
for j in range(1,m+1):
    d={}
    for i in range(n):
        if a[i][:j]in d:d[a[i][:j]]+=1
        else:d[a[i][:j]]=1
    p,b=min([v,k] for k,v in d.items())
    if p<=k:print(j);print(b.translate(str.maketrans("SRP","PSR")));break
else:print(-1)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
tapris|31120|32|Python3|321