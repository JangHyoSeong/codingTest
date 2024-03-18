# [11660] 구간 합 구하기 5

### **난이도**
실버 1
## **📝문제**
N×N개의 수가 N×N 크기의 표에 채워져 있다. (x1, y1)부터 (x2, y2)까지 합을 구하는 프로그램을 작성하시오. (x, y)는 x행 y열을 의미한다.

예를 들어, N = 4이고, 표가 아래와 같이 채워져 있는 경우를 살펴보자.

1	2	3	4  
2	3	4	5  
3	4	5	6  
4	5	6	7  
여기서 (2, 2)부터 (3, 4)까지 합을 구하면 3+4+5+4+5+6 = 27이고, (4, 4)부터 (4, 4)까지 합을 구하면 7이다.

표에 채워져 있는 수와 합을 구하는 연산이 주어졌을 때, 이를 처리하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 표의 크기 N과 합을 구해야 하는 횟수 M이 주어진다. (1 ≤ N ≤ 1024, 1 ≤ M ≤ 100,000) 둘째 줄부터 N개의 줄에는 표에 채워져 있는 수가 1행부터 차례대로 주어진다. 다음 M개의 줄에는 네 개의 정수 x1, y1, x2, y2 가 주어지며, (x1, y1)부터 (x2, y2)의 합을 구해 출력해야 한다. 표에 채워져 있는 수는 1,000보다 작거나 같은 자연수이다. (x1 ≤ x2, y1 ≤ y2)
### **출력**
총 M줄에 걸쳐 (x1, y1)부터 (x2, y2)까지 합을 구해 출력한다.
### **예제입출력**

**예제 입력1**

```
4 3
1 2 3 4
2 3 4 5
3 4 5 6
4 5 6 7
2 2 3 4
3 4 3 4
1 1 4 4
```

**예제 출력1**

```
27
6
64
```

**예제 입력2**

```
2 4
1 2
3 4
1 1 1 1
1 2 1 2
2 1 2 1
2 2 2 2
```

**예제 출력2**

```
1
2
3
4
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N, M = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]
positions = [list(map(int, input().split())) for _ in range(M)]

prefix_sum = [[0] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        prefix_sum[i][j] = table[i-1][j-1] + prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1]

for i in range(M):
    y1, x1, y2, x2 = positions[i]
    result = prefix_sum[y2][x2] - prefix_sum[y2][x1-1] - prefix_sum[y1-1][x2] + prefix_sum[y1-1][x1-1]
    print(result)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|140652|444|PyPy3|561
#### **📝해설**

**알고리즘**
```
1. 누적합
2. 다이나믹 프로그래밍
```
### **다른 풀이**

```python
import os, io, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

N,M=map(int, input().split())
arr = [ list(map(int, input().split())) for _ in range(N)]

cumsum = [[0 for _ in range(N+1)] for _ in range(N+1)]  
for i in range(1,N+1):
    for j in range(1,N+1):
        cumsum[i][j] = cumsum[i-1][j] + cumsum[i][j-1] - cumsum[i-1][j-1] + arr[i-1][j-1]

ans = []
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    ans.append(cumsum[x2][y2] - cumsum[x2][y1-1] - cumsum[x1-1][y2] + cumsum[x1-1][y1-1])
    
sys.stdout.write('\n'.join(map(str, ans)))
```

#### **📝해설**

```python
N, M = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]
positions = [list(map(int, input().split())) for _ in range(M)]

# 누적합을 저장할 2차원 리스트
# 계산을 편하게 하기 위해 N+1의 크기로 선언
# 각 0번 인덱스는 0이 들어감
prefix_sum = [[0] * (N+1) for _ in range(N+1)]

# 누적합 테이블을 작성
for i in range(1, N+1):
    for j in range(1, N+1):
        prefix_sum[i][j] = table[i-1][j-1] + prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1]

# 누적합 계산
for i in range(M):
    y1, x1, y2, x2 = positions[i]
    result = prefix_sum[y2][x2] - prefix_sum[y2][x1-1] - prefix_sum[y1-1][x2] + prefix_sum[y1-1][x1-1]
    print(result)

'''
참고 사이트
https://velog.io/@alkwen0996/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%88%84%EC%A0%81%ED%95%A9Prefix-Sum-2%EC%B0%A8%EC%9B%90-%EB%88%84%EC%A0%81%ED%95%A9Prefix-Sum-of-Matrix
'''
```

### **🔖정리**

1. 배운점