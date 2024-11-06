# [24508] 나도리팡

### **난이도**
골드 5
## **📝문제**
나도리는 귀여운 노란색 공 모양 캐릭터이다. 나도리는 바구니에 들어가 있는 것을 좋아한다.

하지만 나도리에게는 최근 슬픈 일이 생겼다. 왜냐하면 나도리 
$K$ 마리가 한 바구니에 모인다면 빡! 하고 터져버리는 무서운 저주에 걸렸기 때문이다.

현재 
$N$ 개의 바구니가 있고, 
$i$ 번째 바구니에는 나도리가 
$A_i$ 마리 담겨 있다. 프즈슈와는 나도리를 괴롭히는 것을 좋아하기 때문에, 한 바구니에 있는 나도리 한 마리를 다른 바구니로 옮기는 행동을 최대 
$T$ 회 반복하여 모든 나도리들을 터트릴 수 있는지 알고 싶다. 바구니의 개수가 많아 쉽사리 계산하지 못 하고 있는 그를 위해 대신 답을 구해서 알려주자.

### **입력**
첫 번째 줄에는 정수 
$N$, 
$K$, 
$T$ 가 공백을 사이에 두고 주어진다. (
$2 \le N, K \le 10^5$, 
$0 \le T \le 10^9$)

두 번째 줄에는 정수 
$A_1, A_2, \cdots, A_N$ 이 공백을 사이에 두고 주어진다. (
$0 \le A_1, A_2, \cdots, A_N \lt K$)
### **출력**
$T$ 회 이하로 나도리를 옮겨 모두 터트리는 것이 가능하다면 YES를, 불가능하다면 NO 를 첫째 줄에 출력한다.
### **예제입출력**

**예제 입력1**

```
2 2 1
1 1
```

**예제 출력1**

```
YES
```

**예제 입력2**

```
3 5 2
1 2 2
```

**예제 출력2**

```
NO
```

**예제 입력3**

```
3 5 3
1 2 2
```

**예제 출력3**

```
YES
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N, K, T = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
sum_arr = sum(arr)
if sum_arr % K:
    print('NO')
    exit()

count = 0

for i in range(sum_arr//K):
    count += K - arr[N-1-i]

if count > T:
    print('NO')
else:
    print('YES')
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|122264|128|PyPy3|269
#### **📝해설**

**알고리즘**
```
1. 그리디 알고리즘
```

### **다른 풀이**

```python
[n, k, t] = list(map(int, input().split()))
arr = list(reversed(sorted(list(map(int, input().split())))))
sm = 0
accumulating_to = 0
total_sum = sum(arr)
if total_sum % k != 0:
    print("NO")
else:
    for i in range(int(total_sum / k)):
        sm += k - arr[i]
    if sm <= t:
        print("YES")
    else:
        print("NO")
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
a1benjamin|42036|88|Python3|330
#### **📝해설**

```python
N, K, T = map(int, input().split())
arr = list(map(int, input().split()))

# 일단 배열을 정렬
arr.sort()

# 합을 구함
sum_arr = sum(arr)

# 합이 K로 나누어 떨어지지 않는다면 애초에 불가능
if sum_arr % K:
    print('NO')
    exit()

# 이동 횟수
count = 0

# K개 바구니를 sum_arr//K개 만큼 만들 수 있음. 그만큼 반복
for i in range(sum_arr//K):

    # 가장 큰 바구니부터 개수를 채워줌
    count += K - arr[N-1-i]

# 출력
if count > T:
    print('NO')
else:
    print('YES')
```