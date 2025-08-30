# [2073] 수도배관공사

### **난이도**
골드 4
## **📝문제**
아기염소들이 언덕에서 풀을 뜯고 놀다 보면 항상 도중에 목이 마르곤 했다. 그들은 불편함을 참지 못하고 수도관을 설치하여 거리 D(7 ≤ D ≤ 100,000)만큼 떨어진 곳의 강에서 물을 끌어오기로 했다. 근처의 인간 마을에서 P개(1 ≤ P ≤ 350)의 파이프를 매입했는데, 각각은 길이 Li와 용량 Ci로 나타낼 수 있다. (Li와 Ci는 모두 223보다 작거나 같은 양의 정수이다)

파이프들은 일렬로 이어서 수도관 하나로 만들 수 있으며, 이때 수도관의 용량은 그것을 이루는 파이프들의 용량 중 최솟값이 되고, 수도관의 길이는 파이프들 길이의 총합이다.

수도관을 한 개 만들어 총 길이가 정확히 D와 같게 할 때, 가능한 최대 수도관 용량을 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 D와 P가 주어진다. 두 번째 줄부터 P개의 줄이 차례로 주어지고, 각 줄마다 Li와 Ci가 주어진다. 길이 합이 D가 되게 하는 수도관의 부분집합이 적어도 하나 존재한다.
### **출력**
가능한 최대 수도관 용량을 첫째 줄에 출력한다.
### **예제입출력**

**예제 입력1**

```
7 6
4 5
3 6
2 7
1 4
6 7
1 5
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

D, P = map(int, sys.stdin.readline().rstrip().split())
pipes = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(P)]

dp = [-1] * (D + 1)
dp[0] = int(2e23)

for L, C in pipes:
    for s in range(D - L, -1, -1):
        if dp[s] == -1:
            continue
            
        new_cap = dp[s] if dp[s] < C else C
        if new_cap > dp[s+L]:
            dp[s+L] = new_cap

print(dp[D])
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|113612|392|PyPy3|418
#### **📝해설**

**알고리즘**
```
1. 배낭 문제
```

### **다른 풀이**

```python
import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

def solve():
    d, p = map(int, input().split())
    li = [list(map(int, input().split())) for _ in range(p)]
    li.sort(key=lambda x: -x[1])
    
    st = set()
    for l, c in li:
        if l == d:
            return c       
        temp = set()
        for length in st:
            nl = length + l
            if nl == d:
                return c
            if nl < d:
                temp.add(nl)
        temp.add(l)
        st |= temp

print(solve())
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
hsh8086|31120|32|Python3|541
#### **📝해설**

```python
import sys

D, P = map(int, sys.stdin.readline().rstrip().split())
pipes = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(P)]

# DP배열 선언 (dp[i]: 길이 i를 만들 때  최대 용량)
dp = [-1] * (D + 1)

# 시작은 임의의 큰 값
dp[0] = int(2e23)

# 모든 파이프를 확인하면서
for L, C in pipes:

    # 탑다운 방식으로
    for s in range(D - L, -1, -1):

        # 만들 수 없던 경우의수라면 넘어감
        if dp[s] == -1:
            continue
        
        # 현재 파이프의 용량과, dp[s]의 용량 중 큰 것을 사용
        new_cap = dp[s] if dp[s] < C else C

        # 이 파이프를 사용했을 때, dp배열 갱신
        if new_cap > dp[s+L]:
            dp[s+L] = new_cap

print(dp[D])
```