# [14719] 빗물

### **난이도**
골드 5
## **📝문제**
2차원 세계에 블록이 쌓여있다. 비가 오면 블록 사이에 빗물이 고인다.

비는 충분히 많이 온다. 고이는 빗물의 총량은 얼마일까?
### **입력**
첫 번째 줄에는 2차원 세계의 세로 길이 H과 2차원 세계의 가로 길이 W가 주어진다. (1 ≤ H, W ≤ 500)

두 번째 줄에는 블록이 쌓인 높이를 의미하는 0이상 H이하의 정수가 2차원 세계의 맨 왼쪽 위치부터 차례대로 W개 주어진다.

따라서 블록 내부의 빈 공간이 생길 수 없다. 또 2차원 세계의 바닥은 항상 막혀있다고 가정하여도 좋다.
### **출력**
2차원 세계에서는 한 칸의 용량은 1이다. 고이는 빗물의 총량을 출력하여라.

빗물이 전혀 고이지 않을 경우 0을 출력하여라.
### **예제입출력**

**예제 입력1**

```
4 4
3 0 1 4
```

**예제 출력1**

```
5
```

**예제 입력2**

```
4 8
3 1 2 3 4 1 1 2
```

**예제 출력2**

```
5
```

**예제 입력3**

```
3 5
0 0 0 2 0
```

**예제 출력3**

```
0
```
## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
H, W = map(int, input().split())
arr = list(map(int, input().split()))

rain = 0
for i in range(1, W-1):
    left_max = max(arr[:i])
    right_max = max(arr[i+1:])

    valid_height = min(left_max, right_max)

    if arr[i] < valid_height:
        rain += valid_height - arr[i]

print(rain)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|31120|40|Python3|290
#### **📝해설**

**알고리즘**
```
1. 구현
```
#### **📝해설**

```python
H, W = map(int, input().split())
arr = list(map(int, input().split()))

rain = 0
# 양쪽 끝은 빗물이 고일 수 없다. 따라서 범위를 1, W-1까지 설정
for i in range(1, W-1):
    # 현재 위치 기준 왼쪽의 최대값, 오른쪽의 최대값을 구함.
    # 그 안에서 빗물이 쌓임
    left_max = max(arr[:i])
    right_max = max(arr[i+1:])

    # 왼, 오 최대값 중 낮은 값을 기준으로 빗물이 쌓임
    valid_height = min(left_max, right_max)

    # 따라서, 빗물이 쌓일 수 있는 높이라면, 그 칸 개수만큼 빗물이 쌓임
    if arr[i] < valid_height:
        rain += valid_height - arr[i]

print(rain)
```