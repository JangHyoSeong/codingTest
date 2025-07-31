# [11659] 구간 합 구하기 4

### **난이도**
실버 3
## **📝문제**
수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 수의 개수 N과 합을 구해야 하는 횟수 M이 주어진다. 둘째 줄에는 N개의 수가 주어진다. 수는 1,000보다 작거나 같은 자연수이다. 셋째 줄부터 M개의 줄에는 합을 구해야 하는 구간 i와 j가 주어진다.
### **출력**
총 M개의 줄에 입력으로 주어진 i번째 수부터 j번째 수까지 합을 출력한다.
### **예제입출력**

**예제 입력1**

```
5 3
5 4 3 2 1
1 3
2 4
5 5
```

**예제 출력1**

```
12
9
1
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

prefix_sum = [0] * (N+1)
for i in range(1, N+1):
    prefix_sum[i] = prefix_sum[i-1] + arr[i-1]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print(prefix_sum[b] - prefix_sum[a-1])
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|41444|256|Python3|345
#### **📝해설**

**알고리즘**
```
1. 누적 합
```