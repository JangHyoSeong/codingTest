# [5550] 헌책방

### **난이도**
골드 2
## **📝문제**
상근이가 살고있는 도시에는 헌책방이 있다. 데이트 비용을 점점 감당할 수 없게된 상근이는 집에 있는 책을 헌책방에 팔려고 한다. 각 책에는 기준 가격이 정해져있고, 헌책방은 이 가격으로 매입한다.

헌책방은 책을 소설, 만화, 잡지등 10개의 장르로 분류한다. 장르는 1부터 10까지 번호가 매겨져 있다. 이 가게는 같은 장르의 책을 한 번에 매입할 때, 고가로 매입해 준다.

같은 장르의 책을 T권 매입할 때, 책 한 권 당 매입 가격이 기준 가격보다 T-1원 높아진다. 예를 들어, 같은 장르에서 기준 가격이 100원, 120원, 150원인 책을 한 번에 헌책방에 판다면, 매입 가격은 102원, 122원, 152원이 된다.

상근이는 내일 데이트를 가기 위해서 가지고 있는 책 N권 중 K권을 팔려고 한다.

책 N권의 기준 가격과 장르 번호가 주어졌을 때, 총 매입 가격의 최댓값을 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 상근이가 가지고 있는 책의 개수 N과 파려고 하는 책의 수 K가 주어진다. (2 ≤ N ≤ 2000, 1 ≤ K < N)

둘째 줄부터 N개 줄에는 상근이가 가지고 있는 책의 기준 가격 Ci와 장르 Gi가 공백으로 구분되어 주어진다. (1 ≤ Ci ≤ 105, 1 ≤ Gi ≤ 10)
### **출력**
첫째 줄에 총 매입 가격의 최댓값을 출력한다.
### **예제입출력**

**예제 입력1**

```
7 4
14 1
13 2
12 3
14 2
8 2
16 3
11 2
```

**예제 출력1**

```
60
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from collections import defaultdict

N, K = map(int, input().split())
books = [list(map(int, input().split())) for _ in range(N)]

genre_dict = defaultdict(list)

for price, genre in books:
    genre_dict[genre].append(price)

prefix_sums = {}
for genre in genre_dict:
    genre_dict[genre].sort(reverse=True)
    prefix_sums[genre] = [0] * (len(genre_dict[genre]) + 1)
    for i in range(1, len(prefix_sums[genre])):
        prefix_sums[genre][i] = prefix_sums[genre][i-1] + genre_dict[genre][i-1]
    
dp = [0] * (K+1)

for genre, prices in genre_dict.items():
    m = len(prices)
    new_dp =dp[:]
    for t in range(1, min(m, K) + 1):
        total_price = prefix_sums[genre][t] + (t-1) * t
        for j in range(K, t-1, -1):
            new_dp[j] = max(new_dp[j], dp[j-t] + total_price)
    dp = new_dp

print(dp[K])
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|34968|684|Python3|822
#### **📝해설**

**알고리즘**
```
1. DP
2. 누적합
```

### **다른 풀이**

```python
import collections
import sys


def main():
    N, K = [int(x) for x in sys.stdin.readline().split()]
    costs_by_genre = collections.defaultdict(list)
    for _ in range(N):
        C, G = [int(x) for x in sys.stdin.readline().split()]
        costs_by_genre[G].append(C)

    dp_cur = [0] * (K + 1)
    for costs in costs_by_genre.values():
        dp_prev = dp_cur[:]
        cost_sum = 0
        for count, cost in enumerate(sorted(costs, reverse=True), start=1):
            cost_sum += cost
            tot_cost = cost_sum + count * (count - 1)
            for i, dp_cur_i, dp_prev_j in zip(
                range(K + 1), dp_cur, dp_prev[count:]
            ):
                if dp_prev_j + tot_cost > dp_cur_i:
                    dp_cur[i] = dp_prev_j + tot_cost
    print(dp_cur[0])


if __name__ == '__main__':
    main()
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
teferi00|34128|248|Python3|1009
#### **📝해설**

```python
from collections import defaultdict

N, K = map(int, input().split())
books = [list(map(int, input().split())) for _ in range(N)]

# 장르별로 책의 가격을 저장
genre_dict = defaultdict(list)

# 딕셔너리에 값을 입력
for price, genre in books:
    genre_dict[genre].append(price)

# 각 장르별로 내림차순 K개까지 더했을 때 누적합을 구함
prefix_sums = {}

# 모든 장르의 책을 순회하면서
for genre in genre_dict:

    # 책의 가격을 내림차순으로 정렬
    genre_dict[genre].sort(reverse=True)

    # 각 장르별 누적합 배열을 생성
    prefix_sums[genre] = [0] * (len(genre_dict[genre]) + 1)

    # i개 동시 매입했을 때 누적합을 미리 계산
    for i in range(1, len(prefix_sums[genre])):
        prefix_sums[genre][i] = prefix_sums[genre][i-1] + genre_dict[genre][i-1]

# DP 배열 선언 (dp[i] : i개 매입했을 때 최대 가격)
dp = [0] * (K+1)

# 딕셔너리의 모든 값을 순회하면서
for genre, prices in genre_dict.items():

    # 이번에 검사할 장르에서 책의 개수
    m = len(prices)

    # DP 배열 복사
    new_dp =dp[:]

    # 책의 개수, 혹은 최대 매입 개수까지 반복
    for t in range(1, min(m, K) + 1):

        # 총 가격
        total_price = prefix_sums[genre][t] + (t-1) * t

        # DP배열을 거꾸로 순회하면서
        for j in range(K, t-1, -1):

            # 가격을 갱신
            new_dp[j] = max(new_dp[j], dp[j-t] + total_price)

    # dp배열을 새롭게 갱신한 배열로 바꿔줌
    dp = new_dp

print(dp[K])
```