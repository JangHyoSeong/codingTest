# [2258] 정육점

### **난이도**
골드 3
## **📝문제**
은혜는 정육점에서 고기를 사려고 한다. 보통 정육점에서는 자신이 원하는 양을 이야기하면 그 양만큼의 고기를 팔지만, 은혜가 방문한 정육점에서는 세일 행사를 하고 있었기 때문에 N 덩어리의 고기를 이미 잘라놓고 판매하고 있었다.

각각의 덩어리들은 이미 정해져 있는 무게와 가격이 있는데, 어떤 덩어리를 샀을 때에는 그 덩어리보다 싼 고기들은 얼마든지 덤으로 얻을 수 있다(추가 비용의 지불 없이). 또한 각각의 고기들은 부위가 다를 수 있기 때문에 비용과 무게와의 관계가 서로 비례하는 관계가 아닐 수도 있다. 은혜는 이러한 점을 고려하지 않고, 어느 부위든지 자신이 원하는 양만 구매하면 되는 것으로 가정한다. 또한 만약 가격이 더 싸다면 은혜가 필요한 양보다 더 많은 고기를 살 수도 있다.

각 덩어리에 대한 정보가 주어졌을 때, 은혜가 원하는 양의 고기를 구매하기 위해 필요한 최소 비용을 계산하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 두 정수 N(1 ≤ N ≤ 100,000), M(1 ≤ M ≤ 2,147,483,647)이 주어진다. N은 덩어리의 개수를 의미하고, M은 은혜가 필요한 고기의 양이다. 다음 N개의 줄에는 각 고기 덩어리의 무게와 가격을 나타내는 음 아닌 두 정수가 주어진다. 무게의 총 합과 가격의 총 합은 각각 2,147,483,647을 넘지 않는다.
### **출력**
첫째 줄에 답을 출력한다. 불가능한 경우에는 -1을 출력한다.
### **예제입출력**

**예제 입력1**

```
4 9
1 2
2 4
3 6
4 8
```

**예제 출력1**

```
8
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
meats = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

meats.sort(key = lambda x : (x[1], -x[0]))

weight_sum = 0
max_cost, total_cost = 0, 0

for i in range(N):
    weight, cost = meats[i]

    if weight_sum < M:
        weight_sum += weight
        
        if max_cost == cost:
            total_cost += cost
        else:
            max_cost = cost
            total_cost = cost
    
    elif max_cost == cost:
        continue

    elif total_cost > cost:
        total_cost = cost
        break

    else:
        break

if weight_sum < M:
    print(-1)
else:
    print(total_cost)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|127656|336|PyPy3|683
#### **📝해설**

**알고리즘**
```
1. 그리디 알고리즘
```

### **다른 풀이**

```python
def solve():
    import sys
    input = sys.stdin.readline

    # 입력받기
    N, M = map(int, input().split())
    pieces = []
    for _ in range(N):
        weight, price = map(int, input().split())
        pieces.append((price, weight))
    
    # 가격 기준 오름차순 정렬
    pieces.sort(key=lambda x: x[0])
    
    # 가격이 같은 덩어리끼리 그룹화 (각 그룹: (price, [weights]))
    groups = []
    current_price = None
    current_group = []
    for price, weight in pieces:
        if price != current_price:
            if current_group:
                groups.append((current_price, current_group))
            current_price = price
            current_group = [weight]
        else:
            current_group.append(weight)
    if current_group:
        groups.append((current_price, current_group))
    
    best = None  # 최소 비용
    cumulative = 0  # 지금까지 무료로 얻을 수 있는 무게 합 (즉, 이전 그룹의 모든 무게)
    
    # 각 그룹(즉, 각 가능한 최대 가격 T)에 대해 후보비용 계산
    for price, group in groups:
        # 그룹 내 덩어리들을 무게 내림차순으로 정렬하여
        # 적은 개수로 필요한 무게를 채울 수 있도록 함.
        group.sort(reverse=True)
        
        # 현재까지 무료로 얻을 수 있는 무게와 합쳐서 M을 채워야 함.
        needed = M - cumulative
        
        if needed <= 0:
            # 이미 무료로 얻는 고기의 무게가 M 이상이므로,
            # 단, 무료 혜택을 받으려면 반드시 한 덩어리(가격 price)를 구매해야 함.
            candidate = price
        else:
            # 현재 그룹에서 필요한 무게를 채우기 위해 몇 개 구매해야 하는지 구하기
            s = 0
            count = 0
            for w in group:
                s += w
                count += 1
                if s >= needed:
                    break
            if s < needed:
                candidate = None  # 현재 그룹으로는 M을 채울 수 없음.
            else:
                candidate = count * price
        
        if candidate is not None:
            if best is None or candidate < best:
                best = candidate
        
        # 무료로 얻을 수 있는 무게에 현재 그룹의 모든 덩어리 무게를 추가
        cumulative += sum(group)
    
    if best is None:
        sys.stdout.write("-1")
    else:
        sys.stdout.write(str(best))


solve()
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
se1620236|48052|156|Python3|2521
#### **📝해설**

```python
import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
meats = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

# 고기를 가격기준으로 오름차순, 무게 순으로 내림차순 정렬
meats.sort(key = lambda x : (x[1], -x[0]))

# 고기를 가격순으로 조회할 때, 그 때의 총 무게합
weight_sum = 0

# 고기를 조회할 때, 고기 가격의 최대값, 그 때 지불할 비용의 최대값
max_cost, total_cost = 0, 0

for i in range(N):
    weight, cost = meats[i]

    # 아직 목표무게가 되지 못했다면 이번 고기의 무게를 더함
    if weight_sum < M:
        weight_sum += weight
        
        # 만약, 이전 고기 가격과 같다면
        if max_cost == cost:
            # 지불해야 할 금액을 더함
            total_cost += cost
        
        # 이전 고기 가격과 다르다면
        else:
            # 가격을 갱신
            max_cost = cost
            total_cost = cost
    
    # 목표 무게를 넘겼고, 가격이 같다면 건너뜀
    elif max_cost == cost:
        continue

    # 목표 무게를 넘겼고, 다음 고기를 사는게 더 싸다면
    elif total_cost > cost:
        # 다음 고기를 삼
        total_cost = cost
        break

    else:
        break

# 목표 무게를 달성하지 못했다면 -1, 아니라면 값을 출력
if weight_sum < M:
    print(-1)
else:
    print(total_cost)
```