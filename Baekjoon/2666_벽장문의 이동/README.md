# [2666] 벽장문의 이동

### **난이도**
골드 5
## **📝문제**
n개의 같은 크기의 벽장들이 일렬로 붙어져 있고 벽장의 문은 n-2개만이 있다. 한 벽장 앞에 있는 문은 이웃 벽장 앞에 문이 없다면(즉, 벽장이 열려있다면) 그 벽장 앞으로 움직일 수 있다.

그림은 7개의 벽장의 예이다. 그림에서 2번 벽장과 5번 벽장이 열려있고, 나머지 벽장은 닫혀 있다.  벽장 문은 좌우 어느 쪽이든 그 이웃 벽장이 열려 있다면 그 쪽으로 한 칸씩 이동할 수 있다. 그림에서 주어진 상태에서는 1번 벽장을 닫고 있는 벽장문을 오른쪽으로 한 칸 이동함으로써 1번 벽장을 사용할 수 있다. 이때 2번 벽장은 닫혀져 사용할 수 없다. 역시 5번 벽장이 열려 있으므로 4번 벽장 또는 6번 벽장 앞의 벽장문을 5번 벽장 앞으로 이동시킬 수 있다.



풀어야 할 문제는 입력으로 주어지는 사용할 벽장의 순서에 따라서 벽장문을 이동하는 순서를 찾는 것이다. 이때 벽장문의 이동횟수를 최소로 하여야 한다. 입력은 다음과 같이 주어지며, 열려있는 벽장의 개수는 항상 2개이다.

예를 들어 사용할 벽장 순서가 3 1 6 5이면, 3번 앞의 문을 2번으로 옮겨서 3번 벽장을 사용하고(문 이동횟수=1), 다음에 1번과 2번 앞에 있는 문을 오른쪽으로 하나씩 옮겨서(문 이동횟수=2) 1번 벽장을 사용하며, 6번 앞에 있는 문을 왼쪽으로 옮겨서 6번 벽장을 사용하고(문 이동횟수=1), 다시 그 문을 오른쪽으로 옮겨서 5번 벽장을 사용한다(문 이동횟수=1), 따라서 문이 이동한 횟수의 합은 5이다.
### **입력**
첫 번째 줄에 벽장의 개수를 나타내는 3보다 크고 20보다 작거나 같은 하나의 정수, 두 번째 줄에 초기에 열려있는 두 개의 벽장을 나타내는 두 개의 정수, 그리고 세 번째 줄에는 사용할 벽장들의 순서의 길이(최대 20), 그리고 그 다음줄부터 사용할 벽장의 번호가 한줄에 하나씩 순서대로 주어진다.
### **출력**
벽장문의 최소 이동횟수를 화면에 출력한다.
### **예제입출력**

**예제 입력1**

```
7
2 5
4
3
1
6
5
```

**예제 출력1**

```
5
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N = int(input())
open1, open2 = map(int, input().split())

M = int(input())
arr = [int(input()) for _ in range(M)]

dp = [[[float('inf')] * (N + 1) for _ in range(N + 1)] for _ in range(M + 1)]
dp[0][open1][open2] = 0

for i in range(M):
    for j in range(1, N+1):
        for k in range(1, N+1):
            if dp[i][j][k] != float('inf'):
                current_use = arr[i]

                # 문 j를 current_use로 이동
                dp[i + 1][current_use][k] = min(dp[i + 1][current_use][k], dp[i][j][k] + abs(j - current_use))
                
                # 문 k를 current_use로 이동
                dp[i + 1][j][current_use] = min(dp[i + 1][j][current_use], dp[i][j][k] + abs(k - current_use))

result = float('inf')
for j in range(1, N+1):
    for k in range(1, N+1):
        result = min(result, dp[M][j][k])

print(result)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|31120|36|Python3|848
#### **📝해설**

**알고리즘**
```
1. DP
2. 브루트포스
```

### **다른 풀이**

```python
N = int(input())
A, B = map(int, input().split())
S = int(input())
a = [int(input()) for _ in range(S)]
# print(N,A,B,S,a)

ans=2147000000
def DFS(L,lt, rt, cnt):
  global ans
  if ans<=cnt: return 
  
  if L==S:
    ans=min(ans,cnt)
    return 
    
  n1 = abs(lt-a[L])
  n2 = abs(rt-a[L])
  if a[L]<rt: DFS(L+1,a[L], rt , cnt+n1)   # A를 움직이거나
  if lt<a[L]: DFS(L+1,lt, a[L] , cnt+n2)   # B를 움직이거나 

  
DFS(0,A,B,0)
print(ans)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
xtema|31120|40|Python3|451
#### **📝해설**

```python
N = int(input())
open1, open2 = map(int, input().split())

M = int(input())
arr = [int(input()) for _ in range(M)]

# dp[i][j][k] : i번째 작업까지 수행했을 때, 문이 j, k에 있을 때의 최소 이동 횟수

dp = [[[float('inf')] * (N + 1) for _ in range(N + 1)] for _ in range(M + 1)]
dp[0][open1][open2] = 0

for i in range(M):
    for j in range(1, N+1):
        for k in range(1, N+1):
            if dp[i][j][k] != float('inf'):
                current_use = arr[i]

                # 문 j를 current_use로 이동
                dp[i + 1][current_use][k] = min(dp[i + 1][current_use][k], dp[i][j][k] + abs(j - current_use))
                
                # 문 k를 current_use로 이동
                dp[i + 1][j][current_use] = min(dp[i + 1][j][current_use], dp[i][j][k] + abs(k - current_use))

result = float('inf')
for j in range(1, N+1):
    for k in range(1, N+1):
        result = min(result, dp[M][j][k])

print(result)
```