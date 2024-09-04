# [20293] 연료가 부족해

### **난이도**
골드 2
## **📝문제**
피라미드를 직접 보는 게 소원이었던 향빈이는 사막 투어 여행패키지를 신청하게 되었다. 그리고 여행 둘째 날에 사막 입구에 도착해서 사막 투어용 자동차에 탑승했다.

출발하기 전 들뜬 마음으로 자동차 안에 앉아있던 향빈이는 사막 투어 가이드북을 발견했다. 가이드북 안의 
$R \times C$ 크기의 지도에는 연료 보관소 
$N$곳의 위치와 연료 보관소마다 보관하고 있는 연료량이 표시되어 있었다.

평소에 자동차 덕후였던 향빈이는 모든 자동차의 연비를 외우고 있었고, 현재 탑승한 자동차가 
$1$만큼의 거리를 움직일 때 연료를 
$1$만큼 소비한다는 것을 알고 있다. 또한, 자동차는 지도의 
$x$축 또는 
$y$축과 평행한 방향으로만 주행한다. 따라서 예를 들어 자동차가 
$\left(0,0\right)$에서 
$\left(i,j\right)$까지 최단 거리로 움직인다면 연료는 
$i+j$만큼 소비할 것이다.

현재 자동차의 연료가 없는 관계로, 여기에 있는 주유소에서 연료를 충전하고 나서 출발하려 한다. 하지만 주유소에서 파는 연료는 매우 비싸기 때문에, 향빈이는 여기서는 연료를 되도록 최소로 충전하고 이후에는 이동하면서 방문하는 연료 보관소에서 연료를 충전할 계획이다.

향빈이는 얼른 피라미드를 보고 싶기 때문에 운전사분께 피라미드와 멀어지는 방향으로는 운전하지 말아 달라고 부탁했다. 즉, 자동차는 오직 오른쪽이나 아래쪽으로만 이동한다. 

주유소에서 충전 가능한 연료량에는 제한이 없으며, 현재 위치와 피라미드가 있는 위치에는 연료 보관소가 없다. 또한, 한 위치에 두 개 이상의 연료 보관소가 있는 경우는 없다.

문제는 연료 보관소마다 위치와 보관된 연료량이 다르기 때문에, 연료보관소들을 어떤 순서로 경유해서 이동하는가에 따라 처음 충전해야 하는 연료량이 달라질 수 있다는 점이다. 현 위치인 
$\left(1,1\right)$에서 피라미드가 있는 지점인 
$\left(R,C\right)$까지 가기 위해 주유소에서 충전해야 하는 연료량의 최솟값을 구해보자.
### **입력**
첫째 줄에 지도의 세로 길이와 가로 길이를 나타내는 정수 
$R$, 
$C$가 주어진다. (
$2 \leq R, C \leq 3\ 000$)

둘째 줄에 지도에 표시된 연료 보관소의 개수를 나타내는 정수 
$N$이 주어진다. (
$0 \leq N \leq 1\ 000$)

셋째 줄부터 
$N$개 줄에 각 연료 보관소의 위치를 나타내는 정수 좌표 
$\left(r,c\right)$와 보관중인 연료량을 나타내는 정수 
$f$가 주어진다. (
$1 \leq r \leq R$, 
$1 \leq c \leq C$, 
$0 \leq f \leq 100$)
### **출력**
향빈이가 현 위치인 
$\left(1,1\right)$에서 피라미드가 있는 지점인 
$\left(R,C\right)$까지 가기 위해 주유소에서 충전해야 하는 연료량의 최솟값을 출력한다.
### **예제입출력**

**예제 입력1**

```
3 3
1
2 2 1
```

**예제 출력1**

```
3
```

**예제 입력2**

```
5 5
3
2 2 1
3 4 2
4 3 4
```

**예제 출력2**

```
4
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys
input = sys.stdin.readline

R, C = map(int, input().split())
n = int(input())

graph = [[0 for _ in range(C)] for _ in range(R)]

for i in range(n):
    a,b,c = map(int, input().split())
    graph[a-1][b-1] = c

def find(initial_fuel):

    dp = [[0 for _ in range(C)] for _ in range(R)]
    dp[0][0] = initial_fuel

    for i in range(R):
        for j in range(C):
            if i == 0 and j == 0:
                continue

            if i == 0:
                dp[i][j] = dp[i][j-1] - 1

            elif j == 0:
                dp[i][j] = dp[i-1][j] - 1

            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j]) - 1

            if graph[i][j]:
                if dp[i][j] >= 0:
                    dp[i][j] += graph[i][j]

    if dp[R-1][C-1] < 0:
        return False
    
    return True


start = 0
end = R+C


while start <= end:
    mid = (start + end) // 2

    if find(mid):
        end = mid - 1

    else:
        start = mid + 1

print(start)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|392700|3248|PyPy3|979
#### **📝해설**

**알고리즘**
```
1. DP
2. 이분 탐색
```

### **다른 풀이**

```python
import sys
input=sys.stdin.readline

def check(n):
    dp=[-1]*(N+2)
    dp[0]=n
    gas[0][2]=n
    for i in range(1,N+2):
        for j in range(i):
            if gas[j][0]>gas[i][0] or gas[j][1]>gas[i][1]:
                continue
            if dp[j]<(gas[i][0]-gas[j][0]+gas[i][1]-gas[j][1]):
                continue
            dp[i]=max(dp[i],dp[j]-(gas[i][0]-gas[j][0]+gas[i][1]-gas[j][1])+gas[i][2])
    return dp[-1]>=0

R,C=map(int,input().split())
N=int(input())
gas=[]
for _ in range(N):
    gas.append(list(map(int,input().split())))
gas.append([1,1,0])
gas.append([R,C,0])
gas.sort(key=lambda x:x[0]+x[1])
start=1
end=R+C-2
while start<end:
    mid=(start+end)//2
    if check(mid):
        end=mid
    else:
        start=mid+1
print(end)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
easteregg423|116452|416|PyPy3|756
#### **📝해설**

```python
import sys
input = sys.stdin.readline

R, C = map(int, input().split())
n = int(input())

# 그래프에 연료보급 정보 추가
graph = [[0 for _ in range(C)] for _ in range(R)]

for i in range(n):
    a,b,c = map(int, input().split())
    graph[a-1][b-1] = c

# 시작 연료를 기준으로 R, C에 도달할 수 있는지 확인
def find(initial_fuel):

    # dp배열 초기화
    dp = [[0 for _ in range(C)] for _ in range(R)]

    # 시작 연료
    dp[0][0] = initial_fuel

    # dp 배열 작성
    for i in range(R):
        for j in range(C):
            
            # 0인 경우 처리
            if i == 0 and j == 0:
                continue

            if i == 0:
                dp[i][j] = dp[i][j-1] - 1

            elif j == 0:
                dp[i][j] = dp[i-1][j] - 1

            # 위나 왼쪽에서 온 것 중에 작은 것을 선택
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j]) - 1

            # 현재 위치에 정류장이 있고, 현재 연료가 아직 남아있다면
            if graph[i][j]:
                if dp[i][j] >= 0:
                  # 연료 보급
                    dp[i][j] += graph[i][j]
                  # 연료가 남아있지 않다면 이미 이번 케이스는 불가능

    # 도착할수없다면 False
    if dp[R-1][C-1] < 0:
        return False
    
    return True


start = 0
end = R+C


while start <= end:
    mid = (start + end) // 2

    if find(mid):
        end = mid - 1

    else:
        start = mid + 1

print(start)
```

### **🔖정리**

1. 이분탐색을 적용할 거리를 잘 찾아보자