# [15961] 회전 초밥

### **난이도**
골드 4
## **📝문제**
회전 초밥 음식점에는 회전하는 벨트 위에 여러 가지 종류의 초밥이 접시에 담겨 놓여 있고, 손님은 이 중에서 자기가 좋아하는 초밥을 골라서 먹는다. 초밥의 종류를 번호로 표현할 때, 다음 그림은 회전 초밥 음식점의 벨트 상태의 예를 보여주고 있다. 벨트 위에는 같은 종류의 초밥이 둘 이상 있을 수 있다. 

![이미지](https://upload.acmicpc.net/f29f0bd9-6114-4543-aa72-797208dc9cdd/-/preview/)

새로 문을 연 회전 초밥 음식점이 불경기로 영업이 어려워서, 다음과 같이 두 가지 행사를 통해서 매상을 올리고자 한다.

1. 원래 회전 초밥은 손님이 마음대로 초밥을  고르고, 먹은 초밥만큼 식대를 계산하지만, 벨트의 임의의 한 위치부터 k개의 접시를 연속해서 먹을 경우 할인된 정액 가격으로 제공한다. 
2. 각 고객에게 초밥의 종류 하나가 쓰인 쿠폰을 발행하고, 1번 행사에 참가할 경우 이 쿠폰에 적혀진 종류의 초밥 하나를 추가로 무료로 제공한다. 만약 이 번호에 적혀진 초밥이 현재 벨트 위에 없을 경우, 요리사가 새로 만들어 손님에게 제공한다.    

위 할인 행사에 참여하여 가능한 한 다양한 종류의 초밥을 먹으려고 한다. 위 그림의 예를 가지고 생각해보자. k=4이고, 30번 초밥을 쿠폰으로 받았다고 가정하자. 쿠폰을 고려하지 않으면 4가지 다른 초밥을 먹을 수 있는 경우는 (9, 7, 30, 2), (30, 2, 7, 9), (2, 7, 9, 25) 세 가지 경우가 있는데, 30번 초밥을 추가로 쿠폰으로 먹을 수 있으므로 (2, 7, 9, 25)를 고르면 5가지 종류의 초밥을 먹을 수 있다. 

회전 초밥 음식점의 벨트 상태, 메뉴에 있는 초밥의 가짓수, 연속해서 먹는 접시의 개수, 쿠폰 번호가 주어졌을 때, 손님이 먹을 수 있는 초밥 가짓수의 최댓값을 구하는 프로그램을 작성하시오. 
### **입력**
첫 번째 줄에는 회전 초밥 벨트에 놓인 접시의 수 N, 초밥의 가짓수 d, 연속해서 먹는 접시의 수 k, 쿠폰 번호 c가 각각 하나의 빈 칸을 사이에 두고 주어진다. 단, 2 ≤ N ≤ 3,000,000, 2 ≤ d ≤ 3,000, 2 ≤ k ≤ 3,000 (k ≤ N), 1 ≤ c ≤ d이다. 두 번째 줄부터 N개의 줄에는 벨트의 한 위치부터 시작하여 회전 방향을 따라갈 때 초밥의 종류를 나타내는 1 이상 d 이하의 정수가 각 줄마다 하나씩 주어진다. 
### **출력**
주어진 회전 초밥 벨트에서 먹을 수 있는 초밥의 가짓수의 최댓값을 하나의 정수로 출력한다.
### **예제입출력**

**예제 입력1**

```
8 30 4 30
7
9
7
30
2
7
9
25
```

**예제 출력1**

```
5
```

**예제 입력2**

```
8 50 4 7
2
7
9
25
7
9
7
30
```

**예제 출력2**

```
4
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys
from collections import defaultdict

N, d, k, c = map(int, sys.stdin.readline().rstrip().split())
arr = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
arr.extend(arr[:k-1])

current_window = defaultdict(int)
count = 0
max_count = 0

for i in range(k):
    if current_window[arr[i]] == 0:
        count += 1
    current_window[arr[i]] += 1

if current_window[c] == 0:
    max_count = count + 1
else:
    max_count = count

for i in range(1, N):
    removed_sushi = arr[i-1]
    current_window[removed_sushi] -= 1
    if current_window[removed_sushi] == 0:
        count -= 1

    added_sushi = arr[i+k-1]
    if current_window[added_sushi] == 0:
        count += 1
    current_window[added_sushi] += 1

    if current_window[c] == 0:
        max_count = max(max_count, count + 1)
    else:
        max_count = max(max_count, count)

print(max_count)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|165172|764|PyPy3|867
#### **📝해설**

**알고리즘**
```
1. 슬라이딩 윈도우
```

### **다른 풀이**

```python
import sys
n,d,k,c=map(int,sys.stdin.readline().rstrip().split())
g=[int(sys.stdin.readline().rstrip()) for _ in range(n)]  
v=[0 for _ in range(d+1)]
v[c]=1
for i in range(k):
    v[g[i]]+=1
cnt=d-v.count(0)+1
ans=cnt
for i in range(n):
    v[g[i]]-=1
    if not v[g[i]]:cnt-=1
    try:
        if not v[g[i+k]]:cnt+=1
        v[g[i+k]]+=1
    except:
        if not v[g[i+k-n]]:cnt+=1
        v[g[i+k-n]]+=1
    ans=max(ans,cnt)
print(ans)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
k550706|134760|556|PyPy3|441
#### **📝해설**

```python
import sys
from collections import defaultdict

# 입력받기
N, d, k, c = map(int, sys.stdin.readline().rstrip().split())
arr = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

# 순환을 위해서 k만큼 뒤에 덧붙임
arr.extend(arr[:k-1])

# 현재 k개 동안 포함된 스시를 셀 딕셔너리
current_window = defaultdict(int)

# 현재 초밥 종류
count = 0

# 최대 초밥 종류
max_count = 0

# 일단 리스트의 처음부터 k개만큼 초밥을 채움
for i in range(k):
    # 아직 포함되지 않은 초밥의 종류면 종류 ++
    if current_window[arr[i]] == 0:
        count += 1

    # 이 초밥의 개수를 늘림
    current_window[arr[i]] += 1

# 만약 이번 초밥에서 쿠폰 초밥이 포함되어 있지 않다면
if current_window[c] == 0:

    # 개수를 하나 늘림
    max_count = count + 1

# 포함되어 있다면 개수를 늘리지 않음
else:
    max_count = count

# 슬라이딩 윈도우
for i in range(1, N):

    # 맨 앞의 초밥을 제거
    removed_sushi = arr[i-1]
    current_window[removed_sushi] -= 1
    if current_window[removed_sushi] == 0:
        count -= 1

    # 초밥을 하나 추가
    added_sushi = arr[i+k-1]
    if current_window[added_sushi] == 0:
        count += 1
    current_window[added_sushi] += 1

    if current_window[c] == 0:
        max_count = max(max_count, count + 1)
    else:
        max_count = max(max_count, count)

print(max_count)
```