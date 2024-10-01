# [10942] 팰린드롬

### **난이도**
골드 4
## **📝문제**
명우는 홍준이와 함께 팰린드롬 놀이를 해보려고 한다.

먼저, 홍준이는 자연수 N개를 칠판에 적는다. 그 다음, 명우에게 질문을 총 M번 한다.

각 질문은 두 정수 S와 E(1 ≤ S ≤ E ≤ N)로 나타낼 수 있으며, S번째 수부터 E번째 까지 수가 팰린드롬을 이루는지를 물어보며, 명우는 각 질문에 대해 팰린드롬이다 또는 아니다를 말해야 한다.

예를 들어, 홍준이가 칠판에 적은 수가 1, 2, 1, 3, 1, 2, 1라고 하자.

- S = 1, E = 3인 경우 1, 2, 1은 팰린드롬이다.
- S = 2, E = 5인 경우 2, 1, 3, 1은 팰린드롬이 아니다.
- S = 3, E = 3인 경우 1은 팰린드롬이다.
- S = 5, E = 7인 경우 1, 2, 1은 팰린드롬이다.  
자연수 N개와 질문 M개가 모두 주어졌을 때, 명우의 대답을 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 수열의 크기 N (1 ≤ N ≤ 2,000)이 주어진다.

둘째 줄에는 홍준이가 칠판에 적은 수 N개가 순서대로 주어진다. 칠판에 적은 수는 100,000보다 작거나 같은 자연수이다.

셋째 줄에는 홍준이가 한 질문의 개수 M (1 ≤ M ≤ 1,000,000)이 주어진다.

넷째 줄부터 M개의 줄에는 홍준이가 명우에게 한 질문 S와 E가 한 줄에 하나씩 주어진다.
### **출력**
총 M개의 줄에 걸쳐 홍준이의 질문에 대한 명우의 답을 입력으로 주어진 순서에 따라서 출력한다. 팰린드롬인 경우에는 1, 아닌 경우에는 0을 출력한다.
### **예제입출력**

**예제 입력1**

```
7
1 2 1 3 1 2 1
4
1 3
2 5
3 3
5 7
```

**예제 출력1**

```
1
0
1
1
```
### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N = int(input())
arr = [0] + list(map(int, input().split()))
M = int(input())
questions = [list(map(int, input().split())) for _ in range(M)]

dp = [[False] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    dp[i][i] = True

for i in range(1, N):
    if arr[i] == arr[i+1]:
        dp[i][i+1] = True

for length in range(3, N+1):
    for i in range(1, N-length+2):
        j = i + length - 1
        if arr[i] == arr[j] and dp[i+1][j-1]:
            dp[i][j] = True

for question in questions:
    s, e = question
    if dp[s][e]:
        print(1)
    else:
        print(0)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|255368|876|PyPy3|581
#### **📝해설**

**알고리즘**
```
1. DP
```

### **다른 풀이**

```python
import io, os, sys


def main() -> None:
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    n = 2 * int(input()) + 1
    arr = [0] * n
    arr[1::2] = list(map(int, input().split()))
    radii = [0] * n
    for i in range(1, n - 1):
        for r in range(1, min(i, n - 1 - i) + 1):
            if arr[i - r] != arr[i + r]:
                break
        radii[i] = r

    result = []

    for _ in range(int(input())):
        s, e = map(int, input().split())
        s = s + s - 1
        e = e + e - 1
        mid = (s + e) // 2
        rad = (e - s) // 2 + 1
        result.append(1 if radii[mid] >= rad else 0)

    print("\n".join(map(str, result)))


sys.exit(main())
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
20210805|187480|260|PyPy3|693
#### **📝해설**

```python
N = int(input())
arr = [0] + list(map(int, input().split()))
M = int(input())
questions = [list(map(int, input().split())) for _ in range(M)]

# dp배열 선언. dp[i][j]==True는 i에서 j까지 팰린드롬이라는 뜻
dp = [[False] * (N+1) for _ in range(N+1)]


# 길이가 1이면 무조건 대칭
for i in range(1, N+1):
    dp[i][i] = True

# 길이가 2인 경우 대칭을 검사
for i in range(1, N):
    if arr[i] == arr[i+1]:
        dp[i][i+1] = True

# 길이가 3이상인 경우 대칭 검사
for length in range(3, N+1):
    for i in range(1, N-length+2):
        j = i + length - 1
        if arr[i] == arr[j] and dp[i+1][j-1]:
            dp[i][j] = True

for question in questions:
    s, e = question
    if dp[s][e]:
        print(1)
    else:
        print(0)
```