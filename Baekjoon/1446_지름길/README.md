# [1446] 지름길

### **난이도**
실버 1
## **📝문제**
매일 아침, 세준이는 학교에 가기 위해서 차를 타고 D킬로미터 길이의 고속도로를 지난다. 이 고속도로는 심각하게 커브가 많아서 정말 운전하기도 힘들다. 어느 날, 세준이는 이 고속도로에 지름길이 존재한다는 것을 알게 되었다. 모든 지름길은 일방통행이고, 고속도로를 역주행할 수는 없다.

세준이가 운전해야 하는 거리의 최솟값을 출력하시오.
### **입력**
첫째 줄에 지름길의 개수 N과 고속도로의 길이 D가 주어진다. N은 12 이하인 양의 정수이고, D는 10,000보다 작거나 같은 자연수이다. 다음 N개의 줄에 지름길의 시작 위치, 도착 위치, 지름길의 길이가 주어진다. 모든 위치와 길이는 10,000보다 작거나 같은 음이 아닌 정수이다. 지름길의 시작 위치는 도착 위치보다 작다.
### **출력**
세준이가 운전해야하는 거리의 최솟값을 출력하시오.
### **예제입출력**

**예제 입력1**

```
5 150
0 50 10
0 50 20
50 100 10
100 151 10
110 140 90
```

**예제 출력1**

```
70
```

**예제 입력2**

```
2 100
10 60 40
50 90 20
```

**예제 출력2**

```
80
```

**예제 입력3**

```
8 900
0 10 9
20 60 45
80 190 100
50 70 15
160 180 14
140 160 14
420 901 5
450 900 0
```

**예제 출력3**

```
432
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N, D = map(int, input().split())

shortcuts = {}
for _ in range(N):
    a, b, c = map(int, input().split())
    if shortcuts.get(a) is None:
        shortcuts[a] = [(b, c)]
    else:
        shortcuts[a].append((b, c))

dp = [i for i in range(D+1)]

for i in range(D+1):
    dp[i] = min(dp[i-1] + 1, dp[i])

    if shortcuts.get(i) is not None:
        for next, dist in shortcuts[i]:
            if next <= D:
                dp[next] = min(dp[next], dp[i] + dist)

print(dp[-1])
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|31120|32|Python3|480
#### **📝해설**

**알고리즘**
```
1. DP
```

#### **📝해설**

```python
N, D = map(int, input().split())

# 지름길 정보를 저장할 딕셔너리
shortcuts = {}

# 지름길 정보를 저장
for _ in range(N):
    a, b, c = map(int, input().split())
    if shortcuts.get(a) is None:
        shortcuts[a] = [(b, c)]
    else:
        shortcuts[a].append((b, c))

# i번째 인덱스 : i 거리까지 가는 최단거리
dp = [i for i in range(D+1)]

# DP 배열 작성
for i in range(D+1):

    dp[i] = min(dp[i-1] + 1, dp[i])

    if shortcuts.get(i) is not None:
        for next, dist in shortcuts[i]:
            if next <= D:
                dp[next] = min(dp[next], dp[i] + dist)

print(dp[-1])
```