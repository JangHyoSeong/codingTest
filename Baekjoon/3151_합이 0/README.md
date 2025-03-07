# [3151] 합이 0

### **난이도**
골드 4
## **📝문제**
Elly는 예상치 못하게 프로그래밍 대회를 준비하는 학생들을 가르칠 위기에 처했다. 대회는 정확히 3명으로 구성된 팀만 참가가 가능하다. 그러나 그녀가 가르칠 학생들에게는 큰 문제가 있었다. 코딩 실력이 좋으면 팀워크가 떨어지고, 팀워크가 좋을수록 코딩 실력이 떨어진다. 그리고 출전하고자 하는 대회는 코딩 실력과 팀워크 모두가 중요하다.

Elly는 그녀가 가르칠 수 있는 모든 학생들의 코딩 실력을 알고 있다. 각각의 코딩 실력 Ai는 -10000부터 10000 사이의 정수로 표시되어 있다. 그녀는 팀워크와 코딩 실력이 모두 적절한 팀을 만들기 위해, 세 팀원의 코딩 실력의 합이 0이 되는 팀을 만들고자 한다. 이러한 조건 하에, 그녀가 대회에 출전할 수 있는 팀을 얼마나 많이 만들 수 있는지를 계산하여라.

N명의 학생들의 코딩 실력 Ai가 -10000부터 10000사이의 정수로 주어질 때, 합이 0이 되는 3인조를 만들 수 있는 경우의 수를 구하여라.
### **입력**
입력은 표준 입력으로 주어진다.

첫 번째 줄에 학생의 수 N이 입력된다. 두 번째 줄에 N개의 그녀가 가르칠 학생들의 코딩 실력인 Ai가 주어진다.

- 1 ≤ N ≤ 10000
- -10000 ≤ Ai ≤ 10000
### **출력**
표준 출력으로 그녀가 고를 수 있는 팀의 수를 하나의 정수로 출력한다.
### **예제입출력**

**예제 입력1**

```
10
2 -5 2 3 -4 7 -4 0 1 -6
```

**예제 출력1**

```
6
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from bisect import bisect_left

N = int(input())
arr = list(map(int, input().split()))

arr.sort()
result = 0

for i in range(N-2):
    left, right = i+1, N-1

    while left < right:
        score_sum = arr[i] + arr[left] + arr[right]

        if score_sum > 0:
            right -= 1
        else:
            if score_sum == 0:
                if arr[left] == arr[right]:
                    result += (right - left)
                else:
                    idx = bisect_left(arr, arr[right])
                    result += (right - idx + 1)
            left += 1

print(result)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|111836|3464|PyPy3|581
#### **📝해설**

**알고리즘**
```
1. 투 포인터
2. 이분 탐색
```

### **다른 풀이**

```python
n = int(input())
li = list(map(int, input().split()))

dp = [0] * 40001
total = 0
for i in range(1, n):
    total += dp[20000 - li[i]]
    
    for j in range(i):
        dp[20000 + li[j] + li[i]] += 1
        
print(total)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
hsh8086|125788|260|PyPy3|223
#### **📝해설**

```python
from bisect import bisect_left

N = int(input())
arr = list(map(int, input().split()))

# 투포인터, 이분탐색을 위해 정렬
arr.sort()
result = 0

# 숫자를 하나 고정한 뒤
for i in range(N-2):
    # 투 포인터 설정
    left, right = i+1, N-1

    # 두 포인터가 만날때까지 반복
    while left < right:

        # 숫자의 합
        score_sum = arr[i] + arr[left] + arr[right]

        # 숫자의 합이 0보다 크면, 오른쪽 숫자를 줄임
        if score_sum > 0:
            right -= 1

        else:
            # 합이 0이라면
            if score_sum == 0:

                # 오른쪽, 왼쪽이 중복된 수라면 중복된 숫자만큼 경우의 수에 더함
                if arr[left] == arr[right]:
                    result += (right - left)
                
                # 중복된 수가 아니라면 이분탐색을 통해 인덱스를 찾고
                else:
                    idx = bisect_left(arr, arr[right])

                    # 그만큼 더함
                    result += (right - idx + 1)

            # 왼쪽 인덱스를 증가
            left += 1

print(result)
```