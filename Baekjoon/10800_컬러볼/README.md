# [10800] 컬러볼

### **난이도**
골드 2
## **📝문제**
지훈이가 최근에 즐기는 컴퓨터 게임이 있다. 이 게임은 여러 플레이어가 참여하며, 각 플레이어는 특정한 색과 크기를 가진 자기 공 하나를 조종하여 게임에 참여한다. 각 플레이어의 목표는 자기 공보다 크기가 작고 색이 다른 공을 사로잡아 그 공의 크기만큼의 점수를 얻는 것이다. 그리고 다른 공을 사로잡은 이후에도 본인의 공의 색과 크기는 변하지 않는다. 다음 예제는 네 개의 공이 있다. 편의상 색은 숫자로 표현한다.

공 번호 | 색 | 크기
------- | ------- | -------
1 | 1 | 10
2 | 3 | 15
3 | 1 | 3
4 | 4 | 8

이 경우, 2번 공은 다른 모든 공을 사로잡을 수 있다. 반면, 1번 공은 크기가 더 큰 2번 공과 색이 같은 3번 공은 잡을 수 없으며, 단지 4번 공만 잡을 수 있다. 

공들의 색과 크기가 주어졌을 때, 각 플레이어가 사로잡을 수 있는 모든 공들의 크기의 합을 출력하는 프로그램을 작성하시오. 
### **입력**
첫 줄에는 공의 개수를 나타내는 자연수 N이 주어진다(1 ≤ N ≤ 200,000). 다음 N개의 줄 중 i번째 줄에는 i번째 공의 색을 나타내는 자연수 Ci와 그 크기를 나타내는 자연수 Si가 주어진다(1 ≤ Ci ≤ N, 1 ≤ Si ≤ 2,000). 서로 같은 크기 혹은 같은 색의 공들이 있을 수 있다.
### **출력**
N개의 줄을 출력한다. N개의 줄 중 i번째 줄에는 i번째 공을 가진 플레이어가 잡을 수 있는 모든 공들의 크기 합을 출력한다.
### **예제입출력**

**예제 입력1**

```
4
1 10
3 15
1 3
4 8
```

**예제 출력1**

```
8
21
0
3
```

**예제 입력2**

```
3
2 3
2 5
2 4
```

**예제 출력2**

```
0
0
0
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys
from collections import defaultdict

N = int(sys.stdin.readline().rstrip())
balls = [list(map(int, sys.stdin.readline().rstrip().split())) + [i] for i in range(N)]

balls.sort(key= lambda x : (x[1], x[0]))
color = [0] * (N+1)
result = [0] * (N)

total = 0
j = 0
for i in range(N):
    while balls[j][1] < balls[i][1]:
        color[balls[j][0]] += balls[j][1]
        total += balls[j][1]
        j += 1
    result[balls[i][2]] = total - color[balls[i][0]]

print("\n".join(map(str, result)))
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|153136|672|PyPy3|503
#### **📝해설**

**알고리즘**
```
1. 정렬
2. 누적합
```

### **다른 풀이**

```python
import sys 
input = sys.stdin.readline 
n=int(input())
balls=[[] for _ in range(2001)]
for id in range(n):
    c,s=map(int,input().split())
    balls[s].append((c,id))

count={}
answer=[0]*n 
total=0
for i in range(1,2001):
    for c,id in balls[i]:
        if c not in count:
            count[c]=0 
        answer[id]=total-count[c]
    total+=i*len(balls[i])
    for c,id in balls[i]:
        count[c]+=i 
for i in range(n):
    print(answer[i])

```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
engineerjkk|158940|260|PyPy3|449
#### **📝해설**

```python
import sys
from collections import defaultdict

# 인덱스를 포함해서 입력받음
N = int(sys.stdin.readline().rstrip())
balls = [list(map(int, sys.stdin.readline().rstrip().split())) + [i] for i in range(N)]

# 크기를 기준으로 정렬
balls.sort(key= lambda x : (x[1], x[0]))

# 색깔마다 얼마만큼의 크기를 가지는지 누적합 저장
color = [0] * (N+1)

# 결과
result = [0] * (N)


# 현재까지 총 크기 총합
total = 0

# 투포인터를 위한 인덱스
j = 0

# 모든 공을 크기 기준 오름차순으로 순회하면서
for i in range(N):

    # 자신보다 작은 공을 만난다면 계속 반복
    while balls[j][1] < balls[i][1]:

        # 현재 색깔의 크기를 더함
        color[balls[j][0]] += balls[j][1]

        # 총 크기를 더함
        total += balls[j][1]

        # 인덱스를 1 증가
        j += 1

    # 결과에 자신의 색과 같은 색의 공의 크기 합을 제외하고 더함
    result[balls[i][2]] = total - color[balls[i][0]]

# 결과 출력
print("\n".join(map(str, result)))
```