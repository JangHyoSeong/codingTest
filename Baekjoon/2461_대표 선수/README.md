# [2461] 대표 선수

### **난이도**
골드 2
## **📝문제**
KOI 중학교에는 N개의 학급이 있으며, 각 학급의 학생 수는 모두 M명으로 구성된다. 이 중학교에서는 체육대회에 새로운 종목의 경기를 추가하였다. 이 경기에 대해 모든 학생들은 저마다의 능력을 나타내는 능력치를 가지고 있으며, 이 능력치는 모든 학생이 서로 다르다.

이 경기는 한반에서 한 명의 대표선수를 선발하여 치른다. 경기의 형평성을 위하여, 각각의 반에서 대표로 선발된 모든 학생들의 능력치 중 최댓값과 최솟값의 차이가 최소가 되도록 선수를 선발하려고 한다. 예를 들어, N=3, M=4인 경우 학생들의 능력치가 1반=[12, 16, 67, 43],  2반=[7, 17, 68, 48], 3반=[14, 15, 77, 54]로 주어질 때, 각 학급으로부터 능력치 16, 17, 15를 가진 학생을 각각 선택하면, 최댓값과 최솟값의 차이가 17-15=2로 최소가 된다. 

대표로 선발된 모든 학생들 능력치의 최댓값과 최솟값 차이가 최소가 되는 경우의 값을 출력하는 프로그램을 작성하시오.
### **입력**
입력의 첫 번째 줄에는 학급의 수를 나타내는 N과 각 학급의 학생의 수를 나타내는 M이 하나의 빈칸을 사이에 두고 주어진다. 단, 1 ≤ N, M ≤ 1,000이다. 두 번째 줄부터 N개의 줄에는 각 줄마다 한 학급 학생들의 능력치를 나타내는 M개의 양의 정수가 하나의 빈칸을 사이에 두고 주어진다. 능력치는 0이상 109이하이다.
### **출력**
대표로 선발된 모든 학생들 능력치의 최댓값과 최솟값 차이가 최소가 되는 경우의 값을 하나의 정수로 출력한다.
### **예제입출력**

**예제 입력1**

```
3 4
12 16 67 43
7 17 68 48
14 15 77 54
```

**예제 출력1**

```
2
```

**예제 입력2**

```
4 3
10 20 30
40 50 60
70 80 90
100 110 120
```

**예제 출력2**

```
70
```
### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
arr = []
for class_id in range(N):
    team = list(map(int, sys.stdin.readline().rstrip().split()))

    for value in team:
        arr.append((value, class_id))
    
arr.sort(key=lambda x: x[0])

count = [0] * N
covered = 0
answer = int(10e9)

left = 0
for right in range(len(arr)):
    value_right, class_right = arr[right]

    if count[class_right] == 0:
        covered += 1
    
    count[class_right] += 1

    while covered == N:
        value_left, class_left = arr[left]
        answer = min(answer, value_right - value_left)

        count[class_left] -= 1
        if count[class_left] == 0:
            covered -= 1
        
        left += 1

if N == 1:
    print(0)
else:
    print(answer)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|144036|1804|Python3|770
#### **📝해설**

**알고리즘**
```
1. 투 포인터
2. 최소 힙
```

### **다른 풀이**

```python
"""

"""
import sys, heapq

fin = sys.stdin.read().split('\n')
n_class, n_student = map(int, fin[0].split())
ability = []
for idx in range(1,1+n_class):
    ability.append(list(map(int, fin[idx].split())))

def solve(n_class: int, n_student: int, ability: list[list[int]]):
    for abty in ability: abty.sort()

    idx = [0 for _ in range(n_class)]
    heap = [(ability[src][0], src) for src in range(n_class)]
    heapq.heapify(heap)
    heap_max = max(heap, key=lambda s: s[0])[0]

    ans = 1000000001

    while heap:
        heap_min, src = heapq.heappop(heap)
        ans = min(ans, heap_max - heap_min)

        idx[src] += 1
        if idx[src] == n_student: break

        heapq.heappush(heap, (ability[src][idx[src]], src))
        heap_max = max(heap_max, ability[src][idx[src]])

    return ans

print(solve(n_class, n_student, ability))

```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
irhi_2077|148620|624|PyPy3|851
#### **📝해설**

```python
import sys

# 입력받기
N, M = map(int, sys.stdin.readline().rstrip().split())

# 모든 학생들의 점수를 한 리스트에 저장
arr = []
for class_id in range(N):
    team = list(map(int, sys.stdin.readline().rstrip().split()))

    # (점수, 반)이 되도록 저장
    for value in team:
        arr.append((value, class_id))

# 학생을 점수별로 정렬
arr.sort(key=lambda x: x[0])


# 투 포인터를 통해 모든 학생들을 포함하면서, 각 반에서 몇명이 뽑혔는지 검사

# 각 반에서 몇 명이 포함됐는지 저장할 리스트
count = [0] * N

# 현재 몇 반이 골라졌는지 저장할 변수
covered = 0
answer = int(10e9)

# 투포인터 설정
left = 0

# right는 0에서부터 시작
for right in range(len(arr)):

    value_right, class_right = arr[right]

    # 아직 포함되지 않았던 반이라면 += 1
    if count[class_right] == 0:
        covered += 1
    
    count[class_right] += 1

    # 현재 모든 반이 포함된 상태라면
    while covered == N:
        value_left, class_left = arr[left]

        # 최소값이 갱신이 가능하다면 갱신
        answer = min(answer, value_right - value_left)

        # left를 하나 늘림
        count[class_left] -= 1
        if count[class_left] == 0:
            covered -= 1
        
        left += 1

# 출력
if N == 1:
    print(0)
else:
    print(answer)
```