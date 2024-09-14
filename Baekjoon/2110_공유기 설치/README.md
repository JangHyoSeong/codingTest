# [2110] 공유기 설치

### **난이도**
골드 4
## **📝문제**
도현이의 집 N개가 수직선 위에 있다. 각각의 집의 좌표는 x1, ..., xN이고, 집 여러개가 같은 좌표를 가지는 일은 없다.

도현이는 언제 어디서나 와이파이를 즐기기 위해서 집에 공유기 C개를 설치하려고 한다. 최대한 많은 곳에서 와이파이를 사용하려고 하기 때문에, 한 집에는 공유기를 하나만 설치할 수 있고, 가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치하려고 한다.

C개의 공유기를 N개의 집에 적당히 설치해서, 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 집의 개수 N (2 ≤ N ≤ 200,000)과 공유기의 개수 C (2 ≤ C ≤ N)이 하나 이상의 빈 칸을 사이에 두고 주어진다. 둘째 줄부터 N개의 줄에는 집의 좌표를 나타내는 xi (0 ≤ xi ≤ 1,000,000,000)가 한 줄에 하나씩 주어진다.
### **출력**
첫째 줄에 가장 인접한 두 공유기 사이의 최대 거리를 출력한다.
### **예제입출력**

**예제 입력1**

```
5 3
1
2
8
4
9
```

**예제 출력1**

```
3
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys
input = sys.stdin.readline

N, C = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr.sort()

start = 1
end = arr[-1] - arr[0]
result = 0

while start <= end:
    mid = (start + end) // 2
    count = 1
    prev_house = arr[0]

    for i in range(1, N):
        if arr[i] - prev_house >= mid:
            count += 1
            prev_house = arr[i]

    if count >= C:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|38848|436|Python3|487
#### **📝해설**

**알고리즘**
```
1. 이분 탐색
```

#### **📝해설**

```python
import sys
input = sys.stdin.readline

N, C = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr.sort()

# 공유기 사이의 거리를 이분탐색으로 찾음
start = 1
end = arr[-1] - arr[0]

# 결과값
result = 0

# 이분탐색 시작
while start <= end:
    mid = (start + end) // 2

    # 첫 집에 공유기를 설치
    count = 1
    prev_house = arr[0]

    # 다른 집을 탐색하면서
    for i in range(1, N):
        # 다음 집이 이번 탐색에서 설정한 거리보다 멀리 있다면
        if arr[i] - prev_house >= mid:

            # 공유기를 설치
            count += 1
            prev_house = arr[i]

    # 만약 주어진 횟수보다 크거나 같다면
    if count >= C:

        # 거리를 더 늘려서 다시 탐색
        result = mid
        start = mid + 1

    # 주어진 횟수보다 적었다면 거리를 줄여서 탐색
    else:
        end = mid - 1

# 결과 출력
print(result)
```