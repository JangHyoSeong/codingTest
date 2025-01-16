# [19645] 햄최몇?

### **난이도**
골드 1
## **📝문제**
세 모질이들 관우, 철환, 길원이가 모였다. 모질이들은 모이면 서로 '햄버거 최대 몇 개 드실 수 있나요?'의 준말인 '햄최몇?'을 시전하며 자랑을 하기 바쁘다.

막내 길원이는 문득 중요한 사실을 깨달았다. 바로, 개수가 중요한 것이 아니라 최대 효용이 중요하다는 것이었다! 이들은 바로 N개의 햄버거를 준비했다. 그리고 이 햄버거를 사이좋게 나누어 먹었다. 각 모질이들이 얻을 수 있는 효용은 이들이 먹은 햄버거들의 효용의 합이다. 또한 나름의 서열과 규칙이 있어, 존경하는 선배님들보다는 높은 효용을 누려서는 안 된다.

막내 길원이는 선배님들을 존경하기 때문에 규칙을 따라야 하는 한편, 햄버거를 잘 분배하여 본인이 얻을 수 있는 효용이 최대가 되도록 하고 싶다.
### **입력**
첫 번째 줄에 N (1 ≤ N ≤ 50)이 주어진다. N은 햄버거의 수이다.

두 번째 줄에 N개의 양의 정수 ai (1 ≤ ai ≤ 50)가 공백으로 구분되어 주어진다. 각각의 값은 햄버거의 효용을 의미한다.
### **출력**
세 모질이 중 막내 길원이가 얻을 수 있는 효용의 합의 최댓값을 출력한다.
### **예제입출력**

**예제 입력1**

```
10
4 37 50 2 6 15 2 13 3 10
```

**예제 출력1**

```
46
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N = int(input())
burgers = list(map(int, input().split()))

sum_burgers = sum(burgers)
dp = [[False] * (sum_burgers + 1) for _ in range(sum_burgers + 1)]
dp[0][0] = True

current_sum = 0
max_util = 0

for burger in burgers:
    current_sum += burger
    for i in range(current_sum, -1, -1):
        for j in range(current_sum, -1, -1):
            if dp[i][j]:
                dp[i+burger][j] = True
                dp[i][j+burger] = 1

for i in range(sum_burgers + 1):
    for j in range(sum_burgers + 1):
        if not dp[i][j]:
            continue

        k = sum_burgers - (i+j)
        min_util = min(k, i, j)
        max_util = max(max_util, min_util)

print(max_util)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|159732|640|PyPy3|677
#### **📝해설**

**알고리즘**
```
1. 배낭 문제
2. DP
```

### **다른 풀이**

```python
N = int(input())

burger = list(map(int, input().split()))
size = 1000

d = [[-1 for _ in range(size)] for _ in range(size)]

init = burger.pop(0)

d[0][init] = 0
d[init][0] = 0
d[0][0] = init

for now in burger:
    for i in range(size-1, -1, -1):
        for j in range(size-1, -1, -1):
            if d[i][j] == -1:
                continue
            
            if i + now < size:
                d[i + now][j] = d[i][j]
            if j + now < size:
                d[i][j + now] = d[i][j]
            
            d[i][j] += now

ans = 0
for i in range(size):
    for j in range(size):
        if d[i][j] > -1:
            ans = max(ans, min([i, j, d[i][j]]))
print(ans)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
seonjong|123084|572|PyPy3|681
#### **📝해설**

```python
N = int(input())
burgers = list(map(int, input().split()))

# 버거의 효용의 총합
sum_burgers = sum(burgers)

# 선배 1, 2가 i, j의 효용만큼 버거를 먹었을 때, 가능한 조합인지 여부를 저장(Boolean)
dp = [[False] * (sum_burgers + 1) for _ in range(sum_burgers + 1)]

# 0, 0은 가능
dp[0][0] = True

# 현재까지 고려한 햄버거 호용의 합
current_sum = 0

# 최대 효용
max_util = 0

# 모든 햄버거를 탐색하면서
for burger in burgers:

    # 지금까지의 햄버거 호용을 더함
    current_sum += burger

    # 지금까지의 효용을 역순으로 검사하면서
    for i in range(current_sum, -1, -1):
        for j in range(current_sum, -1, -1):

            # 만약 가능한 조합이라면
            if dp[i][j]:

                # 이 상태에서 햄버거를 먹는 것도 가능
                dp[i+burger][j] = True
                dp[i][j+burger] =  True

# 모든 효용을 검사한 후
for i in range(sum_burgers + 1):
    for j in range(sum_burgers + 1):

        # 가능하지 않은 케이스는 건너뜀
        if not dp[i][j]:
            continue
        
        # 가능한 케이스라면, 막내의 효용을 구함
        k = sum_burgers - (i+j)
        min_util = min(k, i, j)

        # 최대값을 갱신
        max_util = max(max_util, min_util)

print(max_util)
```

### **🔖정리**

1. DP를 Boolean으로 하는 경우도 있다