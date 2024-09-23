# [1943] 동전 분배

### **난이도**
골드 2
## **📝문제**
윤화와 준희는 솔선수범하여 쓰레기를 줍는 착한 일을 하였다. 원장선생님께서는 윤화와 준희를 칭찬하시고 과자나 사 먹으라고 하시며 동전 몇 개를 윤화와 준희에게 건네 주었다.

그런데 돈을 받은 윤화와 준희는 좋아하기보다 고민에 빠지고 말았다. 원장선생님께 받은 이 돈을 어떻게 나누어 할지 고민에 빠진 것이다. 두 사람 모두 상대방이 자기보다 1원이라도 더 받는 것은 도저히 인정할 수 없어 한다. 따라서 돈을 똑같이 둘로 나누어 가져야 두 사람이 모두 만족할 수 있게 된다.

하지만 두 사람에게 돈을 똑같이 나누는 것이 불가능한 경우도 있다. 예를 들어 500원짜리 1개와 50원짜리 1개를 받았다면, 이 돈을 두 사람이 똑같이 나누어 가질 수는 없다. 물론 동전을 반으로 잘라서 나누어 가질 수도 있겠지만 그러면 돈으로서의 가치를 잃기 때문에 그렇게 할 수는 없다.

이제 우리가 할 일은 다음과 같다. 원장 선생님께서 N가지 종류의 동전을 각각 몇 개씩 주셨을 때, 그 돈을 반으로 나눌 수 있는지 없는지 판단하는 것이다.
### **입력**
세 개의 입력이 주어진다. 각 입력의 첫째 줄에 동전의 종류 N(1 ≤ N ≤ 100)이 주어진다. 각 입력의 둘째 줄부터 N+1째 줄까지 각각의 동전의 금액과 개수가 빈 칸을 사이에 두고 주어진다. 단, 원장선생님께서 주신 금액의 총 합은 100,000원을 넘지 않는다. 동전의 금액과 개수는 자연수이고, 같은 금액을 가진 동전이 두 번 이상 주어지는 경우는 없다.
### **출력**
첫째 줄부터 세 줄에 걸쳐, 각 입력에 대하여 반으로 나누는 것이 가능하면 1, 불가능하면 0을 출력한다.
### **예제입출력**

**예제 입력1**

```
2
500 1
50 1
3
100 2
50 1
10 5
3
1 1
2 1
3 1
```

**예제 출력1**

```
0
1
1
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
for testcase in range(3):
    N = int(input())
    coins = [list(map(int, input().split())) for _ in range(N)]  # 동전 정보 입력 받기

    # 총 동전 금액을 계산
    coins_sum = 0
    for coin in coins:
        coins_sum += coin[0] * coin[1]
    
    # 총 금액이 홀수면 두 사람에게 똑같이 나눌 수 없으므로 0을 출력
    if coins_sum % 2 == 1:
        print(0)
        continue
    
    # 목표 금액은 전체 금액의 절반
    target_coin = coins_sum // 2
    
    # DP 배열 선언 (0 ~ target_coin까지)
    dp = [False] * (target_coin + 1)
    dp[0] = True  # 0원을 만드는 것은 항상 가능

    # 각 동전 종류별로 처리 (Bounded Knapsack)
    for V, C in coins:
        total_use = min(C, target_coin // V)
        current_amount = 1
        while total_use > 0:
            used_coins = min(current_amount, total_use)
            total_use -= used_coins
            for idx in range(target_coin, V * used_coins - 1, -1):
                if dp[idx - V * used_coins]:
                    dp[idx] = True
            current_amount *= 2
    
    # 목표 금액(target_coin)을 만들 수 있으면 1, 없으면 0 출력
    if dp[target_coin]:
        print(1)
    else:
        print(0)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|111768|444|PyPy3|1253
#### **📝해설**

**알고리즘**
```
1. DP
2. 배낭 문제
```

### **다른 풀이**

```python
import sys
input = lambda: sys.stdin.readline().rstrip()
INF = 100001

def solve(N, money, total):
	# 돈의 총합이 홀수이면 정확히 반으로 나누는 것은 불가능하다.
	if total % 2:
		return 0

	L = total // 2
	memo = [INF] * (L + 1)

	# 0원은 항상 만들 수 있다.
	memo[0] = 0

	for x in range(1, N + 1):
		cost, amount = money[x]

		for m in range(cost, L + 1):
			if memo[m] < INF:
				memo[m] = 0
				continue

			if memo[m - cost] + 1 <= amount:
				memo[m] = memo[m - cost] + 1

	return 1 if memo[L] < INF else 0

if __name__ == "__main__":
	for _ in range(3):
		N = int(input())
		money, total = [None], 0

		for _ in range(N):
			cost, amount = map(int, input().split())

			money.append((cost, amount))
			total += cost * amount

		print(solve(N, money, total))
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
pcmaster0228|111084|140|PyPy3|796