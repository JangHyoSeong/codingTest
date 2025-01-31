# [2302] 극장 좌석

### **난이도**
실버 1
## **📝문제**
어떤 극장의 좌석은 한 줄로 되어 있으며 왼쪽부터 차례대로 1번부터 N번까지 번호가 매겨져 있다. 공연을 보러 온 사람들은 자기의 입장권에 표시되어 있는 좌석에 앉아야 한다. 예를 들어서, 입장권에 5번이 쓰여 있으면 5번 좌석에 앉아야 한다. 단, 자기의 바로 왼쪽 좌석 또는 바로 오른쪽 좌석으로는 자리를 옮길 수 있다. 예를 들어서, 7번 입장권을 가진 사람은 7번 좌석은 물론이고, 6번 좌석이나 8번 좌석에도 앉을 수 있다. 그러나 5번 좌석이나 9번 좌석에는 앉을 수 없다.

그런데 이 극장에는 “VIP 회원”들이 있다. 이 사람들은 반드시 자기 좌석에만 앉아야 하며 옆 좌석으로 자리를 옮길 수 없다.

오늘 공연은 입장권이 매진되어 1번 좌석부터 N번 좌석까지 모든 좌석이 다 팔렸다. VIP 회원들의 좌석 번호들이 주어졌을 때, 사람들이 좌석에 앉는 서로 다른 방법의 가짓수를 구하는 프로그램을 작성하시오.

예를 들어서, 그림과 같이 좌석이 9개이고, 4번 좌석과 7번 좌석이 VIP석인 경우에 <123456789>는 물론 가능한 배치이다. 또한 <213465789> 와 <132465798> 도 가능한 배치이다. 그러나 <312456789> 와 <123546789> 는 허용되지 않는 배치 방법이다.


### **입력**
첫째 줄에는 좌석의 개수 N이 입력된다. N은 1 이상 40 이하이다. 둘째 줄에는 고정석의 개수 M이 입력된다. M은 0 이상 N 이하이다. 다음 M 개의 줄에는 고정석의 번호가 작은 수부터 큰 수의 순서로 한 줄에 하나씩 입력된다.
### **출력**
주어진 조건을 만족하면서 사람들이 좌석에 앉을 수 있는 방법의 가짓수를 출력한다. 방법의 가짓수는 2,000,000,000을 넘지 않는다. (2,000,000,000 < 231-1)
### **예제입출력**

**예제 입력1**

```
9
2
4
7
```

**예제 출력1**

```
12
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N = int(input())
M = int(input())
vips = [int(input()) for _ in range(M)]

sections = []
if M > 0:
    sections.append(vips[0] - 1)
    for i in range(1, M):
        sections.append(vips[i] - vips[i-1] - 1)
    sections.append(N - vips[-1])
else:
    sections.append(N)
max_length = max(sections)

dp = [1] * (max_length+1)
for i in range(2, max_length+1):
    dp[i] = dp[i-1] + dp[i-2]

result = 1
for section in sections:
    result *= dp[section]

print(result)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|31120|36|Python3|464
#### **📝해설**

**알고리즘**
```
1. DP
```

#### **📝해설**

```python
N = int(input())
M = int(input())
vips = [int(input()) for _ in range(M)]

# 구간의 길이들을 저장할 리스트
sections = []

# M이 0이 아닌 경우
if M > 0:

    # 각 구간의 길이를 저장
    sections.append(vips[0] - 1)
    for i in range(1, M):
        sections.append(vips[i] - vips[i-1] - 1)
    sections.append(N - vips[-1])

# M이 0인 경우 구간은 N의 길이인 하나
else:
    sections.append(N)

# 각 구간 중 최대값을 변수로 저장
max_length = max(sections)

# 각 구간에서 나올 수 있는 경우의 수를 저장할 DP
dp = [1] * (max_length+1)

# 각 구간의 경우의 수는 피보나치의 형태로 나옴
for i in range(2, max_length+1):
    dp[i] = dp[i-1] + dp[i-2]

# 경우의 수를 구함
result = 1
for section in sections:
    result *= dp[section]

print(result)
```