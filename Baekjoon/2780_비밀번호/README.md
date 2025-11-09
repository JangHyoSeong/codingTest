# [2780] 비밀번호

### **난이도**
실버 1
## **📝문제**
석원이는 자신의 현관문에 비밀번호 기계를 설치했다. 그 기계의 모양은 다음과 같다.

![이미지](https://www.acmicpc.net/upload/images/pw.png)

지나가던 석원이 친구 주희는 단순한 호기심에 저 비밀번호를 풀고 싶어한다. 이때 주희는 바닥에 떨어져 있는 힌트 종이를 줍게 된다. 이 종이에는 석원이가 비밀번호를 만들 때 사용했던 조건이 적혀 있다. 이제 주희는 이 조건을 가지고, 석원이 집의 가능한 비밀번호의 전체 개수를 알고 싶어 한다. 현재 컴퓨터를 사용할 수 없는 주희는 당신에게 이 문제를 부탁했다. 석원이의 힌트 종이는 다음과 같다.

1. 비밀번호의 길이는 N이다.
2. 비밀번호는 위 그림에 나온 번호들을 눌러서 만든다.
3. 비밀번호에서 인접한 수는 실제 위 기계의 번호에서도 인접해야 한다.

(ex. 15 라는 비밀번호는 불가능하다. (1과 5는 인접하지 않는다. ) 하지만 1236이라는 비밀번호는 가능하다.)
### **입력**
첫 번째 줄에 Test case의 수 T가 주어진다. 그리고 각각의 케이스마다 입력으로 첫 번째 줄에 비밀번호의 길이 N이 주어진다.( 1 <= N <= 1,000 )
### **출력**
각각의 Test case에 대해서 조건을 만족하는 비밀번호의 개수를 출력하라. 단, 수가 매우 커질 수 있으므로 비밀번호의 개수를 1,234,567으로 나눈 나머지를 출력하라.
### **예제입출력**

**예제 입력1**

```
3
1
2
3
```

**예제 출력1**

```
10
26
74
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
MOD = 1234567

T = int(input())
cases = [int(input()) for _ in range(T)]

adj = {
    0: [7],
    1: [2, 4],
    2: [1, 3, 5],
    3: [2, 6],
    4: [1, 5, 7],
    5: [2, 4, 6, 8],
    6: [3, 5, 9],
    7: [4, 8, 0],
    8: [5, 7, 9],
    9: [6, 8],
}

max_N = max(cases)
dp = [[0] * 10 for _ in range(max_N + 1)]

for num in range(10):
    dp[1][num] = 1

for i in range(2, max_N + 1):
    for num in range(10):
        dp[i][num] = sum(dp[i-1][j] for j in adj[num]) % MOD

for n in cases:
    print(sum(dp[n]) % MOD)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|33432|60|Python3|518
#### **📝해설**

**알고리즘**
```
1. DP
```

### **다른 풀이**

```python
import sys

MOD = 1234567
MAX_N = 1000

def get_input():
    input = sys.stdin.readline
    C = int(input().rstrip())
    Ns = []
    for _ in range(C):
        Ns.append(int(input().rstrip()))
    return Ns,

def solve(Ns:list[int])->list[int]:
    '''
    '''
    max_n = max(Ns)
    ans = [0] * (max_n + 1)

    la = [1]*10  # la[k]: num cases where last digit is k
    nx = [0]*10  # next of la[]
    ans[1] = sum(la)

    for k in range(2, max_n+1):
        nx[1] = (la[2]+la[4]) % MOD
        nx[2] = (la[1]+la[3]+la[5]) % MOD
        nx[3] = (la[2]+la[6]) % MOD
        nx[4] = (la[1]+la[5]+la[7]) % MOD
        nx[5] = (la[2]+la[4]+la[6]+la[8]) % MOD
        nx[6] = (la[3]+la[5]+la[9]) % MOD
        nx[7] = (la[4]+la[8]+la[0]) % MOD
        nx[8] = (la[5]+la[7]+la[9]) % MOD
        nx[9] = (la[6]+la[8]) % MOD
        nx[0] = la[7]
        la,nx = nx,la
        ans[k] = sum(la) % MOD

    return [ ans[n] for n in Ns ]

if __name__ == '__main__':
    r = solve(*get_input())
    print('\n'.join(map(str, r)))
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
cafrii|32412|32|Python3|1026
#### **📝해설**

```python
MOD = 1234567

T = int(input())
cases = [int(input()) for _ in range(T)]

# 키패드에서 해당 숫자에 인접한 숫자들을 딕셔너리로 저장
adj = {
    0: [7],
    1: [2, 4],
    2: [1, 3, 5],
    3: [2, 6],
    4: [1, 5, 7],
    5: [2, 4, 6, 8],
    6: [3, 5, 9],
    7: [4, 8, 0],
    8: [5, 7, 9],
    9: [6, 8],
}

# 가장 큰 N을 미리 구함
max_N = max(cases)

# DP배열 선언. dp[i][num] : i번째 크기의 비밀번호를 만들 때, 마지막 숫자가 num인 경우의 만들 수 있는 경우의 수
dp = [[0] * 10 for _ in range(max_N + 1)]

# 비밀번호가 1자리인 경우, 각 자리수는 한개씩 경우의 수를 가짐
for num in range(10):
    dp[1][num] = 1

# 2자리부터 최대크기까지 dp배열 작성
for i in range(2, max_N + 1):

    # 모든 숫자를 확인하면서
    for num in range(10):

        # 이전 끝나는 숫자에서 만들 수 있는 경우의 수를 모두 더함
        dp[i][num] = sum(dp[i-1][j] for j in adj[num]) % MOD

for n in cases:
    print(sum(dp[n]) % MOD)
```