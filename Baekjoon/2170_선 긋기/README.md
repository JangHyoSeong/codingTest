# [2170] 선 긋기

### **난이도**
골드 5
## **📝문제**
매우 큰 도화지에 자를 대고 선을 그으려고 한다. 선을 그을 때에는 자의 한 점에서 다른 한 점까지 긋게 된다. 선을 그을 때에는 이미 선이 있는 위치에 겹쳐서 그릴 수도 있는데, 여러 번 그은 곳과 한 번 그은 곳의 차이를 구별할 수 없다고 하자.

이와 같은 식으로 선을 그었을 때, 그려진 선(들)의 총 길이를 구하는 프로그램을 작성하시오. 선이 여러 번 그려진 곳은 한 번씩만 계산한다.
### **입력**
첫째 줄에 선을 그은 횟수 N (1 ≤ N ≤ 1,000,000)이 주어진다. 다음 N개의 줄에는 선을 그을 때 선택한 두 점의 위치 x, y (-1,000,000,000 ≤ x < y ≤ 1,000,000,000)가 주어진다.
### **출력**
첫째 줄에 그은 선의 총 길이를 출력한다.
### **예제입출력**

**예제 입력1**

```
4
1 3
2 5
3 5
6 7
```

**예제 출력1**

```
5
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys

N = int(sys.stdin.readline().rstrip())
lines = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

lines.sort()

total_length = 0
cur_start, cur_end = lines[0]

for x, y in lines[1:]:

    if x <= cur_end:
        cur_end = max(cur_end, y)
    
    else:
        total_length += cur_end - cur_start
        cur_start, cur_end = x, y

total_length += cur_end - cur_start
print(total_length)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|242340|3512|PyPy3|424
#### **📝해설**

**알고리즘**
```
1. 정렬
```

### **다른 풀이**

```python
import sys
input = sys.stdin.readline

""" Solution 1) """
# res = 0
# l = r = -1000000000
# for x, y in sorted(tuple(map(int, input().split())) for _ in range(int(input()))):
#     if x>r:
#         res += y-x
#         l, r = x, y
#     else:
#         if y>r:
#             res += y-r
#             r = y

# print(res)

""" Solution 2) """
l, r = [], []
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    l.append(x)
    r.append(y)

l.sort(); r.sort()

res = r[0]-l[0]
for i in range(1, n):
    if l[i] > r[i-1]: res += r[i]-l[i]
    else: res += r[i]-r[i-1]

print(res)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
mhc|209204|788|PyPy3|600
#### **📝해설**

```python
import sys

N = int(sys.stdin.readline().rstrip())
lines = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

# 각 선을 정렬
lines.sort()

total_length = 0

# 현재 끝까지 이어진 선분의 시작과 끝
cur_start, cur_end = lines[0]

# 선분들을 확인하면서
for x, y in lines[1:]:

    # 현재 시작점이 끝점과 겹치거나 작다면
    if x <= cur_end:

        # 끝점을 갱신(하나의 선분으로 이어짐)
        cur_end = max(cur_end, y)
    
    # 그게 아니라면
    else:

        # 현재까지 길이를 저장
        total_length += cur_end - cur_start

        # 다시 시작과 끝점 정의
        cur_start, cur_end = x, y

# 마지막으로 한번 더해줌
total_length += cur_end - cur_start
print(total_length)
```