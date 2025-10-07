# [2792] 보석 상자

### **난이도**
실버 1
## **📝문제**
보석 공장에서 보석 상자를 유치원에 기증했다. 각각의 보석은 M가지 서로 다른 색상 중 한 색상이다. 원장 선생님은 모든 보석을 N명의 학생들에게 나누어 주려고 한다. 이때, 보석을 받지 못하는 학생이 있어도 된다. 하지만, 학생은 항상 같은 색상의 보석만 가져간다.

한 아이가 너무 많은 보석을 가져가게 되면, 다른 아이들이 질투를 한다. 원장 선생님은 이런 질투심을 수치화하는데 성공했는데, 질투심은 가장 많은 보석을 가져간 학생이 가지고 있는 보석의 개수이다. 원장 선생님은 질투심이 최소가 되게 보석을 나누어 주려고 한다.

상자에 빨간 보석이 4개 (RRRR), 파란 보석이 7개 (BBBBBBB) 있었고, 이 보석을 5명의 아이들에게 나누어 주는 경우를 생각해보자. RR, RR, BB, BB, BBB로 보석을 나누어주면 질투심은 3이 되고, 이 값보다 작게 나누어 줄 수 없다.

상자 안의 보석 정보와 학생의 수가 주어졌을 때, 질투심이 최소가 되게 보석을 나누어주는 방법을 알아내는 프로그램을 작성하시오.
### **입력**
첫째 줄에 아이들의 수 N과 색상의 수 M이 주어진다. (1 ≤ N ≤ 109, 1 ≤ M ≤ 300,000, M ≤ N)

다음 M개 줄에는 구간 [1, 109]에 포함되는 양의 정수가 하나씩 주어진다. K번째 줄에 주어지는 숫자는 K번 색상 보석의 개수이다.
### **출력**
첫째 줄에 질투심의 최솟값을 출력한다.
### **예제입출력**

**예제 입력1**

```
5 2
7
4
```

**예제 출력1**

```
3
```

**예제 입력2**

```
7 5
7
1
7
4
4
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

N, M = map(int, sys.stdin.readline().rstrip().split())
jewels = [int(sys.stdin.readline().rstrip()) for _ in range(M)]

left, right = 1, max(jewels)
answer = right

while left <= right:
    mid = (left + right) // 2
    total = 0

    for jewel in jewels:
        total += (jewel + mid - 1) // mid
        if total > N:
            break
    
    if total <= N:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|113216|272|PyPy3|466
#### **📝해설**

**알고리즘**
```
1. 이분 탐색
```

### **다른 풀이**

```python
import io, os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def check(mid):
    tot = 0
    for x in a:
        tot += (x+mid-1)//mid
        if tot > n: return False
    
    return True
    # return sum((x+mid-1)//mid for x in a) <= n

n, m = map(int, input().split())
a = [int(input()) for _ in range(m)]

lo, hi = 1, max(a)
while lo <= hi:
    mid = (lo+hi)>>1
    if check(mid): hi = mid-1
    else: lo = mid+1

print(lo)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
mhc|119056|240|PyPy3|442
#### **📝해설**

```python
import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
jewels = [int(sys.stdin.readline().rstrip()) for _ in range(M)]

# 최소, 최대 질투심
left, right = 1, max(jewels)

# 초기 정답은 최대값으로 설정
answer = right

# 이분탐색
while left <= right:

    # 가운데값
    mid = (left + right) // 2

    # 현재 총 질투심
    total = 0

    # 모든 보석을 나누면서
    for jewel in jewels:

        # 현재의 질투심으로 몇 명의 학생에게 나누어 줄 수 있는지 확인
        total += (jewel + mid - 1) // mid
        
        # N을 넘긴다면 끝까지 계산하지 않아도 됨
        if total > N:
            break
    
    # 나누어 주는 학생 수가 N보다 작다면
    if total <= N:

        # 질투심을 더 낮춰도 됨
        answer = mid
        right = mid - 1
    
    # 나누어 주는 학생 수가 N보다 크다면
    else:

        # 질투심이 더 커야함
        left = mid + 1

print(answer)
```