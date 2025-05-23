# [11066] 파일 합치기

### **난이도**
골드 3
## **📝문제**
소설가인 김대전은 소설을 여러 장(chapter)으로 나누어 쓰는데, 각 장은 각각 다른 파일에 저장하곤 한다. 소설의 모든 장을 쓰고 나서는 각 장이 쓰여진 파일을 합쳐서 최종적으로 소설의 완성본이 들어있는 한 개의 파일을 만든다. 이 과정에서 두 개의 파일을 합쳐서 하나의 임시파일을 만들고, 이 임시파일이나 원래의 파일을 계속 두 개씩 합쳐서 소설의 여러 장들이 연속이 되도록 파일을 합쳐나가고, 최종적으로는 하나의 파일로 합친다. 두 개의 파일을 합칠 때 필요한 비용(시간 등)이 두 파일 크기의 합이라고 가정할 때, 최종적인 한 개의 파일을 완성하는데 필요한 비용의 총 합을 계산하시오.

예를 들어, C1, C2, C3, C4가 연속적인 네 개의 장을 수록하고 있는 파일이고, 파일 크기가 각각 40, 30, 30, 50 이라고 하자. 이 파일들을 합치는 과정에서, 먼저 C2와 C3를 합쳐서 임시파일 X1을 만든다. 이때 비용 60이 필요하다. 그 다음으로 C1과 X1을 합쳐 임시파일 X2를 만들면 비용 100이 필요하다. 최종적으로 X2와 C4를 합쳐 최종파일을 만들면 비용 150이 필요하다. 따라서, 최종의 한 파일을 만드는데 필요한 비용의 합은 60+100+150=310 이다. 다른 방법으로 파일을 합치면 비용을 줄일 수 있다. 먼저 C1과 C2를 합쳐 임시파일 Y1을 만들고, C3와 C4를 합쳐 임시파일 Y2를 만들고, 최종적으로 Y1과 Y2를 합쳐 최종파일을 만들 수 있다. 이때 필요한 총 비용은 70+80+150=300 이다.

소설의 각 장들이 수록되어 있는 파일의 크기가 주어졌을 때, 이 파일들을 하나의 파일로 합칠 때 필요한 최소비용을 계산하는 프로그램을 작성하시오.
### **입력**
프로그램은 표준 입력에서 입력 데이터를 받는다. 프로그램의 입력은 T개의 테스트 데이터로 이루어져 있는데, T는 입력의 맨 첫 줄에 주어진다.각 테스트 데이터는 두 개의 행으로 주어지는데, 첫 행에는 소설을 구성하는 장의 수를 나타내는 양의 정수 K (3 ≤ K ≤ 500)가 주어진다. 두 번째 행에는 1장부터 K장까지 수록한 파일의 크기를 나타내는 양의 정수 K개가 주어진다. 파일의 크기는 10,000을 초과하지 않는다.
### **출력**
프로그램은 표준 출력에 출력한다. 각 테스트 데이터마다 정확히 한 행에 출력하는데, 모든 장을 합치는데 필요한 최소비용을 출력한다.
### **예제입출력**

**예제 입력1**

```
2
4
40 30 30 50
15
1 21 3 4 5 35 5 4 3 5 98 21 14 17 32
```

**예제 출력1**

```
300
864
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys

T = int(sys.stdin.readline().rstrip())

for testcase in range(T):
    K = int(sys.stdin.readline().rstrip())
    files = list(map(int, sys.stdin.readline().rstrip().split()))

    prefix_sum = [0] * (K+1)
    for i in range(K):
        prefix_sum[i+1] = prefix_sum[i] + files[i]
    
    dp = [[0] * K for _ in range(K)]

    for length in range(2, K+1):
        for i in range(K - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')

            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + (prefix_sum[j+1] - prefix_sum[i])
                if cost < dp[i][j]:
                    dp[i][j] = cost
    print(dp[0][K-1])
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|120956|2136|PyPy3|683
#### **📝해설**

**알고리즘**
```
1. DP
```

### **다른 풀이**

```python
import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    l = list(map(int,input().split()))
    if n == 1:
        print(0)
        return
    p = [0]
    for i in l:
        p.append(p[-1]+i)
    dp = [[1000000000]*(i+1)for i in range(n)]
    opt = [[0]*(i+1)for i in range(n)]
    for i in range(n-1):
        opt[i+1][i] = i
        dp[i+1][i] = l[i+1]+l[i]
        dp[i][i] = 0
    dp[n-1][n-1] = 0
    for cnt in range(2,n):
        for i in range(n-cnt):
            for k in range(opt[i+cnt-1][i],opt[i+cnt][i+1]+1):
                if dp[i+cnt][i]>dp[k][i]+dp[i+cnt][k+1]:
                    opt[i+cnt][i] = k
                    dp[i+cnt][i] = dp[k][i]+dp[i+cnt][k+1]
            dp[i+cnt][i]+=p[i+cnt+1]-p[i]
    print(dp[n-1][0])
for _ in range(int(input())):
    solve()
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
jakekim0105|117852|160|PyPy3|803
#### **📝해설**

```python
import sys

T = int(sys.stdin.readline().rstrip())

for testcase in range(T):
    K = int(sys.stdin.readline().rstrip())
    files = list(map(int, sys.stdin.readline().rstrip().split()))

    # 파일 크기의 누적합을 미리 계산해둠
    prefix_sum = [0] * (K+1)
    for i in range(K):
        prefix_sum[i+1] = prefix_sum[i] + files[i]
    
    # DP배열 선언. dp[i][j] : i에서 j번째 파일까지 합치는 최소 비용
    dp = [[0] * K for _ in range(K)]

    # 길이가 2인 구간부터 시작해서 K까지 모두 채움
    for length in range(2, K+1):
        # i : 시작 인덱스
        for i in range(K - length + 1):
            # j : 끝 인덱스
            j = i + length - 1

            # 임의의 큰 값으로 초기화
            dp[i][j] = float('inf')

            # 사이의 k에 대해서, 최솟값이 될때를 찾음
            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + (prefix_sum[j+1] - prefix_sum[i])
                if cost < dp[i][j]:
                    dp[i][j] = cost
    
    # 출력
    print(dp[0][K-1])
```