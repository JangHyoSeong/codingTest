# [17615] 볼 모으기

### **난이도**
실버 1
## **📝문제**
빨간색 볼과 파란색 볼이 <그림 1>에서 보인 것처럼 일직선상에 섞여 놓여 있을 때, 볼을 옮겨서 같은 색 볼끼리 인접하게 놓이도록 하려고 한다. 볼을 옮기는 규칙은 다음과 같다.

1. 바로 옆에 다른 색깔의 볼이 있으면 그 볼을 모두 뛰어 넘어 옮길 수 있다. 즉, 빨간색 볼은 옆에 있는 파란색 볼 무더기를 한 번에 뛰어 넘어 옮길 수 있다. 유사하게, 파란색 볼은 옆에 있는 빨간색 볼 무더기를 한 번에 뛰어 넘어 옮길 수 있다.
2. 옮길 수 있는 볼의 색깔은 한 가지이다. 즉, 빨간색 볼을 처음에 옮겼으면 다음에도 빨간색 볼만 옮길 수 있다. 유사하게, 파란색 볼을 처음에 옮겼으면 다음에도 파란색 볼만 옮길 수 있다.  
예를 들어, 처음에 볼이 <그림 1>에서 보인 것처럼 있을 때, 빨간 볼을 <그림 2>에서 보인 것처럼 옮긴 후, <그림 3>에서 보인 것처럼 옮긴다면 두 번 만에 같은 색끼리 모을 수 있다.

[이미지](https://upload.acmicpc.net/347db7e2-5704-4a28-ab85-682bf30f3816/-/crop/894x133/0,0/-/preview/)

<그림 1>

[이미지](https://upload.acmicpc.net/347db7e2-5704-4a28-ab85-682bf30f3816/-/crop/894x162/0,228/-/preview/)

<그림 2>

[이미지](https://upload.acmicpc.net/347db7e2-5704-4a28-ab85-682bf30f3816/-/crop/894x166/0,480/-/preview/)

<그림 3>

반면에 파란색 볼을 선택하여 에서 보인 것처럼 옮기면(화살표에 있는 수는 옮기는 순서를 나타낸다) 네 번을 옮겨야 같은 색의 볼끼리 모을 수 있다.

[이미지](https://upload.acmicpc.net/cf727ec0-1542-4ca1-bdb8-cfc695a5bdfa/-/preview/)

<그림 4>

일직선상에 놓여 있는 볼에 관한 정보가 주어질 때, 규칙에 따라 볼을 이동하여 같은 색끼리 모으되 최소 이동횟수를 찾는 프로그램을 작성하시오.
### **입력**
첫 번째 줄에는 볼의 총 개수 N이 주어진다. (1 ≤ N ≤ 500,000) 다음 줄에는 볼의 색깔을 나타내는 문자 R(빨간색 볼) 또는 B(파란색 볼)가 공백 없이 주어진다. 문자열에는 R 또는 B 중 한 종류만 주어질 수도 있으며, 이 경우 답은 0이 된다.
### **출력**
최소 이동횟수를 출력한다.
### **예제입출력**

**예제 입력1**

```
9
RBBBRBRRR
```

**예제 출력1**

```
2
```

**예제 입력2**

```
8
BBRBBBBR
```

**예제 출력2**

```
1
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys

N = int(sys.stdin.readline().strip())
balls = sys.stdin.readline().strip()

def count_moves(target):
    left_cnt = 0
    for ball in balls:
        if ball == target:
            left_cnt += 1
        else:
            break

    right_cnt = 0
    for ball in reversed(balls):
        if ball == target:
            right_cnt += 1
        else:
            break

    total_cnt = balls.count(target)
    return min(total_cnt - left_cnt, total_cnt - right_cnt)

result = min(count_moves('R'), count_moves('B'))
print(result)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|33392|84|Python3|536
#### **📝해설**

**알고리즘**
```
1. 그리디 알고리즘
```

### **다른 풀이**

```python
n = int(input())
balls = input()
r = balls.count('R')
b = balls.count('B')
print(min(r - n + len(balls.rstrip('R')), b - n + len(balls.rstrip('B')), r - n + len(balls.lstrip('R')), b - n + len(balls.lstrip('B'))))
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
po042|32100|40|Python3|213
#### **📝해설**

```python
import sys

N = int(sys.stdin.readline().strip())
balls = sys.stdin.readline().strip()

# 최소 이동횟수를 찾는 함수. target == 공의 색깔
def count_moves(target):

    # 왼쪽부터 연속한 공의 개수를 셈
    left_cnt = 0
    for ball in balls:
        if ball == target:
            left_cnt += 1
        else:
            break
    
    # 오른쪽부터 연속한 공의 색깔을 셈
    right_cnt = 0
    for ball in reversed(balls):
        if ball == target:
            right_cnt += 1
        else:
            break
    
    # 찾는 색깔의 공의 총 개수
    total_cnt = balls.count(target)

    # 오른쪽, 왼쪽 중 최소값을 리턴
    return min(total_cnt - left_cnt, total_cnt - right_cnt)

# 두 공 중에서 최소값을 찾음
result = min(count_moves('R'), count_moves('B'))
print(result)
```