# [25682] 체스판 다시 칠하기 2

### **난이도**
골드 4
## **📝문제**
지민이는 자신의 저택에서 MN개의 단위 정사각형으로 나누어져 있는 M×N 크기의 보드를 찾았다. 어떤 정사각형은 검은색으로 칠해져 있고, 나머지는 흰색으로 칠해져 있다. 지민이는 이 보드를 잘라서 K×K 크기의 체스판으로 만들려고 한다.

체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다. 구체적으로, 각 칸이 검은색과 흰색 중 하나로 색칠되어 있고, 변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다. 따라서 이 정의를 따르면 체스판을 색칠하는 경우는 두 가지뿐이다. 하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.

보드가 체스판처럼 칠해져 있다는 보장이 없어서, 지민이는 K×K 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다. 당연히 K×K 크기는 아무데서나 골라도 된다. 지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 정수 N, M, K가 주어진다. 둘째 줄부터 N개의 줄에는 보드의 각 행의 상태가 주어진다. B는 검은색이며, W는 흰색이다.
### **출력**
첫째 줄에 지민이가 잘라낸 K×K 보드를 체스판으로 만들기 위해 다시 칠해야 하는 정사각형 개수의 최솟값을 출력한다.
### **예제입출력**

**예제 입력1**

```
4 4 3
BBBB
BBBB
BBBW
BBWB
```

**예제 출력1**

```
2
```

**예제 입력2**

```
8 8 8
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBBBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW
```

**예제 출력2**

```
1
```

**예제 입력3**

```
10 13 10
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
WWWWWWWWWWBWB
WWWWWWWWWWBWB
```

**예제 출력3**

```
30
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N, M, K = map(int, input().split())
board = [list(input()) for _ in range(N)]

start_white = [[0] * M for _ in range(N)]
start_black = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        expected_w = "W" if (i + j) % 2 == 0 else "B"
        expected_b = "B" if (i + j) % 2 == 0 else "W"

        if board[i][j] != expected_w:
            start_white[i][j] = 1
        if board[i][j] != expected_b:
            start_black[i][j] = 1

def prefix_sum(arr):
    psum = [[0] * (M+1) for _ in range(N+1)]
    for i in range(N):
        for j in range(M):
            psum[i+1][j+1] = arr[i][j] + psum[i][j+1] + psum[i+1][j] - psum[i][j]
    
    return psum

psum_w = prefix_sum(start_white)
psum_b = prefix_sum(start_black)

def get_sum(psum, x1, y1, x2, y2):
    return psum[x2][y2] - psum[x1][y2] -psum[x2][y1] + psum[x1][y1]

min_result = int(21e8)
for i in range(N - K + 1):
    for j in range(M - K + 1):
        sum_w = get_sum(psum_w, i, j, i+K, j+K)
        sum_b = get_sum(psum_b, i, j, i+K, j+K)
        min_result = min(min_result, sum_w, sum_b)

print(min_result)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|394776|PyPy3|1097
#### **📝해설**

**알고리즘**
```
1. 누적합
```

### **다른 풀이**

```python
import sys
input=sys.stdin.readline

N,M,K=map(int,input().split())
a=[[0]*(M+1)for _ in range(N+1)]
r=float('inf')
for i in range(N):
    s=input()
    for j in range(M):
        k,h=i+1,j+1
        a[k][h]=(s[j]=='WB'[(i+j)%2])+a[i][h]+a[k][j]-a[i][j]
        if k>=K and h>=K:c=a[k][h]-a[k-K][h]-a[k][h-K]+a[k-K][h-K];r=min(r,c,K*K-c)

print(r)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
samminmul|142480|280|PyPy3|347
#### **📝해설**

```python
N, M, K = map(int, input().split())
board = [list(input()) for _ in range(N)]

# 각각 왼쪽 위가 흑, 백인 경우, 입력받은 체스판과 다르다면 1, 같다면 0으로 채움
start_white = [[0] * M for _ in range(N)]
start_black = [[0] * M for _ in range(N)]

# 체스판을 확인하면서
for i in range(N):
    for j in range(M):

        # 위치가 흑인지 백인지 확인
        expected_w = "W" if (i + j) % 2 == 0 else "B"
        expected_b = "B" if (i + j) % 2 == 0 else "W"

        # 백으로 시작하는 경우, 흑으로 시작하는 경우를 모두 고려해서 기존과 다른지 확인
        if board[i][j] != expected_w:
            start_white[i][j] = 1
        if board[i][j] != expected_b:
            start_black[i][j] = 1

# 다른 칸이 얼마나 있는지 누적합으로 구하는 함수
def prefix_sum(arr):
    psum = [[0] * (M+1) for _ in range(N+1)]

    # 입력받은 체스판과 다른 칸의 누적 합을 구함
    for i in range(N):
        for j in range(M):
            psum[i+1][j+1] = arr[i][j] + psum[i][j+1] + psum[i+1][j] - psum[i][j]
    
    return psum

# 흑 백의 경우를 모두 확인
psum_w = prefix_sum(start_white)
psum_b = prefix_sum(start_black)

# 특정 구간의 누적합을 구하는 함수
def get_sum(psum, x1, y1, x2, y2):
    return psum[x2][y2] - psum[x1][y2] -psum[x2][y1] + psum[x1][y1]

# 결과로 사용할 변수
min_result = int(21e8)

# K * K 배열을 모두 확인
for i in range(N - K + 1):
    for j in range(M - K + 1):

        # 흑, 백의 경우를 모두 구함
        sum_w = get_sum(psum_w, i, j, i+K, j+K)
        sum_b = get_sum(psum_b, i, j, i+K, j+K)
        min_result = min(min_result, sum_w, sum_b)

# 출력
print(min_result)
```