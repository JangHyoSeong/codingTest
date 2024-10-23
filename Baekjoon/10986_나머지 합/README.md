# [10986] 나머지 합

### **난이도**
골드 3
## **📝문제**
수 N개 A1, A2, ..., AN이 주어진다. 이때, 연속된 부분 구간의 합이 M으로 나누어 떨어지는 구간의 개수를 구하는 프로그램을 작성하시오.

즉, Ai + ... + Aj (i ≤ j) 의 합이 M으로 나누어 떨어지는 (i, j) 쌍의 개수를 구해야 한다.
### **입력**
첫째 줄에 N과 M이 주어진다. (1 ≤ N ≤ 106, 2 ≤ M ≤ 103)

둘째 줄에 N개의 수 A1, A2, ..., AN이 주어진다. (0 ≤ Ai ≤ 109)
### **출력**
첫째 줄에 연속된 부분 구간의 합이 M으로 나누어 떨어지는 구간의 개수를 출력한다.
### **예제입출력**

**예제 입력1**

```
5 3
1 2 3 1 2
```

**예제 출력1**

```
7
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N, M = map(int, input().split())
arr = list(map(int, input().split()))

remainder = [0] * M
current_sum = 0
count = 0

remainder[0] = 1

for num in arr:
    current_sum = (current_sum + num) % M
    
    if current_sum < 0:
        current_sum += M
    
    count += remainder[current_sum]
    
    remainder[current_sum] += 1

print(count)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|143316|572|Python3|340
#### **📝해설**

**알고리즘**
```
1. 누적합
```

### **다른 풀이**

```python
import sys
input = sys.stdin.readline


# 1 <= N <= 10^6 , 구간 합이 M(2<=M<=10^3)으로 나누어 떨어지는 (i,j) 쌍 개수 구하기 

n, m = map(int, input().split())

# a list 가져오기 
a_list = [int(a) for a in input().split()]

# 합 배열 
s_list = [0] * n

# i의 합벼열을 m으로 나눈 값 
sum_reminder_list = [0] * n

reminder_same_cnt_list = [0] * m

cnt = 0

# 합배열 가져오기 
for i in range(n):
  if i == 0: 
    s_list[i] = a_list[i] 
  else:
    s_list[i] = s_list[i-1] + a_list[i]

  sum_reminder_list[i] = s_list[i] % m
  
  # 0인 경우의 수는 미리 더해준다. A1 ~ Ai 의 구간 합의 %m 은 0이라는 의미 
  if sum_reminder_list[i] == 0:
    cnt += 1 

  reminder_same_cnt_list[sum_reminder_list[i]] += 1

for dup_count in reminder_same_cnt_list:

  if dup_count > 1:
  #cnt += conbination(dup_count, 2)
    cnt += dup_count * (dup_count -1) // 2

print(cnt)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
sangjeong100|214824|316|PyPy3|918
#### **📝해설**

```python
N, M = map(int, input().split())
arr = list(map(int, input().split()))

# 누적합을 M으로 나눈 나머지를 기록할 배열
remainder = [0] * M
current_sum = 0
count = 0

# 나머지가 0인 구간을 1로 초기화
remainder[0] = 1

for num in arr:
    
    # 현재까지의 누적합을 계산하고, M으로 나눈 나머지를 구함
    current_sum = (current_sum + num) % M
    
    # 누적합이 음수가 된다면 양수로 조정
    if current_sum < 0:
        current_sum += M
    
    # 나머지가 같은 구간의 개수를 추가
    count += remainder[current_sum]
    
    # 현재 나머지를 카운팅
    remainder[current_sum] += 1

print(count)
```