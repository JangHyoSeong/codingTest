# [28099] 이상한 배열

### **난이도**
골드 3
## **📝문제**
길이가 $N$인 배열 $A$가 주어진다. 배열 $A$가 아래 조건을 만족한다면 이 배열 $A$를 이상한 배열이라 한다.
- $A_i=A_j$를 만족하는 정수 $1 \le i,j \le N$와 $i < k < j$를 만족하는 정수 $k$에 대해, 항상 $A_k \le A_i$을 만족한다.   
배열 $A$가 주어질 때 $A$가 이상한 배열인지 확인하여라.
### **입력**
첫 번째 줄에 테스트케이스의 수 $T$가 주어진다. ($1\le T\le 200\ 000$)

각 테스트케이스에 대해, 첫 번째 줄에 배열의 길이 $N$이 주어진다. ($1\leq N\leq 200\, 000$)

두 번째 줄에는 배열의 원소를 나타내는 $N$개의 정수 $A_1,A_2,\ldots,A_N$이 공백으로 구분되어 주어진다. ($1\leq A_i\leq N$)

모든 테스트케이스에 대해 $N$의 합이 $200\, 000$ 이하임이 보장된다.
### **출력**
각 테스트케이스에 대해 주어진 배열이 이상한 배열이면 Yes, 아니라면 No를 출력한다.
### **예제입출력**

**예제 입력1**

```
6
3
1 2 3
5
1 1 2 2 3
6
1 2 3 1 2 3
9
6 3 2 3 6 4 1 4 6
7
4 3 2 3 1 3 4
9
6 3 1 3 6 4 1 4 6
```

**예제 출력1**

```
Yes
Yes
No
Yes
Yes
No
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys

def build(arr, tree, node, start, end):
    if start == end:
        tree[node] = arr[start]

    else:
        mid = (start + end) // 2
        left_child = node * 2 + 1
        right_child = node * 2 + 2

        build(arr, tree, left_child, start, mid)
        build(arr, tree, right_child, mid + 1, end)
        tree[node] = max(tree[left_child], tree[right_child])

def query(tree, node, start, end, left, right):
    if right < start or end < left:
        return 0
    
    if left <= start and end <= right:
        return tree[node]
    
    mid = (start + end) // 2
    left_max = query(tree, node * 2 + 1, start, mid , left, right)
    right_max = query(tree, node * 2 + 2, mid + 1, end, left, right)
    return max(left_max, right_max)


def is_valid(N, arr):
    first_index = {}
    last_index = {}

    for i in range(N):
        if arr[i] not in first_index:
            first_index[arr[i]] = i
        last_index[arr[i]] = i
    
    tree = [0] * (4 * N)
    build(arr, tree, 0, 0, N - 1)

    for num in first_index:
        left, right = first_index[num], last_index[num]
        max_in_range = query(tree, 0, 0, N-1, left, right)
        if max_in_range > num:
            return "No"
    return "Yes"

T = int(sys.stdin.readline().rstrip())

for testcase in range(T):
    N = int(sys.stdin.readline().rstrip())
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    print(is_valid(N, arr))
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|172572|740|PyPy3|1435
#### **📝해설**

**알고리즘**
```
1. 세그먼트 트리
```

### **다른 풀이**

```python
import sys


def main() -> None:
    rd = sys.stdin.readline
    for _ in range(int(rd())):
        n = int(rd())
        a = list(map(int, rd().split()))
        lp = [0] * (n+1)
        for i, ai in enumerate(reversed(a)):
            lp[ai] = n-1-i
        rp = [0] * (n+1)
        for i, ai in enumerate(a):
            rp[ai] = i

        stk = []
        for i, ai in enumerate(a):
            if stk and stk[-1] < ai:
                print("No")
                break
            if i == lp[ai]:
                stk.append(ai)
            if i == rp[ai]:
                if not stk or stk[-1] != ai:
                    print("No")
                    break
                stk.pop()
        else:
            print("Yes")


if __name__ == "__main__":
    main()
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
zenith82114|155148|196|PyPy3|770
#### **📝해설**

```python
import sys

# 세그먼트 트리 빌드
def build(arr, tree, node, start, end):

    # 리프노드까지 다핬다면 노드를 작성
    if start == end:
        tree[node] = arr[start]

    # 리프노드가 아니라면
    else:
        # 왼쪽 오른쪽 노드로 나누어 재귀호출
        mid = (start + end) // 2
        left_child = node * 2 + 1
        right_child = node * 2 + 2

        build(arr, tree, left_child, start, mid)
        build(arr, tree, right_child, mid + 1, end)
        
        # 자식 노드 중 최대값을 저장
        tree[node] = max(tree[left_child], tree[right_child])

# 주어진 구간 중 최대값을 구하는 쿼리 함수
def query(tree, node, start, end, left, right):

    # 구간이 올바르게 주어지지 않았다면 0 리턴
    if right < start or end < left:
        return 0
    
    # 리프노드라면 그 값을 리턴
    if left <= start and end <= right:
        return tree[node]
    
    # 좌 우를 나누어 최대값을 구함
    mid = (start + end) // 2
    left_max = query(tree, node * 2 + 1, start, mid , left, right)
    right_max = query(tree, node * 2 + 2, mid + 1, end, left, right)
    return max(left_max, right_max)

# 이상한 배열인지 검사하는 함수
def is_valid(N, arr):

    # 각 숫자가 처음 나온 인덱스, 마지막으로 나온 인덱스를 저장할 딕셔너리
    first_index = {}
    last_index = {}

    # 숫자의 인덱스를 저장
    for i in range(N):
        if arr[i] not in first_index:
            first_index[arr[i]] = i
        last_index[arr[i]] = i
    
    # 세그먼트 트리를 위한 배열 선언
    tree = [0] * (4 * N)
    build(arr, tree, 0, 0, N - 1)

    # 모든 숫자를 순회하면서
    for num in first_index:

        # 그 숫자가 나왔을 때, 이상한 배열을 만족하는지 확인
        left, right = first_index[num], last_index[num]
        max_in_range = query(tree, 0, 0, N-1, left, right)
        if max_in_range > num:
            return "No"
    return "Yes"

T = int(sys.stdin.readline().rstrip())

for testcase in range(T):
    N = int(sys.stdin.readline().rstrip())
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    print(is_valid(N, arr))
```