# [10164] 격자상의 경로

### **난이도**
실버 2
## **📝문제**
행의 수가 N이고 열의 수가 M인 격자의 각 칸에 1부터 N×M까지의 번호가 첫 행부터 시작하여 차례로 부여되어 있다. 격자의 어떤 칸은 ○ 표시가 되어 있다. (단, 1번 칸과 N × M번 칸은 ○ 표시가 되어 있지 않다. 또한, ○ 표시가 되어 있는 칸은 최대 한 개이다. 즉, ○ 표시가 된 칸이 없을 수도 있다.) 

행의 수가 3이고 열의 수가 5인 격자에서 각 칸에 번호가 1부터 차례대로 부여된 예가 아래에 있다. 이 격자에서는 8번 칸에 ○ 표시가 되어 있다.

![이미지](https://upload.acmicpc.net/8299a142-dd28-48bc-a698-64b8789e4733/-/preview/)

격자의 1번 칸에서 출발한 어떤 로봇이 아래의 두 조건을 만족하면서 N×M번 칸으로 가고자 한다. 

조건 1: 로봇은 한 번에 오른쪽에 인접한 칸 또는 아래에 인접한 칸으로만 이동할 수 있다. (즉, 대각선 방향으로는 이동할 수 없다.)
조건 2: 격자에 ○로 표시된 칸이 있는 경우엔 로봇은 그 칸을 반드시 지나가야 한다. 
위에서 보인 것과 같은 격자가 주어질 때, 로봇이 이동할 수 있는 서로 다른 경로의 두 가지 예가 아래에 있다.

- 1 → 2 → 3 → 8 → 9 → 10 → 15
- 1 → 2 → 3 → 8 → 13 → 14 → 15

격자에 관한 정보가 주어질 때 로봇이 앞에서 설명한 두 조건을 만족하면서 이동할 수 있는 서로 다른 경로가 총 몇 개나 되는지 찾는 프로그램을 작성하라. 
### **입력**
입력의 첫째 줄에는 격자의 행의 수와 열의 수를 나타내는 두 정수 N과 M(1 ≤ N, M ≤ 15), 그리고 ○로 표시된 칸의 번호를 나타내는 정수 K(K=0 또는 1 < K < N×M)가 차례로 주어지며, 각 값은 공백으로 구분된다. K의 값이 0인 경우도 있는데, 이는 ○로 표시된 칸이 없음을 의미한다. N과 M이 동시에 1인 경우는 없다.
### **출력**
주어진 격자의 정보를 이용하여 설명한 조건을 만족하는 서로 다른 경로의 수를 계산하여 출력해야 한다. 
### **예제입출력**

**예제 입력1**

```
3 5 8
```

**예제 출력1**

```
9
```

**예제 입력2**

```
7 11 0
```

**예제 출력2**

```
8008
```

**예제 입력3**

```
7 11 76
```

**예제 출력3**

```
5005
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N, M, K = map(int, input().split())

def count_paths(n, m):
    dp = [[0] * (m+1) for _ in range(n+1)]
    dp[1][1] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == j == 1:
                continue

            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return dp[n][m]

if K == 0:
    print(count_paths(N, M))

else:
    kr = (K-1) // M + 1
    kc = (K-1) % M + 1

    paths1 = count_paths(kr, kc)
    paths2 = count_paths(N-kr+1, M-kc+1)

    print(paths1 * paths2)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|32412|40|Python3|503
#### **📝해설**

**알고리즘**
```
1. DP
```

### **다른 풀이**

```python
def combination(n, r):
    num, rest = 1, 1
    
    for i in range(r):
        num *= n-i
        rest *= i+1
    
    return num // rest
    

n, m, k = map(int, input().split())
if k == 0:
    print(combination(n+m-2, min(n, m)-1))
else:
    k -= 1
    p, q = k//m, k%m
    a, b = n-p-1, m-q-1
    
    print(combination(p+q, min(p, q)) * combination(a+b, min(a, b)))
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
leehk_py|30616|36|Python3|370
#### **📝해설**

```python
N, M, K = map(int, input().split())

# n, m이 주어졌을 때, 경로의 경우의 수를 dp로 구함
def count_paths(n, m):

    # 크기 설정
    dp = [[0] * (m+1) for _ in range(n+1)]

    # 시작점 초기화
    dp[1][1] = 1

    # i와 j가 1인 경우 넘어감
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == j == 1:
                continue
            
            # dp배열 갱신
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return dp[n][m]

# K가 0인 경우 단순히 구함
if K == 0:
    print(count_paths(N, M))

# K가 0이 아닌 경우
else:

    # 동그라미의 좌표를 구함
    kr = (K-1) // M + 1
    kc = (K-1) % M + 1

    # 시작부터 동그라미까지
    paths1 = count_paths(kr, kc)
    # 동그라미부터 끝까지
    paths2 = count_paths(N-kr+1, M-kc+1)

    # 둘을 곱하면 총 경우의 수
    print(paths1 * paths2)
```