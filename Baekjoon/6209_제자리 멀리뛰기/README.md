# [6209] 제자리 멀리뛰기

### **난이도**
골드 2
## **📝문제**
GSHS에서는 체력측정에서 제자리 멀리뛰기가 가장 중요하다. GSHS의 체육선생님께서는 학생들의 제자리 멀리뛰기 실력을 키워주게 하기 위해서 특수 훈련을 준비중이다.

특수 훈련장소는 GSHS특수 트레이닝 센터로 이 곳은 끓는 용암으로 가득 차 있다. 체육선생님께서는 이 용암으로 가득찬 방의 가운데 있는 돌섬에 학생들을 가두고 학생들이 탈출해 나오기를 기대하고 있다. 탈출할 수 있는 방법은 단 한가지 이다. 돌섬에서 탈출구까지 띄엄 띄엄 존재하는 작은 돌섬들로 점프하여 탈출구까지 가는 것이다.

돌섬에서 탈출구 사이에는 총 n개의 작은 돌섬이 있다. 선생님은 이 n개의 작은 돌섬들 중 m개를 제거하여 학생들이 최대한 멀리뛰기 연습의 효율을 높이기 위해서 학생들이 각 돌섬을 점프한 거리의 최솟값을 최대한 크게 하려고 한다. 물론 학생들은 체력이 좋기 때문에 두 돌섬이 아무리 멀더라도 점프할 수 있다. 즉, 빠지는 일은 없다.

그리고 학생들은 탈출 시 n-m개의 모든 돌섬을 밟으면서 탈출해야 한다.

학 생들이 갇힌 돌섬으로부터 탈출구까지의 거리 d가 주어지고, 각 n개의 작은 돌섬의 위치(갇힌 돌섬으로 부터의 거리)가 주어지며, 제거할 수 있는 작은 돌섬의 수 m이 주어질 때, m개를 제거한 후 학생들이 점프하는 최소거리의 최댓값을 구하는 프로그램을 작성하시오.
### **입력**
첫 번째 줄에는 갇힌 돌섬으로부터 탈출구까지의 거리 d(1 ≤ d ≤ 1,000,000,000), 작은 돌섬의 수 n(0 ≤ n ≤ 50,000), 제거할 수 있는 작은 돌섬의 수 m (0 ≤ m ≤ n)이 공백으로 구분되어 주어진다.

두 번째 줄부터 n줄에 걸쳐서 갇힌섬으로부터 각 작은 돌섬이 얼마나 떨어져 있는지를 나타내는 하나의 정수가 한 줄에 하나씩 주어진다. (단, 두 돌섬은 같은 위치에 있을 수 없다.)
### **출력**
m개의 작은섬을 제거한 뒤 학생들이 점프할 수 있는 최소거리의 최댓값을 출력한다.
### **예제입출력**

**예제 입력1**

```
25 5 2
2
14
11
21
17
```

**예제 출력1**

```
4
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys

d, n, m = map(int, sys.stdin.readline().rstrip().split())
rocks = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

rocks.sort()
rocks = [0] + rocks + [d]

left, right = 1, d
result = 0

while left <= right:
    mid = (left + right) // 2
    prev = 0
    remove_count = 0

    for i in range(1, len(rocks)):
        if rocks[i] - rocks[prev] < mid:
            remove_count += 1
        else:
            prev = i

    if remove_count > m:
        right = mid - 1
    else:
        result = mid
        left = mid + 1

print(result)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|112252|124|PyPy3|550
#### **📝해설**

**알고리즘**
```
1. 이분 탐색
2. 그리디 알고리즘
```

#### **📝해설**

```python
import sys

d, n, m = map(int, sys.stdin.readline().rstrip().split())
rocks = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

# 돌을 오름차순으로 정렬, 시작 위치와 끝 위치를 추가함
rocks.sort()
rocks = [0] + rocks + [d]

# 이분 탐색을 통해 값을 찾음. 최대 최소값을 정의
left, right = 1, d
result = 0

# 이분 탐색
while left <= right:
    mid = (left + right) // 2

    # 이전의 돌의 인덱스
    prev = 0

    # 돌을 제거한 숫자
    remove_count = 0

    # 돌들을 검사하면서
    for i in range(1, len(rocks)):

        # 거리가 mid보다 작으면 돌을 제거
        if rocks[i] - rocks[prev] < mid:
            remove_count += 1

        # 거리가 충분한 돌을 밟음
        else:
            prev = i

    # 제거한 돌이 m보다 많다면
    if remove_count > m:
        # 최소 거리를 줄임
        right = mid - 1
    
    # 제거한 돌이 m이하라면
    else:
        # 값을 갱신, 최소 거리를 늘림
        result = mid
        left = mid + 1

print(result)
```