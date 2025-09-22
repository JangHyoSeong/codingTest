# [1911] 흙길 보수하기

### **난이도**
골드 5
## **📝문제**
어젯밤 겨울 캠프 장소에서 월드 본원까지 이어지는, 흙으로 된 비밀길 위에 폭우가 내려서 N(1 ≤ N ≤ 10,000)개의 물웅덩이가 생겼다. 월드학원은 물웅덩이를 덮을 수 있는 길이가 L(1 ≤ L ≤ 1,000,000)인 널빤지들을 충분히 가지고 있어서, 이들로 다리를 만들어 물웅덩이들을 모두 덮으려고 한다. 물웅덩이들의 위치와 크기에 대한 정보가 주어질 때, 모든 물웅덩이들을 덮기 위해 필요한 널빤지들의 최소 개수를 구하여라.
### **입력**
첫째 줄에 두 정수 N과 L이 들어온다.

둘째 줄부터 N+1번째 줄까지 총 N개의 줄에 각각의 웅덩이들의 정보가 주어진다. 웅덩이의 정보는 웅덩이의 시작 위치와 끝 위치로 이루어진다. 각 위치는 0 이상 1,000,000,000 이하의 정수이다. 입력으로 주어지는 웅덩이는 겹치지 않는다.
### **출력**
첫째 줄에 모든 물웅덩이들을 덮기 위해 필요한 널빤지들의 최소 개수를 출력한다.
### **예제입출력**

**예제 입력1**

```
3 3
1 6
13 17
8 12
```

**예제 출력1**

```
5
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys

N, L = map(int, sys.stdin.readline().rstrip().split())
ponds = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

ponds.sort()

count = 0
last = 0
for i in range(N):
    while last < ponds[i][1]:
        count += 1
        if last < ponds[i][0]:
            last = ponds[i][0] + L
        else:
            last += L

print(count)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|111740|2568|PyPy3|366
#### **📝해설**

**알고리즘**
```
1. 그리디 알고리즘
```

### **다른 풀이**

```python
import sys   
input = sys.stdin.readline

N, L = map(int, input().split())

waterhall = [tuple(map(int, input().split())) for _ in range(N)]

waterhall.sort(key=lambda x: x[0])

cnt = 0
temp = waterhall[0][0]
for start, end in waterhall:
    if start < temp:
        start = temp
    diff = end - start
    if diff % L == 0:
        cnt += diff // L
        temp = end
    else:
        temp2 = diff // L + 1
        cnt += temp2
        temp = end + temp2 * L - diff

print(cnt)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
aayy4321|32140|44|Python3|480
#### **📝해설**

```python
import sys

N, L = map(int, sys.stdin.readline().rstrip().split())
ponds = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

# 연못을 정렬
ponds.sort()

# 필요한 판자의 개수
count = 0

# 현재 판자가 이어진 마지막 좌표
last = 0
for i in range(N):

    # 판자가 웅덩이를 덮을 때 까지 반복
    while last < ponds[i][1]:
        count += 1

        # 판자가 웅덩이의 시작부분보다 뒤에있다면, 시작부분부터 새로 깔음
        if last < ponds[i][0]:
            last = ponds[i][0] + L

        # 아니라면, 현재 위치에 판자를 하나 추가
        else:
            last += L

print(count)
```