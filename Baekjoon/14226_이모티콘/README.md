# [14226] 이모티콘

### **난이도**
골드 4
## **📝문제**
영선이는 매우 기쁘기 때문에, 효빈이에게 스마일 이모티콘을 S개 보내려고 한다.

영선이는 이미 화면에 이모티콘 1개를 입력했다. 이제, 다음과 같은 3가지 연산만 사용해서 이모티콘을 S개 만들어 보려고 한다.

1. 화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장한다.
2. 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기 한다.
3. 화면에 있는 이모티콘 중 하나를 삭제한다.  
모든 연산은 1초가 걸린다. 또, 클립보드에 이모티콘을 복사하면 이전에 클립보드에 있던 내용은 덮어쓰기가 된다. 클립보드가 비어있는 상태에는 붙여넣기를 할 수 없으며, 일부만 클립보드에 복사할 수는 없다. 또한, 클립보드에 있는 이모티콘 중 일부를 삭제할 수 없다. 화면에 이모티콘을 붙여넣기 하면, 클립보드에 있는 이모티콘의 개수가 화면에 추가된다.

영선이가 S개의 이모티콘을 화면에 만드는데 걸리는 시간의 최솟값을 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 S (2 ≤ S ≤ 1000) 가 주어진다.
### **출력**
첫째 줄에 이모티콘을 S개 만들기 위해 필요한 시간의 최솟값을 출력한다.

예제 입력 1 
### **예제입출력**

**예제 입력1**

```
2
```

**예제 출력1**

```
2
```

**예제 입력2**

```
4
```

**예제 출력2**

```
4
```

**예제 입력3**

```
6
```

**예제 출력3**

```
5
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from collections import deque

S = int(input())

screen = 1

visited = [[False] * (S+1) for _ in range(S+1)]
visited[1][0] = True

# 현재 이모티콘 개수, 초, 클립보드 상태
q = deque([[1, 0, 0]])

while q:
    now, count, clipboard = q.popleft()

    if now == S:
        print(count)
        break
    
    if now != clipboard and not visited[now][now]:
        q.append([now, count+1, now])
    
    next = now + clipboard
    if next < S+1 and not visited[next][clipboard]:
        q.append([next, count+1, clipboard])
        visited[next][clipboard] = True
    
    next = now - 1
    if next > 0 and not visited[next][clipboard]:
        q.append([next, count+1, clipboard])
        visited[next][clipboard] = True
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|39316|92|Python3|733
#### **📝해설**

**알고리즘**
```
1. BFS
```
### **다른 풀이**

```python
S = int(input())

dp = [x for x in range((S * 2) + 1)]
dp[1] = 0
dp[0] = 1

for i in range(2, (S * 2) + 1):
    cnt = 2
    for j in range(i * 2, (S * 2) + 1, i):
        dp[j] = min(dp[i] + cnt, dp[j])
        dp[j - 1] = min(dp[j] + 1, dp[j - 1])

        cnt += 1
print(dp[S])
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
k0302jsu|31120|44|Python3|280
#### **📝해설**

```python
from collections import deque

S = int(input())

screen = 1

# 현재 화면의 이모티콘 개수, 클립보드의 이모티콘 개수 방문 여부
visited = [[False] * (S+1) for _ in range(S+1)]
visited[1][0] = True

# 현재 이모티콘 개수, 초, 클립보드 상태
q = deque([[1, 0, 0]])

while q:
    now, count, clipboard = q.popleft()

    if now == S:
        print(count)
        break
    
    # 클립보드 갱신하는 경우
    if now != clipboard and not visited[now][now]:
        q.append([now, count+1, now])
    
    # 클립보드 붙여넣는 경우
    next = now + clipboard
    if next < S+1 and not visited[next][clipboard]:
        q.append([next, count+1, clipboard])
        visited[next][clipboard] = True
    
    # -1 하는 경우
    next = now - 1
    if next > 0 and not visited[next][clipboard]:
        q.append([next, count+1, clipboard])
        visited[next][clipboard] = True
```