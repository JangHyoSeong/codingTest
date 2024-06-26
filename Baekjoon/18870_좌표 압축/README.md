# [18870] 좌표 압축

### **난이도**
실버 2
## **📝문제**
수직선 위에 N개의 좌표 X1, X2, ..., XN이 있다. 이 좌표에 좌표 압축을 적용하려고 한다.

Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표 Xj의 개수와 같아야 한다.

X1, X2, ..., XN에 좌표 압축을 적용한 결과 X'1, X'2, ..., X'N를 출력해보자.
### **입력**
첫째 줄에 N이 주어진다.

둘째 줄에는 공백 한 칸으로 구분된 X1, X2, ..., XN이 주어진다.
### **출력**
첫째 줄에 X'1, X'2, ..., X'N을 공백 한 칸으로 구분해서 출력한다.
### **예제입출력**

**예제 입력1**

```
5
2 4 -10 4 -9
```

**예제 출력1**

```
2 3 0 3 1
```

**예제 입력2**

```
6
1000 999 1000 999 1000 999
```

**예제 출력2**

```
1 0 1 0 1 0
```

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N = int(input())
arr = list(map(int, input().split()))
sorted_arr = sorted(arr)
idx = 0

index_dict = {
    sorted_arr[0] : 0
}

for i in range(1, N):
    if sorted_arr[i] != sorted_arr[i-1]:
        idx += 1
        index_dict[sorted_arr[i]] = idx

for i in range(N):
    print(index_dict[arr[i]], end=" ")
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|144340|2072|Python3|307
#### **📝해설**

**알고리즘**
```
1. 정렬
```

### **다른 풀이**

```python
import sys
stdin = sys.stdin.buffer

stdin.readline()
arr = list(map(int, stdin.read().split()))
dic = {x: i for i, x in enumerate(sorted(set(arr)))}
print(' '.join(map(str, [dic[x] for x in arr])))
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
rkaxhdals|315776|712|PyPy3|199
#### **📝해설**

```python
N = int(input())
arr = list(map(int, input().split()))

# 입력받은 배열을 정렬한 배열을 새로 만듦
sorted_arr = sorted(arr)

# 좌표 압축을 위한 인덱스
idx = 0

# 좌표 압축한 인덱스 정보를 저장할 딕셔너리
index_dict = {
    sorted_arr[0] : 0
}

# 두번째 값부터 순회하며
for i in range(1, N):
    # 앞의 값과 다르다면 인덱스를 증가 후 딕셔너리에 정보 저장
    if sorted_arr[i] != sorted_arr[i-1]:
        idx += 1
        index_dict[sorted_arr[i]] = idx

# 배열을 순회하며 압축 좌표를 출력
for i in range(N):
    print(index_dict[arr[i]], end=" ")
```