# [11505] 구간 곱 구하기

### **난이도**
골드 1
## **📝문제**
어떤 N개의 수가 주어져 있다. 그런데 중간에 수의 변경이 빈번히 일어나고 그 중간에 어떤 부분의 곱을 구하려 한다. 만약에 1, 2, 3, 4, 5 라는 수가 있고, 3번째 수를 6으로 바꾸고 2번째부터 5번째까지 곱을 구하라고 한다면 240을 출력하면 되는 것이다. 그리고 그 상태에서 다섯 번째 수를 2로 바꾸고 3번째부터 5번째까지 곱을 구하라고 한다면 48이 될 것이다.
### **입력**
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)과 M(1 ≤ M ≤ 10,000), K(1 ≤ K ≤ 10,000) 가 주어진다. M은 수의 변경이 일어나는 횟수이고, K는 구간의 곱을 구하는 횟수이다. 그리고 둘째 줄부터 N+1번째 줄까지 N개의 수가 주어진다. 그리고 N+2번째 줄부터 N+M+K+1 번째 줄까지 세 개의 정수 a,b,c가 주어지는데, a가 1인 경우 b번째 수를 c로 바꾸고 a가 2인 경우에는 b부터 c까지의 곱을 구하여 출력하면 된다.

입력으로 주어지는 모든 수는 0보다 크거나 같고, 1,000,000보다 작거나 같은 정수이다.
### **출력**
첫째 줄부터 K줄에 걸쳐 구한 구간의 곱을 1,000,000,007로 나눈 나머지를 출력한다.
### **예제입출력**

**예제 입력1**

```
5 2 2
1
2
3
4
5
1 3 6
2 2 5
1 5 2
2 3 5
```

**예제 출력1**

```
240
48
```

**예제 입력2**

```
5 2 2
1
2
3
4
5
1 3 0
2 2 5
1 3 6
2 2 5
```

**예제 출력2**

```
0
240
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys

MOD = 1000000007

def build_segment_tree(arr, tree, node, start, end):
    if start == end:
        tree[node] = arr[start]
        return tree[node]
    
    mid = (start + end) // 2
    left_number = build_segment_tree(arr, tree, 2*node, start, mid)
    right_number = build_segment_tree(arr, tree, 2*node + 1, mid+1, end)
    tree[node] = (left_number * right_number) % MOD
    return tree[node]

def update(tree, node, start, end, idx, value):
    if start == end:
        tree[node] = value
        return
    
    mid = (start + end) // 2

    if idx <= mid:
        update(tree, node*2, start, mid, idx, value)
    
    else:
        update(tree, node*2 + 1, mid+1, end, idx, value)
    
    tree[node] = (tree[node*2] * tree[node*2 + 1]) % MOD


def query(tree, node, start, end, left, right):
    if right < start or end < left:
        return 1
    
    if left <= start and end <= right:
        return tree[node]
    
    mid = (start + end) // 2
    left_number = query(tree, node*2, start, mid, left, right)
    right_number = query(tree, node*2 + 1, mid + 1, end, left, right)

    return (left_number * right_number) % MOD
    


N, M, K = map(int, sys.stdin.readline().rstrip().split())
numbers = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

tree = [0] * (4*N)
build_segment_tree(numbers, tree, 1, 0, N-1)

results = []

for _ in range(M + K):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())

    if a == 1:
        update(tree, 1, 0, N-1, b-1, c)

    else:
        results.append(query(tree, 1, 0, N-1, b-1, c-1))

print("\n".join(map(str, results)))
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|153780|516|PyPy3|1606
#### **📝해설**

**알고리즘**
```
1. 세그먼트 트리
```

### **다른 풀이**

```python
import sys
input = sys.stdin.read
data = input().split()
n, m, k = map(int, data[:3])
MOD = 1000000007

p = 0
while 2 ** p < n:
    p += 1

h = [1] * (2 ** (p + 1))

# 입력값 초기화
for i in range(n):
    h[2 ** p + i] = int(data[3 + i])

# 세그먼트 트리 구성
for i in range(2 ** p - 1, 0, -1):
    h[i] = (h[2 * i] * h[2 * i + 1]) % MOD

def summi(start, end):
    summy = 1
    start += 2 ** p
    end += 2 ** p
    while start <= end:
        if start % 2 == 1:
            summy *= h[start]
            summy %= MOD
            start += 1
        if end % 2 == 0:
            summy *= h[end]
            summy %= MOD
            end -= 1
        start //= 2
        end //= 2
    return summy

def change(site, number):
    site += 2 ** p
    h[site] = number
    while site > 1:
        site //= 2
        h[site] = (h[2 * site] * h[2 * site + 1]) % MOD

queries = data[3 + n:]
idx = 0
result = []
for _ in range(m + k):
    a = list(map(int, queries[idx:idx+3]))
    idx += 3
    if a[0] == 1:
        change(a[1] - 1, a[2])
    elif a[0] == 2:
        result.append(summi(a[1] - 1, a[2] - 1))

sys.stdout.write("\n".join(map(str, result)) + "\n")
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
seungmin3737|188232|276|PyPy3|1168
#### **📝해설**

```python
import sys

# 나눌 수
MOD = 1000000007

# 세그먼트 트리 빌드
def build_segment_tree(arr, tree, node, start, end):

    # 리프 노드인 경우
    if start == end:
        # 트리에 값을 채워넣음
        tree[node] = arr[start]
        return tree[node]
    
    # 중간값
    mid = (start + end) // 2

    # 재귀적으로 오른쪽, 왼쪽 서브트리를 빌드
    left_number = build_segment_tree(arr, tree, 2*node, start, mid)
    right_number = build_segment_tree(arr, tree, 2*node + 1, mid+1, end)

    # 현재 노드는 왼쪽, 오른쪽 자식 노드의 곱
    tree[node] = (left_number * right_number) % MOD
    return tree[node]

# 노드의 값을 업데이트하는 함수
def update(tree, node, start, end, idx, value):

    # 리프 노드의 경우 값을 변경
    if start == end:
        tree[node] = value
        return
    
    mid = (start + end) // 2

    # 재귀적으로 바꿔야 할 값을 찾음
    if idx <= mid:
        update(tree, node*2, start, mid, idx, value)
    
    else:
        update(tree, node*2 + 1, mid+1, end, idx, value)
    
    # 노드의 값을 변경
    tree[node] = (tree[node*2] * tree[node*2 + 1]) % MOD


# 구간 곱을 구하는 함수
def query(tree, node, start, end, left, right):

    # 구간이 겹치지 않는 경우
    if right < start or end < left:
        return 1
    
    # 구간이 완전히 포함되는 경우
    if left <= start and end <= right:
        return tree[node]
    
    # 재귀적으로 값을 찾음
    mid = (start + end) // 2
    left_number = query(tree, node*2, start, mid, left, right)
    right_number = query(tree, node*2 + 1, mid + 1, end, left, right)

    return (left_number * right_number) % MOD
    


N, M, K = map(int, sys.stdin.readline().rstrip().split())
numbers = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

# 세그먼트 트리로 사용할 리스트
tree = [0] * (4*N)

# 트리 빌드
build_segment_tree(numbers, tree, 1, 0, N-1)

# 결과 출력을 위한 리스트
results = []

for _ in range(M + K):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())

    # 트리를 업데이트
    if a == 1:
        update(tree, 1, 0, N-1, b-1, c)

    # 구간 곱을 저장
    else:
        results.append(query(tree, 1, 0, N-1, b-1, c-1))

print("\n".join(map(str, results)))
```