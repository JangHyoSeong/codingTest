# [19622] 회의실 배정 3

### **난이도**
실버 2
## **📝문제**
서준이는 아빠로부터 N개의 회의와 하나의 회의실을 선물로 받았다. 각 회의는 시작 시간, 끝나는 시간, 회의 인원이 주어지고 한 회의실에서 동시에 두 개 이상의 회의가 진행될 수 없다. 단, 회의는 한번 시작되면 중간에 중단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다. 회의의 시작 시간은 끝나는 시간보다 항상 작다. N개의 회의를 회의실에 효율적으로 배정할 경우 회의를 진행할 수 있는 최대 인원을 구하자.
### **입력**
첫째 줄에 회의의 수 N이 주어진다. 둘째 줄부터 N + 1 줄까지 공백을 사이에 두고 회의의 시작시간, 끝나는 시간, 회의 인원이 주어진다.
### **출력**
첫째 줄에 회의실에서 회의를 진행할 수 있는 최대 인원을 출력한다.
### **예제입출력**

**예제 입력1**

```
6
10 40 80
30 60 60
50 80 70
70 100 100
90 120 40
110 140 50
```

**예제 출력1**

```
230
```
### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import bisect

N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]
meetings.sort(key=lambda x: x[1])
end_times = [meeting[1] for meeting in meetings]

dp = [0] * (N + 1)
for i in range(1, N + 1):
    start, end, people = meetings[i - 1]
    idx = bisect.bisect_right(end_times, start) - 1    
    dp[i] = max(dp[i - 1], dp[idx + 1] + people)

print(dp[N])
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|59080|2756|Python3|383
#### **📝해설**

**알고리즘**
```
1. DP
```

#### **📝해설**

```python
import bisect

N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]
meetings.sort(key=lambda x: x[1])
end_times = [meeting[1] for meeting in meetings]

# DP배열. 각 회의를 끝냈을 때 가장 이득인 경우
dp = [0] * (N + 1)
for i in range(1, N + 1):
    start, end, people = meetings[i - 1]
    idx = bisect.bisect_right(end_times, start) - 1    
    dp[i] = max(dp[i - 1], dp[idx + 1] + people)

print(dp[N])
```

### **🔖정리**

1. 배운점