# [2630] 색종이 만들기

### **난이도**
실버 2
## **📝문제**
아래 <그림 1>과 같이 여러개의 정사각형칸들로 이루어진 정사각형 모양의 종이가 주어져 있고, 각 정사각형들은 하얀색으로 칠해져 있거나 파란색으로 칠해져 있다. 주어진 종이를 일정한 규칙에 따라 잘라서 다양한 크기를 가진 정사각형 모양의 하얀색 또는 파란색 색종이를 만들려고 한다.

![이미지](https://www.acmicpc.net/upload/images/bwxBxc7ghGOedQfiT3p94KYj1y9aLR.png)

전체 종이의 크기가 N×N(N=2k, k는 1 이상 7 이하의 자연수) 이라면 종이를 자르는 규칙은 다음과 같다.

전체 종이가 모두 같은 색으로 칠해져 있지 않으면 가로와 세로로 중간 부분을 잘라서 <그림 2>의 I, II, III, IV와 같이 똑같은 크기의 네 개의 N/2 × N/2색종이로 나눈다. 나누어진 종이 I, II, III, IV 각각에 대해서도 앞에서와 마찬가지로 모두 같은 색으로 칠해져 있지 않으면 같은 방법으로 똑같은 크기의 네 개의 색종이로 나눈다. 이와 같은 과정을 잘라진 종이가 모두 하얀색 또는 모두 파란색으로 칠해져 있거나, 하나의 정사각형 칸이 되어 더 이상 자를 수 없을 때까지 반복한다.

위와 같은 규칙에 따라 잘랐을 때 <그림 3>은 <그림 1>의 종이를 처음 나눈 후의 상태를, <그림 4>는 두 번째 나눈 후의 상태를, <그림 5>는 최종적으로 만들어진 다양한 크기의 9장의 하얀색 색종이와 7장의 파란색 색종이를 보여주고 있다.

![이미지](https://www.acmicpc.net/upload/images/VHJpKWQDv.png)

입력으로 주어진 종이의 한 변의 길이 N과 각 정사각형칸의 색(하얀색 또는 파란색)이 주어질 때 잘라진 하얀색 색종이와 파란색 색종이의 개수를 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에는 전체 종이의 한 변의 길이 N이 주어져 있다. N은 2, 4, 8, 16, 32, 64, 128 중 하나이다. 색종이의 각 가로줄의 정사각형칸들의 색이 윗줄부터 차례로 둘째 줄부터 마지막 줄까지 주어진다. 하얀색으로 칠해진 칸은 0, 파란색으로 칠해진 칸은 1로 주어지며, 각 숫자 사이에는 빈칸이 하나씩 있다.
### **출력**
첫째 줄에는 잘라진 햐얀색 색종이의 개수를 출력하고, 둘째 줄에는 파란색 색종이의 개수를 출력한다.
### **예제입출력**

**예제 입력1**

```
8
1 1 0 0 0 0 1 1
1 1 0 0 0 0 1 1
0 0 0 0 1 1 0 0
0 0 0 0 1 1 0 0
1 0 0 0 1 1 1 1
0 1 0 0 1 1 1 1
0 0 1 1 1 1 1 1
0 0 1 1 1 1 1 1
```

**예제 출력1**

```
9
7
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]

white, blue = 0, 0

def count_color(x, y, size):
    global white, blue

    color = table[x][y]
    same = True

    for i in range(x, x + size):
        for j in range(y, y + size):
            if table[i][j] != color:
                same = False
                break
        
        if not same:
            break
    
    if same:
        if color == 0:
            white += 1
        
        else:
            blue += 1
    
    else:
        half = size // 2
        count_color(x, y, half)
        count_color(x, y + half, half)
        count_color(x + half, y, half)
        count_color(x + half, y + half, half)

count_color(0, 0, N)
print(white)
print(blue)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|32412|48|Python3|749
#### **📝해설**

**알고리즘**
```
1. 재귀
```

### **다른 풀이**

```python
N = int(input())
colored_paper = [list(map(int, input().split())) for _ in range(N)]
result = [0, 0]

def split_paper(x, y, width):
  if width == 1:
    if colored_paper[x][y] == 0:
      return (1, 0)
    else:
      return (0, 1)
  
  half = width // 2
  a = split_paper(x, y, half)
  b = split_paper(x+half, y, half)
  c = split_paper(x, y+half, half)
  d = split_paper(x+half, y+half, half)

  wh = a[0] + b[0] + c[0] + d[0]
  bl = a[1] + b[1] + c[1] + d[1]
  
  if bl == 0:
    return (1,0)
  elif wh == 0:
    return (0,1)
  else:
    return (wh, bl)

for i in split_paper(0, 0, N):
  print(i)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
dandilion|31120|36|Pytjon3|599
#### **📝해설**

```python
# 입력받기
N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]

# 흰색, 파란색의 개수
white, blue = 0, 0

# 재귀적으로 호출될 함수
def count_color(x, y, size):
    global white, blue

    # 현재 기준이 될 색깔
    color = table[x][y]
    same = True

    # 현재 구역을 확인하면서
    for i in range(x, x + size):
        for j in range(y, y + size):

            # 다른 색이 있다면 중지
            if table[i][j] != color:
                same = False
                break
        
        if not same:
            break
    
    # 모두 같은 색이라면 색종이 카운트
    if same:
        if color == 0:
            white += 1
        
        else:
            blue += 1
    
    # 다른 색이있더면 4개로 분할해서 탐색
    else:
        half = size // 2
        count_color(x, y, half)
        count_color(x, y + half, half)
        count_color(x + half, y, half)
        count_color(x + half, y + half, half)

# 재귀 시작
count_color(0, 0, N)
print(white)
print(blue)
```