# [2565] 전깃줄

### **난이도**
골드 5
## **📝문제**
두 전봇대 A와 B 사이에 하나 둘씩 전깃줄을 추가하다 보니 전깃줄이 서로 교차하는 경우가 발생하였다. 합선의 위험이 있어 이들 중 몇 개의 전깃줄을 없애 전깃줄이 교차하지 않도록 만들려고 한다.

예를 들어, < 그림 1 >과 같이 전깃줄이 연결되어 있는 경우 A의 1번 위치와 B의 8번 위치를 잇는 전깃줄, A의 3번 위치와 B의 9번 위치를 잇는 전깃줄, A의 4번 위치와 B의 1번 위치를 잇는 전깃줄을 없애면 남아있는 모든 전깃줄이 서로 교차하지 않게 된다.


[이미지](https://upload.acmicpc.net/d90221dd-eb80-419f-bdfb-5dd4ebac23af/-/preview/)
< 그림 1 >

전깃줄이 전봇대에 연결되는 위치는 전봇대 위에서부터 차례대로 번호가 매겨진다. 전깃줄의 개수와 전깃줄들이 두 전봇대에 연결되는 위치의 번호가 주어질 때, 남아있는 모든 전깃줄이 서로 교차하지 않게 하기 위해 없애야 하는 전깃줄의 최소 개수를 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에는 두 전봇대 사이의 전깃줄의 개수가 주어진다. 전깃줄의 개수는 100 이하의 자연수이다. 둘째 줄부터 한 줄에 하나씩 전깃줄이 A전봇대와 연결되는 위치의 번호와 B전봇대와 연결되는 위치의 번호가 차례로 주어진다. 위치의 번호는 500 이하의 자연수이고, 같은 위치에 두 개 이상의 전깃줄이 연결될 수 없다.
### **출력**
첫째 줄에 남아있는 모든 전깃줄이 서로 교차하지 않게 하기 위해 없애야 하는 전깃줄의 최소 개수를 출력한다.
### **예제입출력**

**예제 입력1**

```
8
1 8
3 9
2 2
4 1
6 4
10 10
9 7
7 6
```

**예제 출력1**

```
3
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import bisect

N = int(input())
wires = [list(map(int, input().split())) for _ in range(N)]
wires.sort()

b_values = [b for _, b in wires]

dp = []
for num in b_values:
    pos = bisect.bisect_left(dp, num)
    if pos == len(dp):
        dp.append(num)
    else:
        dp[pos] = num

max_lis = len(dp)
print(N - max_lis)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|34476|40|Python3|322
#### **📝해설**

**알고리즘**
```
1. DP
```

### **다른 풀이**

```python
import sys
input = sys.stdin.readline
print = sys.stdout.write

def get_lines_cnt(arr, N):
  memo = [1 for _ in range(N)] 

  for i in range(N):
    for j in range(i):
      if arr[i][1] > arr[j][1]:
        memo[i] = max(memo[i], memo[j] + 1)

  return max(memo)

if __name__ == '__main__':
  N = int(input())
  lines = [list(map(int, input().split())) for _ in range(N)]
  lines.sort()
  cnt = get_lines_cnt(lines, N)
  print(f'{N - cnt}\n')
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
nestnote|31120|28|Python3|443
#### **📝해설**

```python
import bisect

# 입력받기
N = int(input())
wires = [list(map(int, input().split())) for _ in range(N)]

# 전깃줄을 정렬
wires.sort()

# B 전봇대의 값만 추출
b_values = [b for _, b in wires]

# LIS(최장 증가 수열) 배열
dp = []
for num in b_values:

    # num이 들어갈 위치를 이진탐색
    pos = bisect.bisect_left(dp, num)

    # num이 가장 큰 값이면 그대로 추가
    if pos == len(dp):
        dp.append(num)
    # 기존 LIS 배열에서 값 교체
    else:
        dp[pos] = num

# 최장 증가 부분 수열의 길이
max_lis = len(dp)
# 제거할 전깃줄 개수 = 전체개수 - LIS 길이
print(N - max_lis)
```

### **🔖정리**

1. 배운점