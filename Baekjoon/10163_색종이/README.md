# [10163] 색종이

### **난이도**
브론즈 1
## **📝문제**
평면에 색깔이 서로 다른 직사각형 모양의 색종이 N장이 하나씩 차례로 놓여진다. 이때 색종이가 비스듬하게 놓이는 경우는 없다. 즉, 모든 색종이의 변은 서로 평행하거나, 서로 수직이거나 둘 중 하나이다. 그림-1은 1번, 2번, 3번 세 장의 색종이가 순서대로 놓인 상태를 보여준다.



여기에 그림-2에서 보인 것처럼 4번 색종이가 하나 더 놓이면 3번 색종이는 완전히 가려서 보이지 않게 된다. 그리고, 1번 색종이와 2번 색종이는 부분적으로 가려 보이며, 4번 색종이는 완전히 보이게 된다.



N장의 색종이가 주어진 위치에 차례로 놓일 경우, 각 색종이가 보이는 부분의 면적을 구하는 프로그램을 작성하시오. 

### **입력**
입력의 첫 번째 줄에는 색종이의 장수를 나타내는 정수 N (1 ≤ N ≤ 100)이 주어진다. 이어서 N장의 색종이에 관한 입력이 각 색종이마다 한 줄씩 차례로 주어진다. 색종이가 놓이는 평면은 가로 최대 1001칸, 세로 최대 1001칸으로 구성된 격자 모양이다. 격자의 각 칸은 가로, 세로 길이가 1인 면적이 1인 정사각형이다. 

편의상 가로 6칸, 세로 6칸으로 이루어진 격자의 예를 들어 설명하면, 각 칸에 표시된 값 (a,b)는 해당 칸의 번호를 나타낸다. 가장 왼쪽 아래의 칸은 (0,0) 가장 오른 쪽 위의 칸은 (5,5)이다. 



색종이가 놓인 상태는 가장 왼쪽 아래 칸의 번호와 너비, 높이를 나타내는 네 정수로 표현한다. 예를 들어, 위 그림에서 회색으로 표시된 색종이는 (1,4)가 가장 왼쪽 아래에 있고 너비 3, 높이 2이므로 1 4 3 2로 표현한다. 색종이가 격자 경계 밖으로 나가는 경우는 없다. 
### **출력**
입력에서 주어진 순서에 따라 N장의 색종이를 평면에 놓았을 때, 입력에서 주어진 순서대로 각 색종이가 보이는 부분의 면적을 한 줄에 하나씩 하나의 정수로 출력한다. 만약 색종이가 보이지 않는다면 정수 0을 출력한다. 
### **예제입출력**

**예제 입력1**

```
2
0 0 10 10
2 2 6 6
```

**예제 출력1**

```
64
36
```

**예제 입력2**

```
3
0 2 10 10
7 9 8 4
8 4 10 6
```

**예제 출력2**

```
81
25
60
```

**예제 입력3**

```
4
0 2 10 10
7 9 8 4
8 4 10 6
6 0 12 10
```

**예제 출력3**

```
62
24
0
120
```

### **출처**
Olympiad > 한국정보올림피아드 > KOI 2014 > 초등부 2번
## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N = int(input())

paper = [list(map(int, input().split())) for _ in range(N)]
paper_area = [0] * N

area = [[-1] * 1001 for _ in range(1001)]

for i in range(N):
    for j in range(paper[i][0], paper[i][0] + paper[i][2]):
        for k in range(paper[i][1], paper[i][1] + paper[i][3]):
            area[j][k] = i

for i in range(1001):
    for j in range(1001):
        if area[i][j] == -1:
            continue
        paper_area[area[i][j]] += 1

for i in paper_area:
    print(i)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|38432|152|Python3|435
#### **📝해설**

**알고리즘**
```
1. 구현
```

#### **😅개선점**

1. 지금은 단순히 구현을 하고 있는데, 좀 더 최적화해서 시간, 공간복잡도를 줄일 수 있을 것 같다 

### **다른 풀이**

```python
import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
queries, line_x, line_y = [], set(), set()

for _ in range(N):
	q = list(map(int, input().split()))
	x1, y1, x2, y2 = q[0], q[1], q[0] + q[2], q[1] + q[3]
	queries.append((x1, y1, x2, y2))
	line_x.add(x1)
	line_x.add(x2)
	line_y.add(y1)
	line_y.add(y2)

line_x = sorted(line_x)
line_y = sorted(line_y)
comp_x = {v: i for i, v in enumerate(line_x)}
comp_y = {v: i for i, v in enumerate(line_y)}
dx = [line_x[i] - line_x[i - 1] for i in range(1, len(line_x))]
dy = [line_y[i] - line_y[i - 1] for i in range(1, len(line_y))]

paper = [[0] * len(dx) for _ in range(len(dy))]

for i in range(1, len(queries) + 1):
	x1, y1, x2, y2 = queries[i - 1]
	for x in range(comp_x[x1], comp_x[x2]):
		for y in range(comp_y[y1], comp_y[y2]):
			paper[y][x] = i

ans = [0] * (N + 1)
for y in range(len(paper)):
	for x in range(len(paper[0])):
		ans[paper[y][x]] += dx[x] * dy[y]

print('\n'.join(map(str, ans[1:])))
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
rkaxhdals|29200|104|Python3|979