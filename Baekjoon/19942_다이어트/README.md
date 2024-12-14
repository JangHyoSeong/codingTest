# [19942] 다이어트

### **난이도**
골드 4
## **📝문제**
식재료 N개 중에서 몇 개를 선택해서 이들의 영양분(단백질, 탄수화물, 지방, 비타민)이 일정 이상이 되어야 한다. 아래 표에 제시된 6가지의 식재료 중에서 몇 개를 선택해서 이들의 영양분의 각각 합이 최소 100, 70, 90, 10가 되도록 하는 경우를 생각해보자. 이 경우 모든 재료를 선택하면 쉽게 해결되지만, 우리는 조건을 만족시키면서도 비용이 최소가 되는 선택을 하려고 한다.

재료 | 단백질 | 지방 | 탄수화물 | 비타민 | 가격
---|-----|----|------|-----|---
1 | 30 | 55 | 10 | 8 | 100
2 | 60 | 10 | 10 | 2 | 70
3 | 10 | 80 | 50 | 0 | 50
4 | 40 | 30 | 30 | 8 | 60
5 | 60 | 10 | 70 | 2 | 120
6 | 20 | 70 | 50 | 4 | 40
예를 들어, 식재료 1, 3, 5를 선택하면 영양분은 100, 145, 130, 10으로 조건을 만족하지만 가격은 270이 된다. 대신 2, 3, 4를 선택하면 영양분의 합은 110, 130, 90, 10, 비용은 180이 되므로, 앞의 방법보다는 더 나은 선택이 된다.

입력으로 식재료 표가 주어졌을 때, 최저 영양소 기준을 만족하는 최소 비용의 식재료 집합을 찾아야 한다.
### **입력**
첫 줄에 식재료의 개수 
$N$이 주어진다.

다음 줄에는 단백질, 지방, 탄수화물, 비타민의 최소 영양성분을 나타내는 정수 
$mp$, 
$mf$, 
$ms$, 
$mv$가 주어진다.

이어지는 
$N$개의 각 줄에는 
$i$번째 식재료의 단백질, 지방, 탄수화물, 비타민과 가격이 5개의 정수 
$p_i$, 
$f_i$, 
$s_i$, 
$v_i$, 
$c_i$와 같이 주어진다. 식재료의 번호는 1부터 시작한다.
### **출력**
첫 번째 줄에 최소 비용을 출력하고, 두 번째 줄에 조건을 만족하는 최소 비용 식재료의 번호를 공백으로 구분해 오름차순으로 한 줄에 출력한다. 같은 비용의 집합이 하나 이상이면 사전 순으로 가장 빠른 것을 출력한다.

조건을 만족하는 답이 없다면 -1을 출력하고, 둘째 줄에 아무것도 출력하지 않는다.
### **예제입출력**

**예제 입력1**

```
6
100 70 90 10
30 55 10 8 100
60 10 10 2 70
10 80 50 0 50
40 30 30 8 60
60 10 70 2 120
20 70 50 4 4
```

**예제 출력1**

```
134
2 4 6
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N = int(input())
mp, mf, ms, mv = map(int, input().split())
foods = [list(map(int, input().split())) for _ in range(N)]

min_cost = float('inf')
best_combination = []

def select_food(idx, food, cost, protein, fat, carb, vitamin):
    global min_cost, best_combination

    if idx == N:
        if protein >= mp and fat >= mf and carb >= ms and vitamin >= mv:
            if cost < min_cost:
                min_cost = cost
                best_combination = food[:]
            elif cost == min_cost:
                if food < best_combination:
                    best_combination = food[:]
        return

    select_food(idx + 1, food, cost, protein, fat, carb, vitamin)

    current_food = foods[idx]

    select_food(idx + 1,
                food + [idx + 1],
                cost + current_food[4],
                protein + current_food[0],
                fat + current_food[1],
                carb + current_food[2],
                vitamin + current_food[3])

select_food(0, [], 0, 0, 0, 0, 0)

if min_cost == float('inf'):
    print(-1)
else:
    print(min_cost)
    print(' '.join(map(str, sorted(best_combination))))
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|32412|56|Python3|1131
#### **📝해설**

**알고리즘**
```
1. 백트래킹
```

#### **📝해설**

```python
N = int(input())
mp, mf, ms, mv = map(int, input().split())
foods = [list(map(int, input().split())) for _ in range(N)]

# 최소 비용
min_cost = float('inf')

# 최소비용일때의 음식조합
best_combination = []

# 재귀함수를 통해 각 음식을 선택할지 안할지 정함
def select_food(idx, food, cost, protein, fat, carb, vitamin):
    global min_cost, best_combination

    # 만약 모든 음식 선택을 마쳤다면
    if idx == N:

        # 조건을 만족하는지 검사
        if protein >= mp and fat >= mf and carb >= ms and vitamin >= mv:

            # 최소값이 갱신 가능하다면 갱신
            if cost < min_cost:
                min_cost = cost
                best_combination = food[:]

            # 사전순으로 빠른 것을 출력하도록 갱신
            elif cost == min_cost:
                if food < best_combination:
                    best_combination = food[:]
        return

    # 이번 음식을 선택하지 않고 넘기기
    select_food(idx + 1, food, cost, protein, fat, carb, vitamin)

    current_food = foods[idx]

    # 이번 음식을 선택하고 넘기기
    select_food(idx + 1,
                food + [idx + 1],
                cost + current_food[4],
                protein + current_food[0],
                fat + current_food[1],
                carb + current_food[2],
                vitamin + current_food[3])
# 재귀함수 시작
select_food(0, [], 0, 0, 0, 0, 0)

# 출력
if min_cost == float('inf'):
    print(-1)
else:
    print(min_cost)
    print(' '.join(map(str, sorted(best_combination))))
```

### **🔖정리**

1. 배운점