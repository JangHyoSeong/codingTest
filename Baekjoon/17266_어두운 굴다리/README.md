# [17266] 어두운 굴다리

### **난이도**
실버 4
## **📝문제**
인하대학교 후문 뒤쪽에는 어두운 굴다리가 있다. 겁쟁이 상빈이는 길이 조금이라도 어둡다면 가지 않는다. 따라서 굴다리로 가면 최단거리로 집까지 갈수 있지만, 굴다리는 어둡기 때문에 빙빙 돌아서 집으로 간다. 안타깝게 여긴 인식이는 굴다리 모든 길 0~N을 밝히게 가로등을 설치해 달라고 인천광역시에 민원을 넣었다. 인천광역시에서 가로등을 설치할 개수 M과 각 가로등의 위치 x들의 결정을 끝냈다. 그리고 각 가로등은 높이만큼 주위를 비출 수 있다. 하지만 갑자기 예산이 부족해진 인천광역시는 가로등의 높이가 높을수록 가격이 비싸지기 때문에 최소한의 높이로 굴다리 모든 길 0~N을 밝히고자 한다. 최소한의 예산이 들 높이를 구하자. 단 가로등은 모두 높이가 같아야 하고, 정수이다.

다음 그림을 보자.

![이미지](https://upload.acmicpc.net/d21c182b-3a7d-48ba-b198-65a1bd3ddd98/-/preview/)

가로등의 높이가 H라면 왼쪽으로 H, 오른쪽으로 H만큼 주위를 비춘다.

다음 그림은 예제1에 대한 설명이다.

![이미지](https://upload.acmicpc.net/a1f0fc3c-7c16-4108-bb18-31fe9ff3bbe4/-/preview/)

가로등의 높이가 1일 경우 0~1사이의 길이 어둡기 때문에 상빈이는 지나가지 못한다.

아래 그림처럼 높이가 2일 경우 0~5의 모든 길이 밝기 때문에 상빈이는 지나갈 수 있다.

![이미지](https://upload.acmicpc.net/0c74958f-4437-405d-9242-f204282c0b45/-/preview/)

### **입력**
첫 번째 줄에 굴다리의 길이 N 이 주어진다. (1 ≤ N ≤ 100,000)

두 번째 줄에 가로등의 개수 M 이 주어진다. (1 ≤ M ≤ N)

다음 줄에 M 개의 설치할 수 있는 가로등의 위치 x 가 주어진다. (0 ≤ x ≤ N)

가로등의 위치 x는 오름차순으로 입력받으며 가로등의 위치는 중복되지 않으며, 정수이다.
### **출력**
굴다리의 길이 N을 모두 비추기 위한 가로등의 최소 높이를 출력한다.
### **예제입출력**

**예제 입력1**

```
5
2
2 4
```

**예제 출력1**

```
2
```

**예제 입력2**

```
3
1
0
```

**예제 출력2**

```
3
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys

N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
lights = list(map(int, sys.stdin.readline().rstrip().split()))

left, right = lights[0], N
answer = N

while left <= right:
    mid = (left + right) // 2

    flag = True

    if lights[0] - mid > 0:
        flag = False

    for i in range(1, M):
        if lights[i] - lights[i-1] > 2 * mid:
            flag = False
            break
    
    if lights[-1] + mid < N:
        flag = False

    if flag:
        answer = mid
        right = mid - 1
    
    else:
        left = mid + 1

print(answer)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|42660|280|Python3|593
#### **📝해설**

**알고리즘**
```
1. 이분 탐색
```

#### **📝해설**

```python
import sys

N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
lights = list(map(int, sys.stdin.readline().rstrip().split()))

# 이분 탐색을 위한 가로등 범위 최대 최소 값
left, right = lights[0], N
answer = N

# 이분 탐색
while left <= right:
    mid = (left + right) // 2

    # 현재 mid가 가능한 케이스인지 저장할 변수
    flag = True

    # 시작 지점이 가능한지
    if lights[0] - mid > 0:
        flag = False

    # 가로등 사이들이 가능한지
    for i in range(1, M):
        if lights[i] - lights[i-1] > 2 * mid:
            flag = False
            break
    
    # 끝 부분이 가능한지
    if lights[-1] + mid < N:
        flag = False

    # 가능한 케이스였다면 답을 갱신하고 범위를 줄임
    if flag:
        answer = mid
        right = mid - 1
    
    # 불가능한 케이스였다면 범위를 늘림
    else:
        left = mid + 1

print(answer)
```