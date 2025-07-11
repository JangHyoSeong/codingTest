# [32069] 가로등

### **난이도**
골드 5
## **📝문제**
수직선 도로 위에 
$N$ 개의 가로등이 켜져 있다. 각 가로등의 위치는 왼쪽부터 차례대로 
$A_1 < \cdots < A_N$로 나타낼 수 있다.

위치 
$x$의 어두운 정도를, 그 위치로부터 가장 가까운 가로등까지의 거리로 정의하자. 이는 
$N$ 개의 수 
$| A_1 - x |, \cdots, | A_N - x |$ 중에서 가장 작은 값과 같다. 여기서, 
$| \cdot |$는 절댓값 기호로, 
$y \ge 0$이면 
$|y| := y$, 
$y < 0$이면 
$|y| := -y$이다.

예를 들어, 
$N = 3$ 개의 가로등이 차례대로 
$A_1 = 1$, 
$A_2 = 4$, 
$A_3 = 8$에 위치한다면, 
$0$부터 
$10$까지 각 정수 위치의 어두운 정도는 다음과 같다.

위치	 
$0$ 	 
$1$ 	 
$2$ 	 
$3$ 	 
$4$ 	 
$5$ 	 
$6$ 	 
$7$ 	 
$8$ 	 
$9$ 	 
$10$ 
어두운 정도	 
$1$ 	 
$0$ 	 
$1$ 	 
$1$ 	 
$0$ 	 
$1$ 	 
$2$ 	 
$1$ 	 
$0$ 	 
$1$ 	 
$2$ 
가로등이 있는가?		○			○				○		
 
$x = 0$부터 
$x = L$까지 
$L+1$ 개의 정수 위치의 어두운 정도를 모두 계산했을 때, 가장 작은 값부터 
$K$ 번째로 작은 값까지 차례대로 출력하는 프로그램을 작성하라.
### **입력**
첫 줄에 세 정수 
$L$, 
$N$, 
$K$가 공백으로 구분되어 차례대로 주어진다.

그다음 줄에 
$N$ 개의 정수 
$A\_1, \cdots, A\_N$이 공백으로 구분되어 차례대로 주어진다.
### **출력**
첫 줄부터 
$K$ 개의 줄에 걸쳐 답을 출력한다. 이 중 
$i$ 번째 줄에는 
$i$ 번째로 작은 어두운 정도의 값을 출력한다.
### **예제입출력**

**예제 입력1**

```
10 3 4
1 4 8
```

**예제 출력1**

```
0
0
0
1
```

**예제 입력2**

```
4 5 5
0 1 2 3 4
```

**예제 출력2**

```
0
0
0
0
0
```

**예제 입력3**

```
7 1 4
3
```

**예제 출력3**

```
0
1
1
2
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys
from collections import deque

L, N, K = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

q = deque()
for pos in arr:
    q.append((pos, 0))

visited = set(arr)
count = 0

while q:

    if count == K:
        break

    now_pos, dist = q.popleft()
    print(dist)

    for d in [1, -1]:
        next_pos = now_pos + d

        if 0 <= next_pos <= L and next_pos not in visited:
            q.append((next_pos, dist + 1))
            visited.add(next_pos)
    
    count += 1
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|255264|588|PyPy3|545
#### **📝해설**

**알고리즘**
```
1. BFS
2. 해쉬
```


### **다른 풀이**

```python
l,n,k = (map(int,input().split()))
l_li = list((map(int,input().split())))
l_li2 = []
k_li = [0] * 500001
for i in range(1,len(l_li)):
    l_li2.append(l_li[i] - l_li[i-1]-1)
for i in range(len(l_li2)):
    k_li[min(l_li2[i] // 2,500000)] += 1
    k_li[min(l_li2[i] // 2 + l_li2[i] % 2,500000)] += 1
k_li[min(l_li[0],500000)] += 1
k_li[min(l - l_li[-1],500000)] += 1
if n >= k:
    print("0\n"*k,end="")
else:
    print("0\n"*n,end="")
    k -= n
    cnt = n*2
    inx = 1
    while True:
        cnt -= k_li[inx-1]
        if cnt >= k:
            print((str(inx)+"\n")*k,end="")
            break
        else:
            print((str(inx)+"\n")*cnt,end="")
        k -= cnt
        inx+=1
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
rjs38|197572|216|PyPy3|704
#### **📝해설**

```python
import sys
from collections import deque

L, N, K = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

# 큐를 사용해 현재 가로등의 위치와 가로등까지 떨어진 거리를 저장
q = deque()
for pos in arr:
    q.append((pos, 0))

# visited에서 set을 사용해서 방문했던 위치를 저장
visited = set(arr)
count = 0

# BFS
while q:

    # K번 반복했다면 종료
    if count == K:
        break
    
    # 현재 위치, 가로등과 떨어진 거리
    now_pos, dist = q.popleft()
    print(dist)

    # 앞뒤로 이동하면서
    for d in [1, -1]:
        next_pos = now_pos + d

        # 인덱스를 벗어나지 않고 방문하지 않은 위치라면
        if 0 <= next_pos <= L and next_pos not in visited:

            # 방문
            q.append((next_pos, dist + 1))
            visited.add(next_pos)
    
    count += 1
```