# [2629] 양팔저울

### **난이도**
골드 3
## **📝문제**
양팔 저울과 몇 개의 추가 주어졌을 때, 이를 이용하여 입력으로 주어진 구슬의 무게를 확인할 수 있는지를 결정하려고 한다.

무게가 각각 1g과 4g인 두 개의 추가 있을 경우, 주어진 구슬과 1g 추 하나를 양팔 저울의 양쪽에 각각 올려놓아 수평을 이루면 구슬의 무게는 1g이다. 또 다른 구슬이 4g인지를 확인하려면 1g 추 대신 4g 추를 올려놓으면 된다.

구슬이 3g인 경우 아래 <그림 1>과 같이 구슬과 추를 올려놓으면 양팔 저울이 수평을 이루게 된다. 따라서 각각 1g과 4g인 추가 하나씩 있을 경우 주어진 구슬이 3g인지도 확인해 볼 수 있다.

[이미지](https://upload.acmicpc.net/ce5b29f5-9e03-473b-97db-ce9fd740fde2/-/preview/)

<그림 1> 구슬이 3g인지 확인하는 방법 (
$\boxed{1}$은 1g인 추, 
$\boxed{4}$는 4g인 추, ●은 무게를 확인할 구슬)

<그림 2>와 같은 방법을 사용하면 구슬이 5g인지도 확인할 수 있다. 구슬이 2g이면 주어진 추를 가지고는 확인할 수 없다.

추들의 무게와 확인할 구슬들의 무게가 입력되었을 때, 주어진 추만을 사용하여 구슬의 무게를 확인 할 수 있는지를 결정하는 프로그램을 작성하시오.

[이미지](https://upload.acmicpc.net/883fb22a-7516-46e1-937d-2ddc4df94572/-/preview/)

<그림 2> 구슬이 5g인지 확인하는 방법
### **입력**
첫째 줄에는 추의 개수가 자연수로 주어진다. 추의 개수는 30 이하이다. 둘째 줄에는 추의 무게들이 자연수로 가벼운 것부터 차례로 주어진다. 같은 무게의 추가 여러 개 있을 수도 있다. 추의 무게는 500g이하이며, 입력되는 무게들 사이에는 빈칸이 하나씩 있다. 세 번째 줄에는 무게를 확인하고자 하는 구슬들의 개수가 주어진다. 확인할 구슬의 개수는 7이하이다. 네 번째 줄에는 확인하고자 하는 구슬들의 무게가 자연수로 주어지며, 입력되는 무게들 사이에는 빈 칸이 하나씩 있다. 확인하고자 하는 구슬의 무게는 40,000보다 작거나 같은 자연수이다.
### **출력**
주어진 각 구슬의 무게에 대하여 확인이 가능하면 Y, 아니면 N 을 차례로 출력한다. 출력은 한 개의 줄로 이루어지며, 각 구슬에 대한 답 사이에는 빈칸을 하나씩 둔다.
### **예제입출력**

**예제 입력1**

```
2
1 4
2
3 2
```

**예제 출력1**

```
Y N
```

**예제 입력2**

```
4
2 3 3 3
3
1 4 10
```

**예제 출력2**

```
Y Y N
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N = int(input())
weights = list(map(int, input().split()))

sum_weights = sum(weights)

dp = [[False] * (sum_weights + 1) for _ in range(N+1)]
dp[0][0] = True

for i in range(N):
    weight = weights[i]
    for w in range(sum_weights, -1, -1):
        if dp[i][w]:
            dp[i+1][w] = True
            if w + weight <= sum_weights:
                dp[i+1][w+weight] = True
            dp[i+1][abs(w-weight)] = True

result = []
M = int(input())
arr = list(map(int, input().split()))

for number in arr:
    if number <= sum_weights and dp[N][number]:
        result.append("Y")
    else:
        result.append("N")

print(" ".join(map(str, result)))
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|35224|80|Python3|654
#### **📝해설**

**알고리즘**
```
1. DP
2. 배낭문제
```

### **다른 풀이**

```python
n,chu_lst = int(input()),list(map(int,input().split()))
m,check_chu_lst = int(input()),list(map(int,input().split()))

dp = [ 0 ]
for chu in chu_lst:
    tmp=[]
    for i in dp:
        tmp.append(i+chu)
        tmp.append(abs(i-chu))
    dp = list(set((dp + tmp)))

for chu in check_chu_lst:
    print('Y' if chu in dp else 'N',end=' ')
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
ppllaall02|31120|32|Python3|338
#### **📝해설**

```python
N = int(input())
weights = list(map(int, input().split()))

# 무게의 합(최대 무게)를 미리 계산해서 저장
sum_weights = sum(weights)

# DP배열 선언 dp[i][w] == i번쨰 추를 사용헤서 w만큼의 무게를 만들 수 있는지 여부
dp = [[False] * (sum_weights + 1) for _ in range(N+1)]

# 초기 정보
dp[0][0] = True

# 모든 추를 사용해서
for i in range(N):
    weight = weights[i]

    # 무게를 만들 수 있는지 여부를 검사
    for w in range(sum_weights, -1, -1):

        # 이번 무게를 만들 수 있었다면
        if dp[i][w]:
            dp[i+1][w] = True

            # 최대 무게를 넘지 않는다면
            if w + weight <= sum_weights:

                # 이 추를 사용했을 떄 무게를 만들 수 있음
                dp[i+1][w+weight] = True
            # 이 추를 빼는데 사용해서 무게를 만들 수 있음
            dp[i+1][abs(w-weight)] = True

# 결과 저장
result = []
M = int(input())
arr = list(map(int, input().split()))

for number in arr:
    if number <= sum_weights and dp[N][number]:
        result.append("Y")
    else:
        result.append("N")

print(" ".join(map(str, result)))
```