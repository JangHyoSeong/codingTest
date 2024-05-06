# [16987] 계란으로 계란치기

### **난이도**
골드 5
## **📝문제**
원래 프로그래머의 기본 소양은 팔굽혀펴기를 단 한 개도 할 수 없는 것이라고 하지만 인범이는 3대 500을 넘기는 몇 안되는 프로그래머 중 한 명이다. 인범이는 BOJ에서 틀린 제출을 할 때마다 턱걸이를 5회 하는 기적의 운동 루틴을 통해 뇌와 근육을 동시에 단련한다. 근육을 단련할 때 식단이 정말로 중요하다는 것을 아는 인범이는 탄수화물이 많은 밥이나 빵 따위의 아침 식사를 대신해 단백질이 많은 계란찜을 해먹는다. 계란찜을 먹기 위해서는 계란을 깨야 하는데, 인범이는 힘이 너무 넘치는 나머지 부엌의 대리석을 이용해 계란을 깨면 늘 껍데기가 산산조각나 뒷처리가 너무 어렵게 되곤 한다. 어떻게 하면 계란을 조심스럽게 깰 수 있을까 고민하던 인범이에게 유현이는 굉장히 좋은 해결책을 알려주었다. 바로 계란으로 계란을 치는 것이다. 계란끼리 부딪쳐보니 껍데기가 아주 예쁘게 갈라지는 것을 발견한 인범이는 앞으로 계란으로 계란을 쳐서 식사 준비를 해야겠다고 생각했다. 유현이는 더 나아가 식사 준비를 할 때에도 두뇌를 단련할 수 있는 좋은 퍼즐을 인범이에게 알려주었다.

문제를 소개하기 전, 계란으로 계란을 치게 될 경우 어떤 일이 벌어지는지를 먼저 이해하고 가자. 각 계란에는 내구도와 무게가 정해져있다. 계란으로 계란을 치게 되면 각 계란의 내구도는 상대 계란의 무게만큼 깎이게 된다. 그리고 내구도가 0 이하가 되는 순간 계란은 깨지게 된다. 예를 들어 계란 1의 내구도가 7, 무게가 5이고 계란 2의 내구도가 3, 무게가 4라고 해보자. 계란 1으로 계란 2를 치게 되면 계란 1의 내구도는 4만큼 감소해 3이 되고 계란 2의 내구도는 5만큼 감소해 -2가 된다. 충돌 결과 계란 1은 아직 깨지지 않았고 계란 2는 깨졌다.

유현이가 인범이에게 알려준 퍼즐은 일렬로 놓여있는 계란에 대해 왼쪽부터 차례로 들어서 한 번씩만 다른 계란을 쳐 최대한 많은 계란을 깨는 문제였다. 구체적으로 계란을 치는 과정을 설명하면 아래와 같다.

1. 가장 왼쪽의 계란을 든다.
2. 손에 들고 있는 계란으로 깨지지 않은 다른 계란 중에서 하나를 친다. 단, 손에 든 계란이 깨졌거나 깨지지 않은 다른 계란이 없으면 치지 않고 넘어간다. 이후 손에 든 계란을 원래 자리에 내려놓고 3번 과정을 진행한다.
3. 가장 최근에 든 계란의 한 칸 오른쪽 계란을 손에 들고 2번 과정을 다시 진행한다. 단, 가장 최근에 든 계란이 가장 오른쪽에 위치한 계란일 경우 계란을 치는 과정을 종료한다.  
이 과정을 통해 최대한 많은 계란을 깨는 것이 앞으로 인범이가 매일 아침마다 풀게 될 퍼즐이다. 그리고 유현이는 인범이가 찾은 답이 정답이 맞는지 확인해주려고 한다. 일렬로 놓인 계란들의 내구도와 무게가 차례대로 주어졌을 때 최대 몇 개의 계란을 깰 수 있는지 알아맞춰보자.
### **입력**
첫째 줄에 계란의 수를 나타내는 N(1 ≤ N ≤ 8)가 주어진다. 그 다음 N개의 줄에는 계란의 내구도와 무게에 대한 정보가 주어진다. i+1번째 줄에는 왼쪽에서 i번째에 위치한 계란의 내구도 Si(1 ≤ Si ≤ 300)와 무게 Wi(1 ≤ Wi ≤ 300)가 한 칸의 빈칸을 사이에 두고 주어진다.
### **출력**
첫째 줄에 인범이가 깰 수 있는 계란의 최대 개수를 출력한다.
### **예제입출력**

