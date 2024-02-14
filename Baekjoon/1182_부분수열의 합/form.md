# [1182] 부분수열의 합

### **난이도**
실버 2


## **📝문제**
N개의 정수로 이루어진 수열이 있을 때, 크기가 양수인 부분수열 중에서 그 수열의 원소를 다 더한 값이 S가 되는 경우의 수를 구하는 프로그램을 작성하시오.

### **입력**
첫째 줄에 정수의 개수를 나타내는 N과 정수 S가 주어진다. (1 ≤ N ≤ 20, |S| ≤ 1,000,000) 둘째 줄에 N개의 정수가 빈 칸을 사이에 두고 주어진다. 주어지는 정수의 절댓값은 100,000을 넘지 않는다.

### **출력**
첫째 줄에 합이 S가 되는 부분수열의 개수를 출력한다.

### **예제입출력**

**예제 입력1**

```
5 0
-7 -3 -2 5 8
```

**예제 출력1**

```
1
```


## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
count = 0

def f(i, N, S):
    global count

    if i == N:
        subset_sum = 0
        for j in range(N):
            if bit[j]:
                subset_sum += numbers[j]

        if subset_sum == S:
            count += 1

    else:
        for j in range(1, -1, -1):
            bit[i] = j
            f(i+1, N, S)


N, S = map(int, input().split())

numbers = list(map(int, input().split()))
bit = [0] * N

f(0, N, S)
if S == 0:
    count -= 1

print(count)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|123996|592|PyPy3|463
#### **📝해설**

**알고리즘**
```
1. 재귀함수
2. 백트래킹
```

#### **😅개선점**

1. 조건을 만족하지 못했을 때 종료하지 못해서 실행시간과 메모리를 많이 쓴다
2. 재귀함수를 사용하기 때문에 N이 커진다면 스택오버플로우가 생길 수 있다.


### **다른 풀이**

```python
N, S = map(int, input().split())
sequence = list(map(int, input().split()))

# MITM
def dfs(sector, array, depth, value):
    if depth == len(array):
        sector.append(value)
        return sector
    
    # not select
    sector = dfs(sector, array, depth+1, value)

    # select
    sector = dfs(sector, array, depth+1, value+array[depth])

    return sector

# binary_search
def binary_search(array, find_value):
    global count

    s = 0
    e = len(array)-1

    pivot = (s+e) // 2
    while s <= e:
        pivot = (s+e) // 2
        if array[pivot] <= find_value:
            s = pivot + 1
        elif array[pivot] > find_value:
            e = pivot - 1
    up = e # 탐색 값의 상한

    if array[e] != find_value: return

    s = 0
    e = len(array)-1

    pivot = (s+e) // 2
    while s <= e:
        pivot = (s+e) // 2
        if array[pivot] < find_value:
            s = pivot + 1
        elif array[pivot] >= find_value:
            e = pivot - 1
    down = s # 탐색 값의 하한

    count += up - down + 1

w1 = sequence[:(N//2)]
w2 = sequence[(N//2):]

left = dfs([], w1, 0, 0)
right = sorted(dfs([], w2, 0, 0))

count = 0 
# left에서 0을 선택하면, right에서 0을 찾는 경우 1가지를 미리 제외
if S == 0: count -= 1

for i in range(len(left)): 
    binary_search(right, S-left[i])

print(count)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
ckstlr1730|31120|44|Python3|1345
#### **📝해설**

```
모르겠습니다.. 더공부하겠습니다..
```