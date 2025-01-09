# [13335] 트럭

### **난이도**
실버 1
## **📝문제**
강을 가로지르는 하나의 차선으로 된 다리가 하나 있다. 이 다리를 n 개의 트럭이 건너가려고 한다. 트럭의 순서는 바꿀 수 없으며, 트럭의 무게는 서로 같지 않을 수 있다. 다리 위에는 단지 w 대의 트럭만 동시에 올라갈 수 있다. 다리의 길이는 w 단위길이(unit distance)이며, 각 트럭들은 하나의 단위시간(unit time)에 하나의 단위길이만큼만 이동할 수 있다고 가정한다. 동시에 다리 위에 올라가 있는 트럭들의 무게의 합은 다리의 최대하중인 L보다 작거나 같아야 한다. 참고로, 다리 위에 완전히 올라가지 못한 트럭의 무게는 다리 위의 트럭들의 무게의 합을 계산할 때 포함하지 않는다고 가정한다.

예를 들어, 다리의 길이 w는 2, 다리의 최대하중 L은 10, 다리를 건너려는 트럭이 트럭의 무게가 [7, 4, 5, 6]인 순서대로 다리를 오른쪽에서 왼쪽으로 건넌다고 하자. 이 경우 모든 트럭이 다리를 건너는 최단시간은 아래의 그림에서 보는 것과 같이 8 이다.


![이미지](https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/13335/1.png)
Figure 1. 본문의 예에 대해 트럭들이 다리를 건너는 과정.

다리의 길이와 다리의 최대하중, 그리고 다리를 건너려는 트럭들의 무게가 순서대로 주어졌을 때, 모든 트럭이 다리를 건너는 최단시간을 구하는 프로그램을 작성하라.
### **입력**
입력 데이터는 표준입력을 사용한다. 입력은 두 줄로 이루어진다. 입력의 첫 번째 줄에는 세 개의 정수 n (1 ≤ n ≤ 1,000) , w (1 ≤ w ≤ 100) and L (10 ≤ L ≤ 1,000)이 주어지는데, n은 다리를 건너는 트럭의 수, w는 다리의 길이, 그리고 L은 다리의 최대하중을 나타낸다. 입력의 두 번째 줄에는 n개의 정수 a1, a2, ⋯ , an (1 ≤ ai ≤ 10)가 주어지는데, ai는 i번째 트럭의 무게를 나타낸다.
### **출력**
출력은 표준출력을 사용한다. 모든 트럭들이 다리를 건너는 최단시간을 출력하라.
### **예제입출력**

**예제 입력1**

```
4 2 10
7 4 5 6
```

**예제 출력1**

```
8
```

**예제 입력2**

```
1 100 100
10
```

**예제 출력2**

```
101
```

**예제 입력3**

```
10 100 100
10 10 10 10 10 10 10 10 10 10
```

**예제 출력3**

```
110
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from collections import deque

N, W, L = map(int, input().split())
trucks = list(map(int, input().split()))

bridge = deque([0] * W)
weight = 0
time = 0

for truck in trucks:
    while True:
        time += 1
        weight -= bridge.popleft()

        if weight + truck <= L:
            bridge.append(truck)
            weight += truck
            break
        else:
            bridge.append(0)

time += W

print(time)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|34908|56|Python3|422
#### **📝해설**

**알고리즘**
```
1. 큐
```

#### **📝해설**

```python
from collections import deque

# 입력받기
N, W, L = map(int, input().split())
trucks = list(map(int, input().split()))

# 다리의 상태를 큐로 표현. 단위 위치에 존재하는 트럭의 무게
bridge = deque([0] * W)

# 현재 총 무게
weight = 0

# 걸린 시간
time = 0

# 모든 트럭을 순회하면서
for truck in trucks:

    # 한번의 반복이 1초 경과를 뜻함
    while True:

        # 1초 더함
        time += 1

        # 다리의 가장 끝부분의 트럭은 빠져나감
        weight -= bridge.popleft()

        # 만약 이번 트럭이 다리위에 올라갈 수 있다면
        if weight + truck <= L:
            # 다리의 맨 오른쪽에 트럭을 올림
            bridge.append(truck)
            
            # 다리의 총 무게를 더함
            weight += truck

            # 다음 트럭을 검사
            break

        # 아직 트럭을 올릴 수 없다면
        else:
            # 트럭을 더하지 않고 0을 올림 (모든 트럭 한 칸 씩 전진)
            bridge.append(0)

# 마지막 트럭은 다리를 건너면 끝
time += W

print(time)
```