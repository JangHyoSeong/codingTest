# [11728] 배열 합치기

### **난이도**
실버 5
## **📝문제**
정렬되어있는 두 배열 A와 B가 주어진다. 두 배열을 합친 다음 정렬해서 출력하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 배열 A의 크기 N, 배열 B의 크기 M이 주어진다. (1 ≤ N, M ≤ 1,000,000)

둘째 줄에는 배열 A의 내용이, 셋째 줄에는 배열 B의 내용이 주어진다. 배열에 들어있는 수는 절댓값이 109보다 작거나 같은 정수이다.
### **출력**
첫째 줄에 두 배열을 합친 후 정렬한 결과를 출력한다.
### **예제입출력**

**예제 입력1**

```
2 2
3 5
2 9
```

**예제 출력1**

```
2 3 5 9
```

**예제 입력2**

```
2 1
4 7
1
```

**예제 출력2**

```
1 4 7
```

**예제 입력3**

```
4 3
2 3 5 9
1 4 7
```

**예제 출력3**

```
1 2 3 4 5 7 9
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
A = list(map(int, sys.stdin.readline().rstrip().split()))
B = list(map(int, sys.stdin.readline().rstrip().split()))

A_idx, B_idx = 0, 0

new_arr = [None] * (N + M)
for i in range(N + M):

    if A_idx >= N:
        new_arr[i] = B[B_idx]
        B_idx += 1
    
    elif B_idx >= M:
        new_arr[i] = A[A_idx]
        A_idx += 1

    else:
        if A[A_idx] < B[B_idx]:
            new_arr[i] = A[A_idx]
            A_idx += 1
        else:
            new_arr[i] = B[B_idx]
            B_idx += 1

print(" ".join(map(str, new_arr)))
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|337516|792|PyPy3|605
#### **📝해설**

**알고리즘**
```
1. 투 포인터
```

### **다른 풀이**

```python
import sys
NM = sys.stdin.readline()
print(" ".join(sorted(sys.stdin.read().split(), key=int)))
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
liminicr|285352|616|Python3|95
#### **📝해설**

```python
import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
A = list(map(int, sys.stdin.readline().rstrip().split()))
B = list(map(int, sys.stdin.readline().rstrip().split()))

# 두 배열의 인덱스
A_idx, B_idx = 0, 0

# 새롭게 정렬된 배열을 저장할 리스트
new_arr = [None] * (N + M)

# 리스트를 전부 채울 때까지 반복
for i in range(N + M):

    # 이미 A배열의 수를 모두 검사했다면, B배열로만 채움
    if A_idx >= N:
        new_arr[i] = B[B_idx]
        B_idx += 1
    
    # B배열도 똑같이 작업
    elif B_idx >= M:
        new_arr[i] = A[A_idx]
        A_idx += 1

    # 아직 A, B배열의 숫자가 남았다면
    else:

        # 더 작은수를 배열에 삽입
        if A[A_idx] < B[B_idx]:
            new_arr[i] = A[A_idx]
            # 삽입한 배열의 인덱스를 증가
            A_idx += 1
        else:
            new_arr[i] = B[B_idx]
            B_idx += 1

print(" ".join(map(str, new_arr)))
```