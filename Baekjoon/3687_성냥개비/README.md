# [3687] 성냥개비

### **난이도**
골드 2
## **📝문제**
성냥개비는 숫자를 나타내기에 아주 이상적인 도구이다. 보통 십진수를 성냥개비로 표현하는 방법은 다음과 같다.

[이미지](https://www.acmicpc.net/upload/images/match.png)

성냥개비의 개수가 주어졌을 때, 성냥개비를 모두 사용해서 만들 수 있는 가장 작은 수와 큰 수를 찾는 프로그램을 작성하시오.
### **입력**
첫째 줄에 테스트 케이스의 개수가 주어진다. 테스트 케이스는 최대 100개 이다. 각 테스트 케이스는 한 줄로 이루어져 있고, 성냥개비의 개수 n이 주어진다. (2 ≤ n ≤ 100)
### **출력**
각 테스트 케이스에 대해서 입력으로 주어진 성냥개비를 모두 사용해서 만들 수 있는 가장 작은 수와 가장 큰 수를 출력한다. 두 숫자는 모두 양수이어야 하고, 숫자는 0으로 시작할 수 없다. 
### **예제입출력**

**예제 입력1**

```
4
3
6
7
15
```

**예제 출력1**

```
7 7
6 111
8 711
108 7111111
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
T = int(input())
numbers = [int(input()) for _ in range(T)]

matchsticks = {
    2: '1',
    3: '7',
    4: '4',
    5: '2',
    6: '0',
    7: '8'
}

N = max(numbers)

min_dp = [''] * (N + 1)
min_dp[2] = '1'
min_dp[3] = '7'
min_dp[4] = '4'
min_dp[5] = '2'
min_dp[6] = '6'
min_dp[7] = '8'

for i in range(8, N + 1):
    min_num = None
    for k in matchsticks:
        prev = min_dp[i - k]
        if prev == '':
            continue

        candidate = matchsticks[k] + prev
        candidate = ''.join(sorted(candidate))
        if candidate[0] == '0':
            for j in range(1, len(candidate)):
                if candidate[j] != '0':
                    candidate = candidate[j] + candidate[:j] + candidate[j+1:]
                    break
        
        if min_num is None or int(candidate) < int(min_num):
            min_num = candidate
    min_dp[i] = min_num

for number in numbers:
    min_val = min_dp[number]

    if number % 2 == 0:
        max_val = '1' * (number//2)
    else:
        max_val = '7' + '1' * ((number - 3) // 2)
    
    print(min_val, max_val)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|32412|36|Python3|1080
#### **📝해설**

**알고리즘**
```
1. DP
2. 그리디 알고리즘
```

### **다른 풀이**

```python
import sys
 
def input():
    return sys.stdin.readline()
 
N = int(input())
INF = float('inf')
dp = [INF for _ in range(101)]
dp[2] = 1
dp[3] = 7
dp[4] = 4
dp[5] = 2
dp[6] = 6
dp[7] = 8
dp[8] = 10
 
for num in range(9,101):
    for i in range(2,8):
        if i != 6:
            dp[num] = min(dp[num],dp[num-i]*10+dp[i])
        else:
            dp[num] = min(dp[num],dp[num-i]*10)
for _ in range(N):
    k = int(input())
    
    max_value = ('7' if k%2 else '1' ) +'1'*(k//2-1)
    print(dp[k],max_value)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
lunerave07|31120|28|Python3|509
#### **📝해설**

```python
T = int(input())
numbers = [int(input()) for _ in range(T)]

# 각 성냥개비로 만들 수 있는 숫자
matchsticks = {
    2: '1',
    3: '7',
    4: '4',
    5: '2',
    6: '0',
    7: '8'
}

N = max(numbers)

# DP 배열 초기값 설정
min_dp = [''] * (N + 1)
min_dp[2] = '1'
min_dp[3] = '7'
min_dp[4] = '4'
min_dp[5] = '2'
min_dp[6] = '6'
min_dp[7] = '8'

# 초기값 이후로 DP 배열을 채움
for i in range(8, N + 1):

    # 이번 성냥개비 갯수로 만들 수 있는 최소값
    min_num = None

    # 모든 숫자를 검토하면서
    for k in matchsticks:

        # 이전값에 더해서 최소값을 만듦
        prev = min_dp[i - k]
        if prev == '':
            continue
        
        # 만들 수 있는 숫자 후보
        candidate = matchsticks[k] + prev

        # 최소값이 되도록 정렬
        candidate = ''.join(sorted(candidate))

        # 맨 앞이 0이라면
        if candidate[0] == '0':

            # 0을 맨 앞이 아니고, 바로 앞이 되도록 바꿈
            for j in range(1, len(candidate)):
                if candidate[j] != '0':
                    candidate = candidate[j] + candidate[:j] + candidate[j+1:]
                    break
        # 최소값이 갱신 가능하다면 갱신
        if min_num is None or int(candidate) < int(min_num):
            min_num = candidate
    min_dp[i] = min_num

# 출력
for number in numbers:
    min_val = min_dp[number]

    # 최대값은 항상 7과 1을 사용하는 것이 유리함
    if number % 2 == 0:
        max_val = '1' * (number//2)
    else:
        max_val = '7' + '1' * ((number - 3) // 2)
    
    print(min_val, max_val)
```