# [11497] 통나무 건니뛰기

### **난이도**
실버 1
## **📝문제**
남규는 통나무를 세워 놓고 건너뛰기를 좋아한다. 그래서 N개의 통나무를 원형으로 세워 놓고 뛰어놀려고 한다. 남규는 원형으로 인접한 옆 통나무로 건너뛰는데, 이때 각 인접한 통나무의 높이 차가 최소가 되게 하려 한다.

[이미지](https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/11497/1.png)

통나무 건너뛰기의 난이도는 인접한 두 통나무 간의 높이의 차의 최댓값으로 결정된다. 높이가 {2, 4, 5, 7, 9}인 통나무들을 세우려 한다고 가정하자. 이를 [2, 9, 7, 4, 5]의 순서로 세웠다면, 가장 첫 통나무와 가장 마지막 통나무 역시 인접해 있다. 즉, 높이가 2인 것과 높이가 5인 것도 서로 인접해 있다. 배열 [2, 9, 7, 4, 5]의 난이도는 |2-9| = 7이다. 우리는 더 나은 배열 [2, 5, 9, 7, 4]를 만들 수 있으며 이 배열의 난이도는 |5-9| = 4이다. 이 배열보다 난이도가 낮은 배열은 만들 수 없으므로 이 배열이 남규가 찾는 답이 된다.
### **입력**
입력은 T개의 테스트 케이스로 이루어져 있다. 첫 줄에 T가 주어진다.

이어지는 각 줄마다 첫 줄에 통나무의 개수를 나타내는 정수 N(5 ≤ N ≤ 10,000), 둘째 줄에 각 통나무의 높이를 나타내는 정수 Li가 주어진다. (1 ≤ Li ≤ 100,000)
### **출력**
각 테스트 케이스마다 한 줄에 주어진 통나무들로 만들 수 있는 최소 난이도를 출력하시오.
### **예제입출력**

**예제 입력1**

```
3
7
13 10 12 11 10 11 12
5
2 4 5 7 9
8
6 6 6 6 6 6 6 6
```

**예제 출력1**

```
1
4
0
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys

T = int(sys.stdin.readline().rstrip())

for testcase in range(T):
    N = int(sys.stdin.readline().rstrip())
    arr = list(map(int, sys.stdin.readline().rstrip().split()))

    arr.sort()
    new_arr = [0] * N

    for i in range(N):
        if i % 2:
            new_arr[N - 1 - (i//2)] = arr[i]
        else:
            new_arr[i//2] = arr[i]

    max_gap = 0
    for i in range(N-1):
        max_gap = max(max_gap, abs(new_arr[i+1] - new_arr[i]))

    print(max_gap)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|111896|172|PyPy3|483
#### **📝해설**

**알고리즘**
```
1. 그리디 알고리즘
```

### **다른 풀이**

```python
import sys

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def solution():
    T = int(input())
    for _ in range(T):
        N = int(input())
        nums = list(map(int, input().split()))
        nums.sort()
        ans = 0
        for i in range(N - 2):
            ans = max(ans, nums[i + 2] - nums[i])
        print(ans)


solution()
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
iamhelpingstar|33432|132|Python3|359
#### **📝해설**

```python
import sys

T = int(sys.stdin.readline().rstrip())

for testcase in range(T):
    N = int(sys.stdin.readline().rstrip())
    arr = list(map(int, sys.stdin.readline().rstrip().split()))

    # 배열을 정렬
    arr.sort()

    # 정규분포곡선처럼 가운데로 갈수록 커지게 배열을 재배치
    new_arr = [0] * N

    for i in range(N):
        if i % 2:
            new_arr[N - 1 - (i//2)] = arr[i]
        else:
            new_arr[i//2] = arr[i]

    # 그 중에서 최대 차이를 계산
    max_gap = 0
    for i in range(N-1):
        max_gap = max(max_gap, abs(new_arr[i+1] - new_arr[i]))

    print(max_gap)
```