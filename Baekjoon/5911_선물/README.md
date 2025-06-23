# [5911] 선물

### **난이도**
실버 3
## **📝문제**
시흠이는 군대에 가기 전까지 자신과 놀아준 친구 N(1 ≤ N ≤ 1000)명에게 선물을 주려고 한다. 시흠이는 돈을 B(1 ≤ B ≤ 1,000,000,000)원 가지고 있다.

i번째 친구가 받고 싶어하는 선물의 가격은 P(i)원이고, 배송비는 S(i)원이다. 즉, 시흠이가 i번째 친구에게 선물을 보내려면 돈이 P(i)+S(i)원 필요하다.

시흠이는 물건 가격을 절반으로 할인받을 수 있는 쿠폰을 하나 가지고 있다. 이 쿠폰을 i번째 친구에게 사용한다면, ⌊P(i)/2⌋+S(i)원만 있으면 선물을 보낼 수 있다.

시흠이가 선물을 최대 몇 명에게 보낼 수 있는지 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 N과 B가 주어진다. 둘째 줄부터 N개 줄에는 P(i)와 S(i)가 주어진다. (0 ≤ P(i), S(i) ≤ 1,000,000,000)
### **출력**
첫째 줄에 시흠이가 선물을 최대 몇 명에게 보낼 수 있는지 출력한다.
### **예제입출력**

**예제 입력1**

```
5 24
4 2
2 0
8 1
6 3
12 5
```

**예제 출력1**

```
4
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N, B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

arr.sort(key= lambda x: (sum(x), x[0]))

max_count = 0
for i in range(N):
    coupon_cost = arr[i][0] // 2 + arr[i][1]
    others = sorted(arr[j][0] + arr[j][1] for j in range(N) if j != i)
    
    total, count = coupon_cost, 1
    for cost in others:
        if total + cost > B:
            break
        total += cost
        count += 1

    if total <= B:
        max_count = max(max_count, count)

print(max_count)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|33432|172|Python3|512
#### **📝해설**

**알고리즘**
```
1. 정렬
```

### **다른 풀이**

```python
from sys import stdin
input = stdin.readline

n, b = map(int, input().split())
gifts = [tuple(map(int, input().split())) for _ in range(n)]
gifts.sort(key=lambda x: (x[0]+x[1]))

ans = 0
for i in range(n):
    total = gifts[i][0]//2 + gifts[i][1]
    c = 1 if total<=b else 0
    for j in range(n):
        if j==i:
            continue
        total += gifts[j][0] + gifts[j][1]
        if total<=b:
            c += 1
        else:
            break
    ans = max(ans, c)

print(ans)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
fortunetiger|31120|32|Python3
#### **📝해설**

```python
N, B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

arr.sort(key= lambda x: (sum(x), x[0]))

max_count = 0

# 모든 선물들을 한번씩 쿠폰을 사용해봄
for i in range(N):
    coupon_cost = arr[i][0] // 2 + arr[i][1]

    # 쿠폰을 사용하지 않은 선물들
    others = sorted(arr[j][0] + arr[j][1] for j in range(N) if j != i)
    

    # 최대값을 구함
    total, count = coupon_cost, 1
    for cost in others:
        if total + cost > B:
            break
        total += cost
        count += 1

    if total <= B:
        max_count = max(max_count, count)

print(max_count)
```