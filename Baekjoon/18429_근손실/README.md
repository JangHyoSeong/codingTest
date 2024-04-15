# [18429] 근손실

### **난이도**
실버 3
## **📝문제**
웨이트 트레이닝을 좋아하는 어떤 대학원생은, 현재 3대 운동 중량 500의 괴력을 소유하고 있다. 다만, 하루가 지날 때마다 중량이 K만큼 감소한다. 예를 들어 K=4일 때, 3일이 지나면 중량이 488로 감소하게 된다. 따라서 운동을 하지 않고, 가만히 있다면 매일매일 중량이 감소할 뿐이다.

다행히도 이 대학원생은 N개의 서로 다른 운동 키트를 가지고 있다. 이 대학원생은 하루에 1개씩의 키트를 사용하며, 매일 어떤 키트를 사용할 지는 마음대로 결정할 수 있다. 운동 키트들은 각각의 중량 증가량을 가지고 있으며, 사용할 때마다 즉시 중량이 증가하게 된다. 이 때 몇몇 운동 키트들의 중량 증가량이 같을 수 있으나, 서로 다른 운동 키트로 간주한다. 각각의 운동 키트는 N일 동안 한 번씩만 사용할 수 있다.

대학원생은 운동 기간동안 항상 중량이 500 이상으로 유지가 되도록 N일간의 운동 플랜을 세우고자 한다. 1일차부터 N일차까지의 모든 기간동안, 어떤 시점에서라도 중량이 500보다 작아지지 않도록 해야 한다.

예를 들어 N=3, K=4일 때, 각 운동 키트의 중량 증가량이 다음과 같다고 가정하자.



이 때 1번, 3번, 2번 순서대로 운동 키트를 적용한다고 해보자. 이 경우 운동 1일차에 대학원생은 중량이 3만큼 증가하지만 그와 동시에 하루에 중량이 4만큼 감소하기 때문에, 1일이 지난 이후에 중량은 499가 된다. 따라서 조건을 만족하지 못한다.

반면에 3번, 1번, 2번 순서대로 운동 키트를 적용한다고 해보자. 그러면 1일차부터 운동을 모두 마친 날까지의 모든 시점에 대하여 항상 중량이 500이상이 된다.

N개의 운동 키트에 대한 정보가 주어졌을 때, N일간 하루에 1개씩의 운동 키트를 사용하는 모든 경우 중에서, 운동 기간동안 항상 중량이 500 이상이 되도록 하는 경우의 수를 출력하는 프로그램을 작성하시오.

위 예시에서는 모든 경우 중에서 총 4가지 경우가 조건을 만족한다.


### **입력**
첫째 줄에 자연수 N과 K가 공백을 기준으로 구분되어 주어진다. (1 ≤ N ≤ 8, 1 ≤ K ≤ 50) 둘째 줄에 각 운동 키트의 중량 증가량 A가 공백을 기준으로 구분되어 주어진다. (1 ≤ A ≤ 50)
### **출력**
N일 동안 N개의 운동 키트를 사용하는 모든 경우 중에서, 운동 기간동안 항상 중량이 500 이상이 되도록 하는 경우의 수를 출력한다.
### **예제입출력**

**예제 입력1**

```
3 4
3 7 5
```

**예제 출력1**

```
4
```

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N, K = map(int, input().split())
kits = list(map(int, input().split()))


used = [False] * N
count = 0
routine = []

def workout(i, muscle):
    global count
    
    if i == N:
        muscle = muscle - K + routine[-1]
        if muscle < 500:
            return
        count += 1
        return
    
    for j in range(N):
        if not used[j]:
            used[j] = True
            routine.append(kits[j])
            new_muscle = muscle-K+routine[i]
            if new_muscle < 500:
                used[j] = False
                routine.pop()
                continue
            workout(i+1, new_muscle)
            used[j] = False
            routine.pop()
    
workout(0, 500)
print(count)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|111064|140|PyPy3|702
#### **📝해설**

**알고리즘**
```
1. 순열 생성
2. 백트래킹
```

### **다른 풀이**

```python
def dfs(cnt, total):
    global res
    if total < 500:
        return
    if total-(N-cnt)*K >= 500:
        temp = 1
        for i in range(1, N-cnt+1):
            temp *= i
        res += temp
        return
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            dfs(cnt+1, total+A[i]-K)
            visited[i] = 0

N, K = map(int, input().split())
A = list(map(int, input().split()))
visited = [0]*N
res = 0
dfs(0, 500)
print(res)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
pen2402|31256|52|Python3|470
#### **📝해설**

```python
N, K = map(int, input().split())
kits = list(map(int, input().split()))

# 현재 순열에 포함 여부를 나타낼 리스트
used = [False] * N

# 조건을 만족하는 경우의 수를 구할 변수
count = 0

# 현재 만들어지고 있는 순열
routine = []

def workout(i, muscle):
    # count를 전역변수로 선언
    global count
    
    # 만약 순열에서 N개의 수를 모두 골랐다면
    if i == N:
        # 현재 근력을 계산
        muscle = muscle - K + routine[-1]
        # 500을 넘지 못한다면 그냥 종료
        if muscle < 500:
            return
        
        # 500 이상이라면 count증가후 종료
        count += 1
        return
    
    # 아직 N개의 수를 모두 고르기 전이라면
    # N번 반복하면서, 아직 사용되지 않은 모든 숫자의 경우의수를 계산
    for j in range(N):
        # 아직 순열에 사용되지 않았다면
        if not used[j]:
            # 사용 처리
            used[j] = True
            # 순열에 숫자 삽입
            routine.append(kits[j])
            # 새로운 근력 계산
            new_muscle = muscle-K+routine[i]
            # 이번 숫자로 인해 500을 넘지 못한다면 리턴
            if new_muscle < 500:
                # 백트래킹. 원래대로 값을 돌려줌
                used[j] = False
                routine.pop()
                continue
            
            # 500을 넘었다면 다음 숫자를 고르러 진행
            workout(i+1, new_muscle)
            # 백트래킹. 원래대로 돌려줌
            used[j] = False
            routine.pop()
    
workout(0, 500)
print(count)
```