**예제 입력1**

```
3
8 5
1 100
3 5
```

**예제 출력1**

```
3
```

**예제 입력2**

```
3
1 100
8 5
3 5
```

**예제 출력2**

```
2
```

**예제 입력3**

```
1
123 45
```

**예제 출력3**

```
0
```

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N = int(input())
eggs = [list(map(int, input().split())) for _ in range(N)]

max_crush = 0
def egg_crush(idx, N):

    global max_crush
    if idx == N:
        temp_crush = 0
        for i in range(N):
            if eggs[i][0] <= 0:
                temp_crush += 1
        max_crush = max(max_crush, temp_crush)
        return
    
    if eggs[idx][0] <= 0:
        egg_crush(idx+1, N)

    else:
        is_crashed = False
        for i in range(N):
            if idx == i or eggs[i][0] <= 0:
                continue
            is_crashed = True
            eggs[idx][0] -= eggs[i][1]
            eggs[i][0] -= eggs[idx][1]
            egg_crush(idx+1, N)
            eggs[idx][0] += eggs[i][1]
            eggs[i][0] += eggs[idx][1]
        
        if not is_crashed:
            egg_crush(N, N)

egg_crush(0, N)
print(max_crush)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
119736|960|PyPy3|837
#### **📝해설**

**알고리즘**
```
1. 백트래킹
```

### **다른 풀이**

```python
import sys
si = sys.stdin.readline
N = int(si())
S, W = [], []

for _ in range(N):
    a, b = map(int, si().split())
    S.append(a)
    W.append(b)


answer = 0


def dfs(num, cnt):
    global answer
    if num == N:
        answer = max(answer, cnt)
        return
    if S[num] <= 0:
        dfs(num+1, cnt)

    else:
        if cnt == N-1:
            answer = max(answer, cnt)
            return
        
        p = 0
        for _ in range(num+1, N):
            if S[_] <= 0:
                p += 1
        if cnt + (N - num-p)*2 <= answer:
            return
        for _ in range(N):
            if _ == num:
                continue
            if S[_] > 0:
                S[_] -= W[num]
                S[num] -= W[_]
                k = 0
                if S[_] <= 0:
                    k += 1
                if S[num] <= 0:
                    k += 1
                dfs(num+1, cnt + k)
                S[_] += W[num]
                S[num] += W[_]

dfs(0, 0)
print(answer)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
skyshr|117856|304|PyPy3|993
#### **📝해설**

```python
N = int(input())
eggs = [list(map(int, input().split())) for _ in range(N)]

# 전역변수로 사용할 최대 깬 횟수 변수
max_crush = 0


def egg_crush(idx, N):
    # 계란을 깨는 모든 경우의 수를 구할 함수
    global max_crush

    # 마지막 계란까지 모든 작업을 진행했다면
    if idx == N:
        temp_crush = 0
        # 이번 경우에서 계란이 깨진 개수를 구하고 최대값을 갱신
        for i in range(N):
            if eggs[i][0] <= 0:
                temp_crush += 1
        max_crush = max(max_crush, temp_crush)
        return
    
    # 만약 이번 계란이 이미 깨진 계란이라면 다음 계란으로 바로 이동
    if eggs[idx][0] <= 0:
        egg_crush(idx+1, N)

    # 만약 이번 계란이 깨져있지 않다면
    else:

        # 모든 계란이 깨져있는지 검사할 변수
        # 깰 수 있는 계란이 없다면 바로 계란 갯수를 구하는 작업으로 이동
        is_crashed = False
        for i in range(N):
            if idx == i or eggs[i][0] <= 0:
                continue
            # 계란을 하나라도 깨는 경우가 있다면 True로 바꾸어줌
            is_crashed = True

            # 계란의 내구도를 깎음
            eggs[idx][0] -= eggs[i][1]
            eggs[i][0] -= eggs[idx][1]
            # 다음 계란에 대해 작업 실시
            egg_crush(idx+1, N)
            # 계란의 내구도를 다시 돌려놓음
            eggs[idx][0] += eggs[i][1]
            eggs[i][0] += eggs[idx][1]
        
        # 깰 수 있는 계란이 없다면 바로 계란 갯수를 구하는 작업으로 이동
        # 이렇게 하지 않으면 재귀함수가 idx==N까지 실행되지 않음
        if not is_crashed:
            egg_crush(N, N)

egg_crush(0, N)
print(max_crush)
```

### **🔖정리**

1. 배운점