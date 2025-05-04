# [8983] 사냥꾼

### **난이도**
골드 4
## **📝문제**
KOI 사냥터에는 N 마리의 동물들이 각각 특정한 위치에 살고 있다. 사냥터에 온 사냥꾼은 일직선 상에 위치한 M 개의 사대(총을 쏘는 장소)에서만 사격이 가능하다. 편의상, 일직선을 x-축이라 가정하고, 사대의 위치 x1, x2, ..., xM은 x-좌표 값이라고 하자. 각 동물이 사는 위치는 (a1, b1), (a2, b2), ..., (aN, bN)과 같이 x,y-좌표 값으로 표시하자. 동물의 위치를 나타내는 모든 좌표 값은 양의 정수이다.

사냥꾼이 가지고 있는 총의 사정거리가 L이라고 하면, 사냥꾼은 한 사대에서 거리가 L 보다 작거나 같은 위치의 동물들을 잡을 수 있다고 한다. 단, 사대의 위치 xi와 동물의 위치 (aj, bj) 간의 거리는 |xi-aj| + bj로 계산한다.

예를 들어, 아래의 그림과 같은 사냥터를 생각해 보자. (사대는 작은 사각형으로, 동물의 위치는 작은 원으로 표시되어 있다.) 사정거리 L이 4라고 하면, 점선으로 표시된 영역은 왼쪽에서 세 번째 사대에서 사냥이 가능한 영역이다.

[이미지](https://upload.acmicpc.net/80de7dba-b822-4f30-b833-de3071af385b/-/preview/)

사대의 위치와 동물들의 위치가 주어졌을 때, 잡을 수 있는 동물의 수를 출력하는 프로그램을 작성하시오.
### **입력**
입력의 첫 줄에는 사대의 수 M (1 ≤ M ≤ 100,000), 동물의 수 N (1 ≤ N ≤ 100,000), 사정거리 L (1 ≤ L ≤ 1,000,000,000)이 빈칸을 사이에 두고 주어진다. 두 번째 줄에는 사대의 위치를 나타내는 M개의 x-좌표 값이 빈칸을 사이에 두고 양의 정수로 주어진다. 이후 N개의 각 줄에는 각 동물의 사는 위치를 나타내는 좌표 값이 x-좌표 값, y-좌표 값의 순서로 빈칸을 사이에 두고 양의 정수로 주어진다. 사대의 위치가 겹치는 경우는 없으며, 동물들의 위치가 겹치는 경우도 없다. 모든 좌표 값은 1,000,000,000보다 작거나 같은 양의 정수이다.
### **출력**
출력은 단 한 줄이며, 잡을 수 있는 동물의 수를 음수가 아닌 정수로 출력한다.
### **예제입출력**

**예제 입력1**

```
4 8 4
6 1 4 9
7 2
3 3
4 5
5 1
2 2
1 4
8 4
9 4
```

**예제 출력1**

```
6
```

**예제 입력2**

```
1 5 3
3
2 2
1 1
5 1
4 2
3 3
```

**예제 출력2**

```
5
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys
import bisect

M, N, L = map(int, sys.stdin.readline().rstrip().split())
shooting_places = list(map(int, sys.stdin.readline().rstrip().split()))
animals = [tuple(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

shooting_places.sort()
count = 0

for animal in animals:
    x, y = animal

    if y > L:
        continue

    left = x - (L - y)
    right = x + (L - y)

    idx = bisect.bisect_left(shooting_places, left)

    if idx < M and shooting_places[idx] <= right:
        count += 1
    
print(count)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|127636|216|PyPy3|537
#### **📝해설**

**알고리즘**
```
1. 이분탐색
```

### **다른 풀이**

```python
import sys

input = sys.stdin.readline


m, n, shotRange = map(int, input().split())
spots = sorted(list(map(int, input().split())))

answer = 0
for _ in range(n):
    x, y = map(int, input().split())

    minSpot = x + y - shotRange
    maxSpot = x - y + shotRange

    left = 0
    right = m - 1

    while left <= right:
        mid = (left + right) // 2

        if minSpot <= spots[mid] <= maxSpot:
            answer += 1
            break
        elif maxSpot < spots[mid]:
            right = mid - 1
        else:
            left = mid + 1

print(answer)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
codeer|126916|188|PyPy3|565
#### **📝해설**

```python
import sys
import bisect

M, N, L = map(int, sys.stdin.readline().rstrip().split())
shooting_places = list(map(int, sys.stdin.readline().rstrip().split()))
animals = [tuple(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

# 사대를 이분 탐색을 위해 정렬함
shooting_places.sort()
count = 0

# 모든 동물들을 검사
for animal in animals:
    x, y = animal

    # 만약 y좌표만으로 사정거리를 벗어난다면 절대 맞출수 없으니 넘어감
    if y > L:
        continue
    
    # 이 동물을 맞출 수 있는 사대의 최소 x 좌표
    left = x - (L - y)
    # 최대 x 좌표
    right = x + (L - y)

    # 이분탐색을 통해 사대의 좌표를 찾음
    idx = bisect.bisect_left(shooting_places, left)

    # idx가 M인 경우 범위에 포함되지 않음
    if idx < M and shooting_places[idx] <= right:
        count += 1
    
print(count)
```