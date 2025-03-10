# [2564] 경비원

### **난이도**
실버 1
## **📝문제**
동근이는 무인 경비 회사 경비원으로 항상 대기하고 있다가 호출이 들어오면 경비차를 몰고 그 곳으로 달려가야 한다. 동근이가 담당하고 있는 곳은 직사각형 모양의 블록으로 블록 중간을 가로질러 차가 통과할만한 길이 없다. 이 블록 경계에 무인 경비를 의뢰한 상점들이 있다.

예를 들어 가로의 길이가 10, 세로의 길이가 5인 블록의 경계에 무인 경비를 의뢰한 3개의 상점이 있다고 하자. <그림 1>과 같이 이들은 1, 2, 3으로 표시되어 있고, 동근이는 X로 표시한 위치에 있다.


![이미지](https://upload.acmicpc.net/e89bf381-c913-4e99-b4b7-42bc4ba7c3ec/-/preview/)
< 그림 1 >

1번 상점에서 호출이 들어 왔을 때 동근이가 블록을 시계방향으로 돌아 이동하면 이동 거리가 12가 된다. 반면 반시계방향으로 돌아 이동하면 이동 거리는 18이 된다. 따라서 동근이가 1번 상점으로 가는 최단 거리는 12가 된다. 마찬가지로 동근이의 위치에서 2번 상점까지의 최단 거리는 6, 3번 상점까지의 최단 거리는 5가 된다.

블록의 크기와 상점의 개수 및 위치 그리고 동근이의 위치가 주어질 때 동근이의 위치와 각 상점 사이의 최단 거리의 합을 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 블록의 가로의 길이와 세로의 길이가 차례로 주어진다. 둘째 줄에 상점의 개수가 주어진다. 블록의 가로의 길이와 세로의 길이, 상점의 개수는 모두 100이하의 자연수이다. 이어 한 줄에 하나씩 상점의 위치가 주어진다. 상점의 위치는 두 개의 자연수로 표시된다. 첫째 수는 상점이 위치한 방향을 나타내는데, 1은 블록의 북쪽, 2는 블록의 남쪽, 3은 블록의 서쪽, 4는 블록의 동쪽에 상점이 있음을 의미한다. 둘째 수는 상점이 블록의 북쪽 또는 남쪽에 위치한 경우 블록의 왼쪽 경계로부터의 거리를 나타내고, 상점이 블록의 동쪽 또는 서쪽에 위치한 경우 블록의 위쪽 경계로부터의 거리를 나타낸다. 마지막 줄에는 동근이의 위치가 상점의 위치와 같은 방식으로 주어진다. 상점의 위치나 동근이의 위치는 블록의 꼭짓점이 될 수 없다.
### **출력**
첫째 줄에 동근이의 위치와 각 상점 사이의 최단 거리의 합을 출력한다.
### **예제입출력**

**예제 입력1**

```
10 5
3
1 4
3 2
2 8
2 3
```

**예제 출력1**

```
23
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
W, H = map(int, input().split())
N = int(input())
stores = [list(map(int, input().split())) for _ in range(N)]
start = list(map(int, input().split()))

P = 2 * (W + H)

def convert_position(direction, distance):
    if direction == 1:
        return distance
    elif direction == 2:
        return W + H + (W - distance)
    elif direction == 3:
        return W + H + W + (H - distance)
    else:
        return W + distance
    
position = convert_position(start[0], start[1])
total_distance = 0
for direction, distance in stores:
    store_position = convert_position(direction, distance)
    total_distance += min(abs(position - store_position), P - abs(position - store_position))

print(total_distance)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|32412|36|Python3|709
#### **📝해설**

**알고리즘**
```
1. 구현
```

#### **📝해설**

```python
W, H = map(int, input().split())
N = int(input())
stores = [list(map(int, input().split())) for _ in range(N)]
start = list(map(int, input().split()))

# 전체 둘레
P = 2 * (W + H)

# 입력 정보로 부터 위치를 변환
def convert_position(direction, distance):
    # 북쪽
    if direction == 1:
        return distance

    # 남쪽
    elif direction == 2:
        return W + H + (W - distance)
    
    # 서쪽
    elif direction == 3:
        return W + H + W + (H - distance)

    # 동쪽
    else:
        return W + distance

# 기준 위치
position = convert_position(start[0], start[1])

# 전체 거리
total_distance = 0

# 모든 상점을 순회하면서
for direction, distance in stores:
    # 상점의 위치를 구함
    store_position = convert_position(direction, distance)

    # 시계방향, 시계반대방향 중 최소값을 더함
    total_distance += min(abs(position - store_position), P - abs(position - store_position))

print(total_distance)
```