# [29891] 문체크포인트 달리기

### **난이도**
실버 4
## **📝문제**
철수는 체크포인트 달리기라는 경기에 출전했다. 체크포인트 달리기란 출발점에서 출발하여 길에 있는 모든 체크포인트에 최소 한 번씩 체크하고 출발점으로 돌아오는 경기이다. 출발점은 원점에 있고, 일직선으로 뻗은 길에 
$N$개의 체크포인트가 있다. 
$i$번째 체크포인트는 좌표 
$x_i$에 있다.

체크포인트 달리기에는 특별한 규칙이 있는데, 출발점에서 출발하여 출발점으로 돌아오기 전까지 최대 
$K$개의 체크포인트에만 체크할 수 있다. 예를 들어 
$K$가 
$3$이라면, 출발점에서 출발하여 
$3$개의 체크포인트를 체크하고, 출발점으로 돌아온 뒤, 다시 다른 체크포인트를 향해 달려가야 한다. 체크포인트를 체크하지 않고 지나칠 수도 있다.

철수가 이동 거리를 최소화하면서 모든 체크포인트를 체크할 수 있게 도와주자.
### **입력**
첫 번째 줄에 체크포인트의 개수 
$N$과 한 번에 체크할 수 있는 체크포인트의 개수 
$K$가 주어진다.

이후 
$N$개의 줄에 체크포인트의 위치 
$x_i$가 주어진다.
### **출력**
철수가 이동 거리를 최소화하면서 모든 체크포인트를 체크할 때, 그 이동 거리를 출력한다.

### 제한
- 주어지는 모든 수는 정수이다.
- $1 <= N <= 200000$
- $1 <= K <= N
- $-10^9 <= x_i <= 10^9$

### **예제입출력**

**예제 입력1**

```
4 2
1
2
3
4
```

**예제 출력1**

```
12
```

**예제 입력2**

```
3 1
1
2
3
```

**예제 출력2**

```
12
```

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N, K = map(int, input().split())

checkpoints_plus = []
checkpoints_minus = []
for i in range(N):
    temp_num = int(input())
    if temp_num > 0:
        checkpoints_plus.append(temp_num)
    else:
        checkpoints_minus.append(temp_num)

move_range = 0

checkpoints_minus.sort()
checkpoints_plus.sort(reverse=True)

minus_len = len(checkpoints_minus)
plus_len = N - minus_len

idx = 0
while idx < minus_len:
    move_range += abs(checkpoints_minus[idx])
    idx += K
    
idx = 0
while idx < plus_len:
    move_range += checkpoints_plus[idx]
    idx += K
    
print(move_range * 2)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|120476|252|PyPy3|586
#### **📝해설**

**알고리즘**
```
1. 정렬
2. 그리디 알고리즘
```

#### **😅개선점**


### **다른 풀이**

```python
import sys


n, k = (int(x) for x in sys.stdin.readline().split())
pos, neg = [], []
for _ in range(n):
    x = int(sys.stdin.readline())
    if x > 0:
        pos.append(x)
    elif x < 0:
        neg.append(-x)
pos.sort(reverse=True)
neg.sort(reverse=True)
print(2 * (sum(pos[::k]) + sum(neg[::k])))

```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
thenitromefan|40096|184|Python3|302
#### **📝해설**

```python
N, K = map(int, input().split())

# 양수와 음수를 각각 담음
checkpoints_plus = []
checkpoints_minus = []

# 숫자를 입력받으면서 양수면 양수 리스트, 음수면 음수 리스트에 삽입
for i in range(N):
    temp_num = int(input())
    if temp_num > 0:
        checkpoints_plus.append(temp_num)
    else:
        checkpoints_minus.append(temp_num)

# 이동 거리
move_range = 0

# 각 리스트를 정렬함 (절대값으로 큰 수가 앞에 가게)
checkpoints_minus.sort()
checkpoints_plus.sort(reverse=True)

# 각 리스트의 길이를 변수에 저장
minus_len = len(checkpoints_minus)
plus_len = N - minus_len

# 가장 멀리있는 체크포인트에 방문하고, K개 만큼 인덱스를 증가
idx = 0
while idx < minus_len:
    move_range += abs(checkpoints_minus[idx])
    idx += K

# 양수도 동일한 연산 진행  
idx = 0
while idx < plus_len:
    move_range += checkpoints_plus[idx]
    idx += K

# 왕복이므로 * 2
print(move_range * 2)
```