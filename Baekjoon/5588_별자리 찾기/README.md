# [5588] 별자리 찾기

### **난이도**
골드 5
## **📝문제**
상근이는 밤하늘 사진에서 별자리를 찾고 있다. 사진에는 꼭 찾고 싶은 별자리와 같은 형태, 방향, 크기의 도형이 한 개가 포함되어 있다. 하지만, 상근이가 가지고 있는 사진 속에는 별자리를 구성하는 별 이외에 다른 별도 찍혀 있다.

왼쪽 그림은 상근이가 찾고자하는 별자리이다. 오른쪽 그림은 상근이가 가지고 있는 별자리 사진이고, 상근이가 찾은 별자리의 별은 동그라미가 쳐져 있다. 주어진 별자리의 별 좌표를 x방향으로 2, y방향으로 -3만큼 평행 이동하면 사진 속 위치가 된다.

<img src="https://www.acmicpc.net/upload/images/star1.png">
<img src="https://www.acmicpc.net/upload/images/star2.png">

꼭 찾고 싶은 별자리의 모양과, 사진에 찍힌 별의 위치가 주어졌을 때, 별자리 좌표를 사진 속 좌표로 변환하기 위해 변환해야 하는 양을 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 찾고 싶은 별자리를 구성하는 별의 개수 m이 주어진다. 다음 m개 줄에는 별자리를 구성하는 별의 x좌표와 y좌표가 주어진다. 다음 줄에는 사진의 별의 개수 n이 주어진다. 다음 n개 줄에는 사진에 있는 별의 x좌표와 y좌표가 주어진다. (1 ≤ m ≤ 200, 1 ≤ n ≤ 1000) 별의 x 좌표와 y좌표는 0 이상, 1000000 이하이다.
### **출력**
첫째 줄에 찾고 싶은 별자리 좌표를 얼마나 평행 이동하면 사진 속의 좌표가 되는지를 출력한다. 첫 번째 정수는 x 방향으로 평행 이동하는 양이고, 두 번째 정수는 y 방향으로 평행 이동하는 양이다.
### **예제입출력**

**예제 입력1**

```
5
8 5
6 4
4 3
7 10
0 10
10
10 5
2 7
9 7
8 10
10 2
1 2
8 1
6 7
6 0
0 9
```

**예제 출력1**

```
2 -3
```

**예제 입력2**

```
5
904207 809784
845370 244806
499091 59863
638406 182509
435076 362268
10
757559 866424
114810 239537
519926 989458
461089 424480
674361 448440
81851 150384
459107 795405
299682 6700
254125 362183
50795 541942
```

**예제 출력2**

```
-384281 179674
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
m = int(input())
constellation = [tuple(map(int, input().split())) for _ in range(m)]

n = int(input())
photo = [tuple(map(int, input().split())) for _ in range(n)]

base_x, base_y = constellation[0]
relative_constellation = [(x - base_x, y - base_y) for x, y in constellation]

for star_x, star_y in photo:
    dx = star_x - base_x
    dy = star_y - base_y

    matched = True
    for rx, ry in relative_constellation:
        if (star_x + rx, star_y + ry) not in photo:
            matched = False
            break

    if matched:
        print(dx, dy)
        break
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|31120|684|Python3|570
#### **📝해설**

**알고리즘**
```
1. 브루트포스
```

### **다른 풀이**

```python
import sys

input = sys.stdin.readline


def is_valid_offset(dx, dy, target, A):
    for tx, ty in target:
        if (tx + dx, ty + dy) not in A:
            return False
    return True


M = int(input())
target = [tuple(map(int, input().rstrip().split())) for _ in range(M)]
N = int(input())
A = set(tuple(map(int, input().rstrip().split())) for _ in range(N))

tx0, ty0 = target[0]

for ax, ay in A:
    dx, dy = ax - tx0, ay - ty0

    if is_valid_offset(dx, dy, target, A):
        print(dx, dy)
        break

```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
bavocado1031|31120|36|Python3|516

#### **📝해설**

```python
# 입력받기
m = int(input())
constellation = [tuple(map(int, input().split())) for _ in range(m)]

n = int(input())
photo = [tuple(map(int, input().split())) for _ in range(n)]


# 기준점을 하나 정함
base_x, base_y = constellation[0]

# 기준점 기준으로 각 떨어져있는 좌표를 구함
relative_constellation = [(x - base_x, y - base_y) for x, y in constellation]


# 사진의 별을 하나씩 순회하면서
for star_x, star_y in photo:
    dx = star_x - base_x
    dy = star_y - base_y

    # 사진속에 패턴이 있는지 확인
    matched = True
    for rx, ry in relative_constellation:
        if (star_x + rx, star_y + ry) not in photo:
            matched = False
            break

    if matched:
        print(dx, dy)
        break
```