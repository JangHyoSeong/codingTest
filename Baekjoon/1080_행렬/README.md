# [1080] 행렬

### **난이도**
실버 1
## **📝문제**
0과 1로만 이루어진 행렬 A와 행렬 B가 있다. 이때, 행렬 A를 행렬 B로 바꾸는데 필요한 연산의 횟수의 최솟값을 구하는 프로그램을 작성하시오.

행렬을 변환하는 연산은 어떤 3×3크기의 부분 행렬에 있는 모든 원소를 뒤집는 것이다. (0 → 1, 1 → 0)
### **입력**
첫째 줄에 행렬의 크기 N M이 주어진다. N과 M은 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에는 행렬 A가 주어지고, 그 다음줄부터 N개의 줄에는 행렬 B가 주어진다.
### **출력**
첫째 줄에 문제의 정답을 출력한다. 만약 A를 B로 바꿀 수 없다면 -1을 출력한다.
### **예제입출력**

**예제 입력1**

```
3 4
0000
0010
0000
1001
1011
1001
```

**예제 출력1**

```
2
```

**예제 입력2**

```
3 3
111
111
111
000
000
000
```

**예제 출력2**

```
1
```

**예제 입력3**

```
1 1
1
0
```

**예제 출력3**

```
-1
```

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N, M = map(int, input().split())

arr_A = [list(map(int, input())) for _ in range(N)]
arr_B = [list(map(int, input())) for _ in range(N)]


count = 0

for i in range(N-2):
    for j in range(M-2):
        if arr_A[i][j] != arr_B[i][j]:
            count += 1
            for k in range(3):
                for l in range(3):
                    arr_A[i+k][j+l] = (arr_A[i+k][j+l] + 1) % 2
flag = True
for i in range(N):
    for j in range(M):
        if arr_A[i][j] != arr_B[i][j]:
            flag = False
        
        if not flag:
            break
    if not flag:
        break
    
if flag:
    print(count)
else:
    print(-1)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|110460|124|PyPy3|637
#### **📝해설**

**알고리즘**
```
1. 그리디 알고리즘
```

### **다른 풀이**

```python
def reverse(a, b):
    for i in range(a, a+3):
        for j in range(b, b+3):
            A[i][j] = 1 - A[i][j]

n, m = map(int, input().split())
A = [list(map(int, input())) for _ in range(n)]
B = [list(map(int, input())) for _ in range(n)]
cnt = 0

for i in range(n-2):
    for j in range(m-2):
        if A[i][j] != B[i][j]:
            reverse(i, j)
            cnt += 1

if A == B:
    print(cnt)
else:
    print(-1)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
scato2|30616|40|Python3|493
#### **📝해설**

```python
N, M = map(int, input().split())

arr_A = [list(map(int, input())) for _ in range(N)]
arr_B = [list(map(int, input())) for _ in range(N)]


count = 0

# 문제 조건상 항상 9개를 뒤집어야함. 
# 따라서 범위를 벗어나지 않기 위해 마지막 2칸은 순회하지 않음
for i in range(N-2):
    for j in range(M-2):
        # 두 행렬중 다른 곳을 발견하면
        if arr_A[i][j] != arr_B[i][j]:
            # 뒤집는 횟수 추가
            count += 1
            # 현재 칸을 왼쪽 위로 두고, 9칸을 뒤집음
            for k in range(3):
                for l in range(3):
                    arr_A[i+k][j+l] = (arr_A[i+k][j+l] + 1) % 2
                    
# 한 번 순회하면서, 뒤집지 못한 칸이 있다면 뒤집어서 만들 수 없음
# 만들지 못하는 경우라면 flag = False, -1출력
flag = True
for i in range(N):
    for j in range(M):
        if arr_A[i][j] != arr_B[i][j]:
            flag = False
        
        if not flag:
            break
    if not flag:
        break
    
if flag:
    print(count)
else:
    print(-1)
    
'''
같은 곳을 두 번 뒤집는다면 결국 처음 상태로 돌아오기 때문에 그럴 필요가 없음  
따라서 주어진 행렬을 한 번만 순회하면서 숫자가 다른 부분이 나온다면 바로 뒤집음  
'''
```