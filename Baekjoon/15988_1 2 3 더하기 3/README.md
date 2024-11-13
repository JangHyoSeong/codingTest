# [15988] 1, 2, 3 더하기 3

### **난이도**
실버 2
## **📝문제**
정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다.

- 1+1+1+1
- 1+1+2
- 1+2+1
- 2+1+1
- 2+2
- 1+3
- 3+1  
정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다. n은 양수이며 1,000,000보다 작거나 같다.
### **출력**
각 테스트 케이스마다, n을 1, 2, 3의 합으로 나타내는 방법의 수를 1,000,000,009로 나눈 나머지를 출력한다.
### **예제입출력**

**예제 입력1**

```
3
4
7
10
```

**예제 출력1**

```
7
44
274
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
T = int(input())
numbers = [int(input()) for _ in range(T)]

max_num = max(numbers)
dp = [1] * (max_num + 1)

dp[1] = 1

if max_num > 1:
    dp[2] = 2
if max_num > 2:
    dp[3] = 4

for i in range(4, max_num+1):
    dp[i] = (dp[i-3] + dp[i-2] + dp[i-1]) % 1000000009

for number in numbers:
    print(dp[number])
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|70676|404|Python3|312
#### **📝해설**

**알고리즘**
```
1. DP
```

#### **📝해설**

```python
T = int(input())
numbers = [int(input()) for _ in range(T)]

# 가장 큰 숫자를 구함
max_num = max(numbers)

# 그 숫자만큼 DP배열을 선언
# dp배열은 그 숫자를 만들 수 있는 경우의 수
dp = [1] * (max_num + 1)

# 1을 만들 수 있는 경우의 수 1
dp[1] = 1

# max_num의 edge case 고려
if max_num > 1:
    dp[2] = 2
if max_num > 2:
    dp[3] = 4


# 점화식
for i in range(4, max_num+1):
    dp[i] = (dp[i-3] + dp[i-2] + dp[i-1]) % 1000000009

for number in numbers:
    print(dp[number])
```