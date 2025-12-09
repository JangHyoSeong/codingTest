# [14426] 접두사 찾기

### **난이도**
실버 1
## **📝문제**
문자열 S의 접두사란 S의 가장 앞에서부터 부분 문자열을 의미한다. 예를 들어, S = "codeplus"의 접두사는 "code", "co", "codepl", "codeplus"가 있고, "plus", "s", "cude", "crud"는 접두사가 아니다.

총 N개의 문자열로 이루어진 집합 S가 주어진다.

입력으로 주어지는 M개의 문자열 중에서 집합 S에 포함되어 있는 문자열 중 적어도 하나의 접두사인 것의 개수를 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 문자열의 개수 N과 M (1 ≤ N ≤ 10,000, 1 ≤ M ≤ 10,000)이 주어진다.

다음 N개의 줄에는 집합 S에 포함되어 있는 문자열이 주어진다.

다음 M개의 줄에는 검사해야 하는 문자열이 주어진다.

입력으로 주어지는 문자열은 알파벳 소문자로만 이루어져 있으며, 길이는 500을 넘지 않는다. 집합 S에 같은 문자열이 여러 번 주어지는 경우는 없다.
### **출력**
첫째 줄에 M개의 문자열 중에 총 몇 개가 포함되어 있는 문자열 중 적어도 하나의 접두사인지 출력한다.
### **예제입출력**

**예제 입력1**

```
5 10
baekjoononlinejudge
startlink
codeplus
sundaycoding
codingsh
baekjoon
star
start
code
sunday
coding
cod
online
judge
plus
```

**예제 출력1**

```
7
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys
from bisect import bisect_left

N, M = map(int, sys.stdin.readline().rstrip().split())
arr = sorted(sys.stdin.readline().rstrip() for _ in range(N))

answer = 0
for _ in range(M):
    query = sys.stdin.readline().rstrip()
    idx = bisect_left(arr, query)

    if idx < N and arr[idx].startswith(query):
        answer += 1

print(answer)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|39072|92|Python3|349
#### **📝해설**

**알고리즘**
```
1. 이진 탐색
```

### **다른 풀이**

```python
def main():
    import io
    import os
    from bisect import bisect_left

    input = io.BufferedReader(io.FileIO(0), 1 << 17).readline
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    S.sort()
    k = 0
    for _ in range(M):
        Q = input()[:-1]
        i = bisect_left(S, Q)
        k += i < N and S[i].startswith(Q)
    os.write(1, str(k).encode("ascii"))
    os._exit(0)


main()
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
kiwiyou|37968|52|Python3|418
#### **📝해설**

```python
import sys
from bisect import bisect_left

# 입력받기
N, M = map(int, sys.stdin.readline().rstrip().split())

# 오름차순으로 정렬
arr = sorted(sys.stdin.readline().rstrip() for _ in range(N))

answer = 0
for _ in range(M):
    query = sys.stdin.readline().rstrip()

    # 이진탐색을 통해 사전순으로 어디에 위치하는지 확인
    idx = bisect_left(arr, query)

    # N을 넘지 않고, 문자열이 그 단어로 시작하면 += 1
    if idx < N and arr[idx].startswith(query):
        answer += 1

print(answer)
```