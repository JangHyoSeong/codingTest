# [7573] 고기잡이

### **난이도**
골드 3
## **📝문제**
한국인의 식단에서 생선은 매우 중요한 단백질 공급원이다. 반면, 지구 온난화로 인한 바닷물의 온도 상승, 그리고 지금까지 마구잡이로 물고기를 잡은 결과로 점점 우리나라의 바다에서 물고기의 수가 줄어들고 있다. 정부에서는 이 문제를 심각하게 생각하여, 물고기를 잡을 수 있는 곳과 여기서 고기잡이 배가 사용할 수 있는 그물의 폭에 제한을 두었다. 물고기는 바다 표면 근처에 살기 때문에, 그물의 높이는 중요하지 않다. 따라서 그물은 길이가 l인 직선으로 생각할 수 있고, 물고기를 잡을 때, 그물은 한 변의 길이가 1 이상 정수인 직사각형 모양으로 치게 된다. 예를 들어, l = 10이라면, 칠 수 있는 그물의 모양은 1×4, 2×3, 3×2, 4×1과 같이 4가지 형태의 직사각형이 된다.

고기를 잡을 수 있는 곳은 N×N 크기의 모눈종이 모양으로 되어 있다. 각 모눈에는 좌표가 주어지며, 가장 왼쪽 위 모눈이 (1,1)이고, 가장 오른쪽 아래 모눈이 (N,N)이다. 총 M 마리의 물고기가 서로 다른 모눈 위에 한 마리씩 살고 있으며, 물고기는 움직이지 않는다. 고기잡이 배는 한 모눈 위에 위치를 잡고 자신의 오른쪽과 아래쪽으로 그물을 친다. 일단 그물을 치면, 그물 안, 그리고 그물에 걸친 물고기들을 잡을 수 있다. 예를 들면, 다음 그림은 N = 7, l = 10 이고 M = 6 마리의 물고기가 (2,2), (2,4), (3,3), (5,6), (6,2), (7,4)에 살고 있을 때, (2,2)에 놓인 고기잡이 배가 2×3 모양으로 그물을 친 예를 보이고 있다. 이때 고기잡이 배는 총 3마리의 물고기를 잡을 수 있다. 고기를 잡을 수 있는 영역 밖으로 그물을 치는 경우는 없다.

![이미지](https://upload.acmicpc.net/b198ba72-f675-4909-8dd1-f7bc302b15cf/-/preview/)

고기를 잡을 수 있는 영역, 물고기의 위치, 그물의 폭이 주어졌을 때 한 번의 그물치기로 잡을 수 있는 가장 많은 물고기의 마릿수를 구하는 프로그램을 작성하시오.
### **입력**
첫 번째 줄에는 모눈종이의 크기, 그물의 길이, 물고기의 수를 나타내는 세 개의 정수 N, l, M이 하나의 공백을 두고 주어진다. 단, 2 ≤ N ≤ 10,000, 4 ≤ l ≤ 100, 1 ≤ M ≤100 이다. l은 l ≤ 4N - 4을 만족하는 짝수이다. 두 번째 줄부터 이후 M 개의 줄에는 각 물고기의 좌표가 하나의 공백을 두고 주어진다. 물고기의 좌표 순서는 무작위로 주어진다.
### **출력**
첫 줄에 주어진 입력에서 잡을 수 있는 가장 많은 물고기의 마릿수를 하나의 정수로 출력한다.
### **예제입출력**

**예제 입력1**

```
7 10 6
2 2
2 4
6 2
7 4
3 3
5 6
```

**예제 출력1**

```
3
```
### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N, I, M = map(int, input().split())
fish = [tuple(map(int, input().split())) for _ in range(M)]

rects = []
half = I // 2
for w in range(1, half):
    h = half - w
    rects.append((w, h))
    
    if w != h:
        rects.append((h, w))

answer = 0

xs = sorted({x for x, _ in fish})
ys = sorted({y for _, y in fish})

for x in xs:
    for y in ys:
        for w, h in rects:

            if x + h - 1 <= N and y + w - 1 <= N:
                count = 0
                for fx, fy in fish:
                    if x <= fx <= x + h and y <= fy <= y + w:
                        count += 1
                
                answer = max(answer, count)

print(answer)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|111476|804|PyPy3|679
#### **📝해설**

**알고리즘**
```
1. 브루트포스 알고리즘
```

### **다른 풀이**

```python
import sys

n,l,m = map(int,sys.stdin.readline().split())
fishes = sorted([list(map(int,sys.stdin.readline().split())) for _ in range(m)])
fishesY = [fish[1] for fish in fishes]
l//=2

result=0
# 그물 크기 구하기
for w in range(1,l):
    h=l-w

    # i번째 물고기와 같은 그물에 있을 수 있는 물고기 구하기 (x 확인)
    j=0
    for i in range(m):
        while j<m and fishes[j][0]-fishes[i][0]<=h:
            j+=1
        targetFishes = sorted(fishesY[i:j])

        # ii번째 물고기와 같은 그물에 있을 수 있는 물고기 구하기 (y 확인)
        jj=0
        for ii in range(j-i):
            while jj<j-i and targetFishes[jj]-targetFishes[ii]<=w:
                jj+=1
            result = max(result,jj-ii)
print(result)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
dbswl4951|31256|96|Python3|772
#### **📝해설**

```python
N, I, M = map(int, input().split())
fish = [tuple(map(int, input().split())) for _ in range(M)]

# 현재 그물 길이로 만들 수 있는 직사각형을 저장
rects = []
half = I // 2
for w in range(1, half):
    h = half - w
    rects.append((w, h))
    
    # 정사각형이 아닌 경우, 세로 가로를 바꾼 값도 저장
    if w != h:
        rects.append((h, w))

answer = 0

# 물고기의 x, y좌표를 모두 확인
xs = sorted({x for x, _ in fish})
ys = sorted({y for _, y in fish})

# 모든 물고기의 x, y좌표에서 그물을 침
for x in xs:
    for y in ys:
        for w, h in rects:
            
            # 그물이 영역을 벗어나지 않을 때
            if x + h - 1 <= N and y + w - 1 <= N:
                count = 0

                # 잡을 수 있는 물고기를 확인
                for fx, fy in fish:
                    if x <= fx <= x + h and y <= fy <= y + w:
                        count += 1
                
                answer = max(answer, count)

print(answer)
```