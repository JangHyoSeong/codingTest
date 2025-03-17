# [2357] 최솟값과 최댓값

### **난이도**
골드 1
## **📝문제**
N(1 ≤ N ≤ 100,000)개의 정수들이 있을 때, a번째 정수부터 b번째 정수까지 중에서 제일 작은 정수, 또는 제일 큰 정수를 찾는 것은 어려운 일이 아니다. 하지만 이와 같은 a, b의 쌍이 M(1 ≤ M ≤ 100,000)개 주어졌을 때는 어려운 문제가 된다. 이 문제를 해결해 보자.

여기서 a번째라는 것은 입력되는 순서로 a번째라는 이야기이다. 예를 들어 a=1, b=3이라면 입력된 순서대로 1번, 2번, 3번 정수 중에서 최소, 최댓값을 찾아야 한다. 각각의 정수들은 1이상 1,000,000,000이하의 값을 갖는다.
### **입력**
첫째 줄에 N, M이 주어진다. 다음 N개의 줄에는 N개의 정수가 주어진다. 다음 M개의 줄에는 a, b의 쌍이 주어진다.
### **출력**
M개의 줄에 입력받은 순서대로 각 a, b에 대한 답을 최솟값, 최댓값 순서로 출력한다.
### **예제입출력**

**예제 입력1**

```
10 4
75
30
100
38
50
51
52
20
81
5
1 10
3 5
6 9
8 10
```

**예제 출력1**

```
5 100
38 100
20 81
5 81
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys

def build_segment_tree(arr: list, tree: list, node: int, start: int, end: int, type: str):
    if start == end:
        tree[node] = arr[start]
    
    else:
        mid = (start + end) // 2
        build_segment_tree(arr, tree, 2*node + 1, start, mid, type)
        build_segment_tree(arr, tree, 2*node + 2, mid+1, end, type)
        
        if type == "max":
            tree[node] = max(tree[2*node + 1], tree[2*node + 2])
        elif type == "min":
            tree[node] = min(tree[2*node + 1], tree[2*node + 2])

def query_segment_tree(tree: list, node: int, start: int, end: int, left: int, right: int, type: str):
    if right < start or end < left:
        if type == "min":
            return int(21e8)
        elif type == "max":
            return 0
    
    if left <= start and end <= right:
        return tree[node]
    
    mid = (start + end) // 2
    left_result = query_segment_tree(tree, 2*node + 1, start, mid, left, right, type)
    right_result = query_segment_tree(tree, 2*node + 2, mid + 1, end, left, right, type)
    
    if type == "max":
        return max(left_result, right_result)
    elif type == "min":
        return min(left_result, right_result)

N, M = map(int, sys.stdin.readline().rstrip().split())
arr = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

min_tree = [0] * (4*N)
max_tree = [0] * (4*N)

build_segment_tree(arr, min_tree, 0, 0, N-1, "min")
build_segment_tree(arr, max_tree, 0, 0, N-1, "max")

for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    min_result = query_segment_tree(min_tree, 0, 0, N-1, a-1, b-1, "min")
    max_result = query_segment_tree(max_tree, 0, 0, N-1, a-1, b-1, "max")
    print(min_result, max_result)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|148828|1260|PyPy3|1728
#### **📝해설**

**알고리즘**
```
1. 세그먼트 트리
```

### **다른 풀이**

```python
import sys
input = sys.stdin.buffer.read

def main():
	arr = list(map(int, input().split()))
	N, M = arr[0], arr[1]
	seg_min = [0] * N + arr[2: N + 2]
	seg_max = seg_min[:]
	ans = []

	for i in range(N - 1, 0, -1):
		seg_min[i] = min(seg_min[i << 1], seg_min[i << 1 | 1])
		seg_max[i] = max(seg_max[i << 1], seg_max[i << 1 | 1])

	for i in range(N + 2, N + 2 + 2 * M, 2):
		_min, _max = 10 ** 9, 1
		l, r = arr[i] + N - 1, arr[i + 1] + N
		while l < r:
			if l & 1:
				_min = min(_min, seg_min[l])
				_max = max(_max, seg_max[l])
				l += 1
			if r & 1:
				r -= 1
				_min = min(_min, seg_min[r])
				_max = max(_max, seg_max[r])
			l >>= 1
			r >>= 1
		ans.append(f'{_min} {_max}')

	print('\n'.join(ans))

main()
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
rkaxhdals|166544|304|PyPy3|718
#### **📝해설**

```python
import sys

# 세그먼트 트리 빌드
def build_segment_tree(arr: list, tree: list, node: int, start: int, end: int, type: str):

    # 리프노드까지 내려갔다면 리프노드 작성
    if start == end:
        tree[node] = arr[start]
    
    # 리프노드가 아니라면
    else:
        # 자식 노드로 이동
        mid = (start + end) // 2
        build_segment_tree(arr, tree, 2*node + 1, start, mid, type)
        build_segment_tree(arr, tree, 2*node + 2, mid+1, end, type)
        
        # 최대값, 최소값을 구분
        if type == "max":
            tree[node] = max(tree[2*node + 1], tree[2*node + 2])
        elif type == "min":
            tree[node] = min(tree[2*node + 1], tree[2*node + 2])

# 세그먼트 트리의 쿼리를 작성하는 함수
def query_segment_tree(tree: list, node: int, start: int, end: int, left: int, right: int, type: str):

    # 리프노드가 주어진 값을 벗어난다면
    if right < start or end < left:

        # 각각 최소, 최대일 경우 영향을 미치지 않을 값으로 리턴
        if type == "min":
            return int(21e8)
        elif type == "max":
            return 0
    
    # 리프노드라면 그 값을 리턴
    if left <= start and end <= right:
        return tree[node]
    
    # 좌우로 나누어서 최대, 최소값을 찾음
    mid = (start + end) // 2
    left_result = query_segment_tree(tree, 2*node + 1, start, mid, left, right, type)
    right_result = query_segment_tree(tree, 2*node + 2, mid + 1, end, left, right, type)
    
    # 최대, 최소 구분
    if type == "max":
        return max(left_result, right_result)
    elif type == "min":
        return min(left_result, right_result)

# 입력받기
N, M = map(int, sys.stdin.readline().rstrip().split())
arr = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

# 최대, 최소값을 위한 세그먼트 트리를 각각 작성
min_tree = [0] * (4*N)
max_tree = [0] * (4*N)

build_segment_tree(arr, min_tree, 0, 0, N-1, "min")
build_segment_tree(arr, max_tree, 0, 0, N-1, "max")

# 최대값, 최소값을 구함
for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    min_result = query_segment_tree(min_tree, 0, 0, N-1, a-1, b-1, "min")
    max_result = query_segment_tree(max_tree, 0, 0, N-1, a-1, b-1, "max")
    print(min_result, max_result)
```