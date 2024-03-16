# [15650] N과 M(2)

### **난이도**
실버 3
## **📝문제**
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

- 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
- 고른 수열은 오름차순이어야 한다.
### **입력**
첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)
### **출력**
한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.
### **예제입출력**

**예제 입력1**

```
3 1
```

**예제 출력1**

```
1
2
3
```

**예제 입력2**

```
4 2
```

**예제 출력2**

```
1 2
1 3
1 4
2 3
2 4
3 4
```

**예제 입력3**

```
4 4
```

**예제 출력3**

```
1 2 3 4
```

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
def permutation(i, M, N, arr):
    arr = arr[:]

    if M == 0:
        for num in arr:
            print(num, end= ' ')
        print()
        return
    
    for j in range(i+1, N+1):
        if N-j < M-1:
            return
        permutation(j, M-1, N, arr + [j])
        

N, M = map(int, input().split())

permutation(0, M, N, [])
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|108080|108|PyPy3|338
#### **📝해설**

**알고리즘**
```
1. 백트래킹
```

### **다른 풀이**

```python
from itertools import combinations
n, m = map(int, input().split())
for i in combinations([i for i in range(1, n + 1)], m):
    print(*i)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
정답|30616|32|Python3|138
#### **📝해설**

```python
from itertools import combinations
n, m = map(int, input().split())
# 중복을 허용하지 않고 오름차순으로 정렬하기 때문에 조합과 같다
for i in combinations([i for i in range(1, n + 1)], m):
    print(*i)
```