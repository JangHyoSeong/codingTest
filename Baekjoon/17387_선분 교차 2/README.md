# [17387] 선분 교차 2

### **난이도**
골드 2
## **📝문제**
2차원 좌표 평면 위의 두 선분 L1, L2가 주어졌을 때, 두 선분이 교차하는지 아닌지 구해보자. 한 선분의 끝 점이 다른 선분이나 끝 점 위에 있는 것도 교차하는 것이다.

L1의 양 끝 점은 (x1, y1), (x2, y2), L2의 양 끝 점은 (x3, y3), (x4, y4)이다.
### **입력**
첫째 줄에 L1의 양 끝 점 x1, y1, x2, y2가, 둘째 줄에 L2의 양 끝 점 x3, y3, x4, y4가 주어진다.
### **출력**
L1과 L2가 교차하면 1, 아니면 0을 출력한다.
### **예제입출력**

**예제 입력1**

```
1 1 5 5
1 5 5 1
```

**예제 출력1**

```
1
```

**예제 입력2**

```
1 1 5 5
6 10 10 6
```

**예제 출력2**

```
0
```

**예제 입력3**

```
1 1 5 5
5 5 1 1
```

**예제 출력3**

```
1
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
def ccw(x1, y1, x2, y2, x3, y3):
    return (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)

def is_crossing(x1, y1, x2, y2, x3, y3, x4, y4):
    ccw1 = ccw(x1, y1, x2, y2, x3, y3)
    ccw2 = ccw(x1, y1, x2, y2, x4, y4)
    ccw3 = ccw(x3, y3, x4, y4, x1, y1)
    ccw4 = ccw(x3, y3, x4, y4, x2, y2)
    
    if ccw1 * ccw2 <= 0 and ccw3 * ccw4 <= 0:
        if ccw1 * ccw2 == 0 and ccw3 * ccw4 == 0:
            if (min(x1, x2) <= max(x3, x4) and min(x3, x4) <= max(x1, x2) and
                min(y1, y2) <= max(y3, y4) and min(y3, y4) <= max(y1, y2)):
                return 1
            else:
                return 0
        return 1
    return 0

# 입력
x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

# 결과 출력
print(is_crossing(x1, y1, x2, y2, x3, y3, x4, y4))
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|108080|88|Python3|812
#### **📝해설**

**알고리즘**
```
1. CCW 알고리즘
```

#### **📝해설**

```python
def ccw(x1, y1, x2, y2, x3, y3):
    # 세 점이 이루는 방향을 판단하는 함수
    return (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)

def is_crossing(x1, y1, x2, y2, x3, y3, x4, y4):

    # 각 모든 점에 대해 방향을 판단
    ccw1 = ccw(x1, y1, x2, y2, x3, y3)
    ccw2 = ccw(x1, y1, x2, y2, x4, y4)
    ccw3 = ccw(x3, y3, x4, y4, x1, y1)
    ccw4 = ccw(x3, y3, x4, y4, x2, y2)
    
    # 이 두 조건을 모두 만족하면 선분이 교차함
    if ccw1 * ccw2 <= 0 and ccw3 * ccw4 <= 0:

        # 두 선분이 한 직선상에 있는 경우
        if ccw1 * ccw2 == 0 and ccw3 * ccw4 == 0:

            # 두 선분이 만나는지 검증
            if (min(x1, x2) <= max(x3, x4) and min(x3, x4) <= max(x1, x2) and
                min(y1, y2) <= max(y3, y4) and min(y3, y4) <= max(y1, y2)):
                return 1
            else:
                return 0
        return 1
    return 0

# 입력
x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

# 결과 출력
print(is_crossing(x1, y1, x2, y2, x3, y3, x4, y4))
```