# [12847] 꿀 아르바이트

### **난이도**
실버 3
## **📝문제**
윤호는 퍼주기로 유명한 편의점 사장이다. 그의 편의점에는 특이한 임금 체계를 가지고 있다.

- 각 날마다 일의 차이때문에 일마다 급여가 정해져 있다.
- 윤호는  오차 없이 일급을 따박 따박 당일에 준다.
- 정해진 일 수 만큼만 일을 시킨다.
- 한번이라도 퇴직한 자를 다시 취직 시키지 않는다. (만약 취직을 한다면, 일을 시작 한 날부터 끝날 때까지 하루도 빠지면 안 된다.)  
무서운 아르바이트를 짤린 준수는 n+1일 후에 001에 월세를 내야 해서 윤호가 사장으로 있는 편의점에 취직하려 한다. 다행히 주변 퇴직자들의 얘기로 급여에 관련해 파악했다. 또한 퇴직자들의 급여 통계를 통해 당장 n일 후까지 일급 정보를 알아냈다. 하지만 준수는 시험을 준비해야 하기에 최대 m일 밖에 일을 할 수 없다.

어제까지 과제를 제출하고 지금도 001에서 자고 있는 준수를 위해 코딩 잘하는 여러분이 일을 해서 벌 수 있는 최대 이익을 준수에게 또 알려주도록 하자.
### **입력**
월세를 내기 바로 전 날 까지 인 n (1 ≤ n ≤ 100,000) 일과 일을 할 수 있는 날 m (0 ≤ m ≤ n) 일이 주어진다.

그 다음 줄 에는 1일부터 n일 까지 일급 Ti가 순서대로 주어진다. (0 < Ti ≤ 1,000,000)
### **출력**
준수가 일을 해서 벌 수 있는 최대 이익을 출력한다.
### **예제입출력**

**예제 입력1**

```
5 3
10 20 30 20 10
```

**예제 출력1**

```
70
```
### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N, M = map(int, input().split())
arr = list(map(int, input().split()))
prefix_sum = [0] * (N+1)

for i in range(N):
    prefix_sum[i+1] = prefix_sum[i] + arr[i]

max_sum = 0
for i in range(M, N+1):
    max_sum = max(max_sum, prefix_sum[i] - prefix_sum[i-M])

print(max_sum)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|42700|96|Python3|273
#### **📝해설**

**알고리즘**
```
1. 누적합
```

#### **📝해설**

```python
N, M = map(int, input().split())
arr = list(map(int, input().split()))
# 누적합을 계산할 리스트
prefix_sum = [0] * (N+1)

# 누적합을 미리 계산해둠
for i in range(N):
    prefix_sum[i+1] = prefix_sum[i] + arr[i]

# M개의 연속된 수열의 합 중 최대값을 구함
max_sum = 0
for i in range(M, N+1):
    max_sum = max(max_sum, prefix_sum[i] - prefix_sum[i-M])

print(max_sum)
```