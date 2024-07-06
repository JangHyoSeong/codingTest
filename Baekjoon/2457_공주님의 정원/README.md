# [2457] 공주님의 정원

### **난이도**
골드 3
## **📝문제**
오늘은 공주님이 태어난 경사스러운 날이다. 왕은 이 날을 기념하기 위해 늘 꽃이 피어있는 작은 정원을 만들기로 결정했다.

총 N개의 꽃이 있는 데, 꽃은 모두 같은 해에 피어서 같은 해에 진다. 하나의 꽃은 피는 날과 지는 날이 정해져 있다. 예를 들어, 5월 8일 피어서 6월 13일 지는 꽃은 5월 8일부터 6월 12일까지는 꽃이 피어 있고, 6월 13일을 포함하여 이후로는 꽃을 볼 수 없다는 의미이다. (올해는 4, 6, 9, 11월은 30일까지 있고, 1, 3, 5, 7, 8, 10, 12월은 31일까지 있으며, 2월은 28일까지만 있다.)

이러한 N개의 꽃들 중에서 다음의 두 조건을 만족하는 꽃들을 선택하고 싶다.

공주가 가장 좋아하는 계절인 3월 1일부터 11월 30일까지 매일 꽃이 한 가지 이상 피어 있도록 한다.
정원이 넓지 않으므로 정원에 심는 꽃들의 수를 가능한 적게 한다. 
N개의 꽃들 중에서 위의 두 조건을 만족하는, 즉 3월 1일부터 11월 30일까지 매일 꽃이 한 가지 이상 피어 있도록 꽃들을 선택할 때, 선택한 꽃들의 최소 개수를 출력하는 프로그램을 작성하시오. 
### **입력**
첫째 줄에는 꽃들의 총 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 다음 N개의 줄에는 각 꽃이 피는 날짜와 지는 날짜가 주어진다. 하나의 날짜는 월과 일을 나타내는 두 숫자로 표현된다. 예를 들어서, 3 8 7 31은 꽃이 3월 8일에 피어서 7월 31일에 진다는 것을 나타낸다. 
### **출력**
첫째 줄에 선택한 꽃들의 최소 개수를 출력한다. 만약 두 조건을 만족하는 꽃들을 선택할 수 없다면 0을 출력한다.
### **예제입출력**

**예제 입력1**

```
4
1 1 5 31
1 1 6 30
5 15 8 31
6 10 12 10
```

**예제 출력1**

```
2
```

**예제 입력2**

```
10
2 15 3 23
4 12 6 5
5 2 5 31
9 14 12 24
6 15 9 3
6 3 6 15
2 28 4 25
6 15 9 27
10 5 12 31
7 14 9 1
```

**예제 출력2**

```
5
```

### **출처**
Olympiad > 한국정보올림피아드 > 한국정보올림피아드시․도지역본선 > 지역본선 2011 > 초등부 3번

Olympiad > 한국정보올림피아드 > 한국정보올림피아드시․도지역본선 > 지역본선 2011 > 중등부 2번
## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N = int(input())

flowers = []
for _ in range(N):
    temp_input = list(map(int, input().split()))
    flowers.append([temp_input[0] * 100 + temp_input[1], temp_input[2] * 100 + temp_input[3]])
    
flowers.sort()

current_end = 301
count = 0
i = 0

while current_end <= 1130:
    max_end = current_end
    while i < N and flowers[i][0] <= current_end:
        if flowers[i][1] > max_end:
            max_end = flowers[i][1]
        i += 1
    
    if max_end == current_end:
        count = 0
        break
    current_end = max_end
    count += 1
    
print(count)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|124468|392|PyPy3|566
#### **📝해설**

**알고리즘**
```
1. 그리디 알고리즘
```

### **다른 풀이**

```python
import sys

input = sys.stdin.readline

def solution():
    N = int(input())
    calendar = [0]*(31*12+1)
    for _ in range(N):
        a, b, c, d = map(int, input().split())
        idx, val = (a-1)*31+b, (c-1)*31+d
        if val > calendar[idx]:
            calendar[idx] = val
    m = _m = 3
    d = _d = res = 1
    for i in range(31*12+1):
        if calendar[i]:
            sm = i//31+1
            sd = i%31
            if sm > m or (sm == m and sd > d):
                res += 1
                m, d = _m, _d
            if sm < m or (sm == m and sd <= d):
                em = calendar[i]//31+1
                ed = calendar[i]%31
                if em > _m or (em == _m and ed > _d):
                    _m, _d = em, ed
                    if _m > 11:
                        break
    if _m > 11:
        print(res)
    else:
        print(0)

solution()
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
pen2402|31256|140|Python3|868
#### **📝해설**

```python
N = int(input())

flowers = []
# 달과 날짜를 하나의 숫자로 합침
for _ in range(N):
    temp_input = list(map(int, input().split()))
    flowers.append([temp_input[0] * 100 + temp_input[1], temp_input[2] * 100 + temp_input[3]])

# 시작 날짜를 기준으로 정렬
flowers.sort()

# 현재 꽃이 지는 날짜
current_end = 301
count = 0
i = 0

# 11월 30일이 넘기 전까지 반복
while current_end <= 1130:

    # 현재 지는 날짜를 최대 날짜로 갱신
    max_end = current_end

    # 현재 꽃이 current_end 보다 작다면
    while i < N and flowers[i][0] <= current_end:

        # 현재 꽃이 선택한 꽃이 지는 날짜보다 크다면 갱신
        if flowers[i][1] > max_end:
            max_end = flowers[i][1]
        i += 1
    
    # 꽃을 하나도 추가못했다면 불가능한 케이스
    if max_end == current_end:
        count = 0
        break
    current_end = max_end
    count += 1
    
print(count)
```