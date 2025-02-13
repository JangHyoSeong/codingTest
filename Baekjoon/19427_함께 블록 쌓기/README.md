# [19427] 함께 블록 쌓기

### **난이도**
골드 4
## **📝문제**
번부터 N번까지의 학생들은 각각 블록들을 가지고 있다. 학생마다 최대 M개의 블록을 가지고 있을 수 있으며, 한 명의 학생이 가지고 있는 모든 블록들의 높이는 서로 다르다. 이 때 1번부터 N번까지의 학생들이 가진 블록을 차례대로 사용하여 바닥에서부터 쌓아올려 하나의 탑을 만들고자 한다.

단, 어떤 학생의 블록은 사용하지 않아도 되며 한 학생당 최대 1개의 블록만을 사용할 수 있다.

1번부터 N번까지의 학생들이 가지고 있는 블록들에 대한 정보가 주어졌을 때, 높이가 정확히 H인 탑을 만들 수 있는 경우의 수를 계산하는 프로그램을 작성하시오.

예를 들어 N=3, M=3, H=5일 때, 각 학생마다 가지고 있는 블록들의 높이가 다음과 같다고 가정하자.

- 1번 학생: 2, 3, 5
- 2번 학생: 3, 5
- 3번 학생: 1, 2, 3  
이 때, 탑의 높이가 정확히 5가 되도록 블록을 쌓는 경우로는 다음의 6가지가 존재한다. (블록을 사용하지 않는 경우는 X로 표시하였다.)
[이미지](https://upload.acmicpc.net/82b228be-4bf3-4a38-95e3-a2238e9bb4ff/-/preview/)
### **입력**
첫째 줄에 자연수 N, M, H가 공백을 기준으로 구분되어 주어진다. (1 ≤ N ≤ 50, 1 ≤ M ≤ 10, 1 ≤ H ≤ 1,000) 둘째 줄부터 N개의 줄에 걸쳐서 각 학생이 가진 블록들의 높이가 공백을 기준으로 구분되어 주어진다.

단, 모든 블록의 높이는 1,000 이하의 자연수이며 한 명의 학생이 가지고 있는 모든 블록들의 높이는 서로 다르게 주어진다.
### **출력**
첫째 줄에 높이가 H인 탑을 만드는 경우의 수를 10,007로 나눈 나머지를 출력한다.
### **예제입출력**

**예제 입력1**

```
3 3 5
2 3 5
3 5
1 2 3
```

**예제 출력1**

```
6
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N, M, H = map(int, input().split())
blocks = [list(map(int, input().split())) for _ in range(N)]

dp = [0] * (H+1)
dp[0] = 1

for block in blocks:
    new_dp = dp[:]
    for b in block:
        for h in range(H, b-1, -1):
            new_dp[h] = (new_dp[h] + dp[h-b]) % 10007
    dp = new_dp

print(dp[H])
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|32412|132|Python3|305
#### **📝해설**

**알고리즘**
```
1. DP
```
### **다른 풀이**

```python
def dynamic_programming(students):
    dp = [[0] * (H + 1) for _ in range(N + 1)]

    # 높이 0을 만드는 경우는 1가지
    dp[0][0] = 1
    # 학생 순회
    for n in range(1, N + 1):
        # 블록을 사용하지 않는 경우 복사
        dp[n] = dp[n - 1][:]
        # 각 블록 순회
        for block in students[n]:
            # 이번 블록보다 크거나 같은 높이 순회
            for h in range(block, H + 1):
                # 이번 경우의 수에 이전에 블록을 사용하지 않았을 때 경우의 수 더하기
                dp[n][h] += dp[n - 1][h - block]
    
    return dp[N][H] % 10007


N, M, H = map(int, input().split())
students = [[]]
for _ in range(N):
    student = list(map(int, input().split()))
    students.append(student)

print(dynamic_programming(students))
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
taetaehyeon|33164|72|Python3|1417
#### **📝해설**

```python
N, M, H = map(int, input().split())
blocks = [list(map(int, input().split())) for _ in range(N)]

# DP배열 선언 dp[h] : h높이를 만들 수 있는 경우의 수
dp = [0] * (H+1)

# 높이 0을 만드는 경우의 수는 하나
dp[0] = 1

# 학생이 사용할 수 있는 모든 블럭을 순회
for block in blocks:

    # 기존의 DP배열을 복사
    new_dp = dp[:]

    # 이번 학생이 사용할 수 있는 모든 블럭을 검사하면서
    for b in block:

        # 탑다운 방식으로 순회
        for h in range(H, b-1, -1):

            # 이 블록을 사용했을 때 만들 수 있는 경우의 수를 업데이트
            new_dp[h] = (new_dp[h] + dp[h-b]) % 10007
    dp = new_dp

print(dp[H])
```