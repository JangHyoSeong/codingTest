# [2492] 보석

### **난이도**
골드 3
## **📝문제**
지질 탐사의 결과 지하 깊숙이 묻힌 금강석 정보를 나타내는 지도가 아래 그림처럼 만들어졌다. 지도에는 같은 간격으로 수직선과 수평선들이 그어져 있다. 금강석은 항상 수직선(경계선 포함)과 수평선(경계선 포함)이 만나는 곳에 위치하며 굵은 점으로 표시된다. 앞으로 지도의 왼쪽 변에서 A 칸 떨어진 수직선과 지도의 아래쪽 변에서 B 칸 떨어진 수평선이 만나는 곳을 (A, B)라고 표시하자. 

이제 땅을 파서 금강석을 캐려고 한다. 굴착할 영역은 항상 각 변이 지도의 경계선과 평행한 정사각형이다. 현재 보유하고 있는 예산과 굴착 기술로는 한 변의 길이가 K인 정사각형 영역에 대해 단 한 번만 팔 수 있다. 그래서 정사각형 영역에 가장 많은 금강석이 포함될 수 있도록 하려고 한다. 단, 굴착할 영역인 정사각형의 모든 꼭짓점들은 지도의 수직선(경계선 포함)과 수평선(경계선 포함)이 만나는 곳에 위치해야 하고, 정사각형 변에 놓인 금강석도 이 정사각형에 포함된 것으로 본다. 

예를 들어, 아래 그림에서 K=3인 경우 가장 많은 금강석을 포함하는 정사각형은 5개의 금강석을 포함한다. 

![이미지](https://upload.acmicpc.net/6afee9f8-bbc1-4c99-ae2e-5767893fca64/-/preview/)

지질 탐사 지도에 대한 정보를 입력받아 가장 많은 금강석을 포함하는 정사각형을 구하는 프로그램을 작성하라. 
### **입력**
첫째 줄에 4개의 정수 N, M, T, K가 빈칸을 사이에 두고 주어진다. N은 지도의 너비를 나타내고, M은 지도의 높이를 나타낸다(1 ≤ N, M ≤ 1,000,000).  T는 금강석의 개수를 나타내고, K는 정사각형의 크기(한 변의 길이)를 나타낸다. T는 1 이상 100 이하이고, K는 1 이상 1,000,000 이하로서 N과 M보다 크지 않다. 둘째 줄부터 T개의 줄에는 각 줄마다 각 금강석의 위치 (A, B)를 나타내는 두 개의 정수 A와 B가 빈칸을 사이에 두고 주어진다. A는 0 이상 N 이하이고, B는 0 이상 M 이하이다. 입력으로 주어진 금강석의 좌표들은 모두 다르다.
### **출력**
첫째 줄에 정사각형의 왼쪽 위 꼭짓점의 위치 (X, Y)를 나타내는 두 개의 정수 X, Y를 빈칸을 사이에 두고 출력한다. 둘째 줄에는 이 정사각형에 포함되는 금강석의 개수를 출력한다. 답이 여러 개 있는 경우에는 그 중 하나만 출력하라. 

정사각형은 지도 밖으로 벗어날 수 없다.
### **예제입출력**

**예제 입력1**

```
10 6 7 3
2 2
3 4
7 6
4 5
4 3
5 3
6 4
```

**예제 출력1**

```
3 5
5
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys

N, M, T, K = map(int, sys.stdin.readline().rstrip().split())
stones = [tuple(map(int, sys.stdin.readline().rstrip().split())) for _ in range(T)]

xs = {x for x, _ in stones}
ys = {y for _, y in stones}
xs.add(N - K)
ys.add(M - K)

xs = sorted(xs)
ys = sorted(ys)

max_count = 0
ans_x, ans_y = 0, 0

for X in xs:
    for Y in ys:
        if X < 0 or Y < 0 or X + K > N or Y + K > M:
            continue

        cnt = 0
        for sx, sy in stones:
            if X <= sx <= X + K and Y <= sy <= Y + K:
                cnt += 1

        if cnt > max_count:
            max_count = cnt
            ans_x, ans_y = X, Y

print(ans_x, ans_y + K)
print(max_count)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|32412|176|Python3|671
#### **📝해설**

**알고리즘**
```
1. 브루트포스
```

### **다른 풀이**

```python
import sys, itertools
input = sys.stdin.readline

N, M, T, K = map(int, input().split())
points = list(tuple(map(int, input().split())) for _ in range(T))

check_points = set(points.copy())
for cb in itertools.combinations(points, 2):
    a, b = cb
    new_point = (min(a[0], b[0]), min(a[1], b[1]))
    check_points.add(new_point)

max_count = 0
max_pos = (-1, -1)
for start_x, start_y in check_points:
    end_x, end_y = start_x + K, start_y + K

    if end_x > N:
        diff = end_x - N
        start_x -= diff
        end_x -= diff

    if end_y > M:
        diff = end_y - M
        start_y -= diff
        end_y -= diff

    cur_count = 0
    for x, y in points:
        if start_x <= x <= end_x and start_y <= y <= end_y:
            cur_count += 1

    if cur_count > max_count:
        max_count = cur_count
        max_pos = (start_x, end_y)

print(*max_pos)
print(max_count)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
fchopinof99|31120|68|Python3|887
#### **📝해설**

```python
import sys

N, M, T, K = map(int, sys.stdin.readline().rstrip().split())
stones = [tuple(map(int, sys.stdin.readline().rstrip().split())) for _ in range(T)]

# 돌의 x좌표, y좌표를 각각 set로 저장 후 정렬
xs = {x for x, _ in stones}
ys = {y for _, y in stones}

# 정사각형의 끝 점도 set에 저장
xs.add(N - K)
ys.add(M - K)

xs = sorted(xs)
ys = sorted(ys)

max_count = 0
ans_x, ans_y = 0, 0

# 후보로 가능한 모든 점들을 확인하면서
for X in xs:
    for Y in ys:

        # 인덱스를 벗어난다면 넘어감
        if X < 0 or Y < 0 or X + K > N or Y + K > M:
            continue
        
        # 현재 위치 기준으로
        cnt = 0

        # 돌들을 확인하면서 포함 가능하다면 cnt += 1
        for sx, sy in stones:
            if X <= sx <= X + K and Y <= sy <= Y + K:
                cnt += 1

        # 최대값 갱신
        if cnt > max_count:
            max_count = cnt
            ans_x, ans_y = X, Y

print(ans_x, ans_y + K)
print(max_count)
```