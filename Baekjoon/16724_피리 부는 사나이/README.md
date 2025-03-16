# [16724] 피리 부는 사나이

### **난이도**
골드 3
## **📝문제**
피리 부는 사나이 성우는 오늘도 피리를 분다.

성우가 피리를 불 때면 영과일 회원들은 자기도 모르게 성우가 정해놓은 방향대로 움직이기 시작한다. 성우가 정해놓은 방향은 총 4가지로 U, D, L, R이고 각각 위, 아래, 왼쪽, 오른쪽으로 이동하게 한다.

이를 지켜보던 재훈이는 더 이상 움직이기 힘들어하는 영과일 회원들을 지키기 위해 특정 지점에 ‘SAFE ZONE’ 이라는 최첨단 방음 시설을 만들어 회원들이 성우의 피리 소리를 듣지 못하게 하려고 한다. 하지만 예산이 넉넉하지 않은 재훈이는 성우가 설정해 놓은 방향을 분석해서 최소 개수의 ‘SAFE ZONE’을 만들려 한다. 

성우가 설정한 방향 지도가 주어졌을 때 재훈이를 도와서 영과일 회원들이 지도 어느 구역에 있더라도 성우가 피리를 불 때 ‘SAFE ZONE’에 들어갈 수 있게 하는 ‘SAFE ZONE’의 최소 개수를 출력하는 프로그램을 작성하시오.
### **입력**
첫 번째 줄에 지도의 행의 수를 나타내는 N(1 ≤ N ≤ 1,000)과 지도의 열의 수를 나타내는 M(1 ≤ M ≤ 1,000)이 주어진다.

두 번째 줄부터 N개의 줄에 지도의 정보를 나타내는 길이가 M인 문자열이 주어진다.

지도 밖으로 나가는 방향의 입력은 주어지지 않는다.
### **출력**
첫 번째 줄에 ‘SAFE ZONE’의 최소 개수를 출력한다.
### **예제입출력**

**예제 입력1**

```
3 4
DLLL
DRLU
RRRU
```

**예제 출력1**

```
2
```
### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)
    
    if root_x != root_y:
        parent[root_y] = root_x
    


N, M = map(int, input().split())
table = [list(input()) for _ in range(N)]

parent = [i for i in range(N * M)]

move = {
    "D" : (1, 0),
    "U" : (-1, 0),
    "L" : (0, -1),
    "R" : (0, 1)
}

for i in range(N):
    for j in range(M):
        ni, nj = i + move[table[i][j]][0], j + move[table[i][j]][1]
        union(parent, i * M + j, ni * M + nj)

roots = set(find(parent, i) for i in range(N * M))
print(len(roots))
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|205144|684|PyPy3|685
#### **📝해설**

**알고리즘**
```
1. 분리 집합
```

### **다른 풀이**

```python
import sys

N, M = map(int, input().split())
mList = []
for i in range(N):
    mList.append(sys.stdin.readline().rstrip())

visited = [ [0] * M for i in range(N) ]
cnt = 0
ans = 0
for i in range(N):
    for j in range(M):
        if visited[i][j] == 0:
            cnt += 1
            x, y = j, i
            while True:
                if visited[y][x] != 0:
                    if visited[y][x] == cnt:
                        ans += 1
                    break

                visited[y][x] = cnt

                if mList[y][x] == "D":
                    y += 1

                elif mList[y][x] == "U":
                    y -= 1

                elif mList[y][x] == "L":
                    x -= 1

                elif mList[y][x] == "R":
                    x += 1

print(ans)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
juinha1220|119608|168|PyPy3|787
#### **📝해설**

```python
# 부모 노드 찾는 함수
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

# 분리 집합 합치는 함수
def union(parent, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)
    
    if root_x != root_y:
        parent[root_y] = root_x
    
# 입력받기
N, M = map(int, input().split())
table = [list(input()) for _ in range(N)]

# 부모 노드를 일차원 리스트로 저장
parent = [i for i in range(N * M)]

# 이동을 위한 딕셔너리
move = {
    "D" : (1, 0),
    "U" : (-1, 0),
    "L" : (0, -1),
    "R" : (0, 1)
}

# 테이블의 모든 값을 검사
for i in range(N):
    for j in range(M):

        # 이동한 뒤의 위치
        ni, nj = i + move[table[i][j]][0], j + move[table[i][j]][1]

        # 현재 위치와 이동한 뒤의 위치의 부모 노드를 합침
        union(parent, i * M + j, ni * M + nj)

# 분리집합이 몇개 생성되었는지 확인
roots = set(find(parent, i) for i in range(N * M))
print(len(roots))
```