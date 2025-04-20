# [2776] 암기왕

### **난이도**
실버 4
## **📝문제**
연종이는 엄청난 기억력을 가지고 있다. 그래서 하루 동안 본 정수들을 모두 기억 할 수 있다. 하지만 이를 믿을 수 없는 동규는 그의 기억력을 시험해 보기로 한다. 동규는 연종을 따라 다니며, 연종이 하루 동안 본 정수들을 모두 ‘수첩1’에 적어 놓았다. 그것을 바탕으로 그가 진짜 암기왕인지 알아보기 위해, 동규는 연종에게 M개의 질문을 던졌다. 질문의 내용은 “X라는 정수를 오늘 본 적이 있는가?” 이다. 연종은 막힘없이 모두 대답을 했고, 동규는 연종이 봤다고 주장하는 수 들을 ‘수첩2’에 적어 두었다. 집에 돌아온 동규는 답이 맞는지 확인하려 하지만, 연종을 따라다니느라 너무 힘들어서 여러분에게 도움을 요청했다. 동규를 도와주기 위해 ‘수첩2’에 적혀있는 순서대로, 각각의 수에 대하여, ‘수첩1’에 있으면 1을, 없으면 0을 출력하는 프로그램을 작성해보자.
### **입력**
첫째 줄에 테스트케이스의 개수 T가 들어온다. 다음 줄에는 ‘수첩 1’에 적어 놓은 정수의 개수 N(1 ≤ N ≤ 1,000,000)이 입력으로 들어온다. 그 다음 줄에  ‘수첩 1’에 적혀 있는 정수들이 N개 들어온다. 그 다음 줄에는 ‘수첩 2’에 적어 놓은 정수의 개수 M(1 ≤ M ≤ 1,000,000) 이 주어지고, 다음 줄에 ‘수첩 2’에 적어 놓은 정수들이 입력으로 M개 들어온다. 모든 정수들의 범위는 int 로 한다.
### **출력**

### **예제입출력**

**예제 입력1**

```
1
5
4 1 5 2 3
5
1 3 7 9 5
```

**예제 출력1**

```
1
1
0
0
1
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    arr_1 = set(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline().rstrip())
    arr_2 = list(map(int, sys.stdin.readline().split()))
    
    for num in arr_2:
        print(1 if num in arr_1 else 0)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|304516|936|PyPy3|336
#### **📝해설**

**알고리즘**
```
1. 해쉬
```

### **다른 풀이**

```python
def main():
    import io, os
    input = io.BufferedReader(io.FileIO(0), buffer_size=1 << 18).readline
    T = int(input())
    row = bytearray()
    for _ in range(T):
        input()
        counter = set(input().split())
        M = int(input())
        for e in input().split():
            row.append(48 | (e in counter))
            row.append(32)
    os.write(1, row)

main()
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
kiwiyou|180340|672|Python3|383
#### **📝해설**

```python
import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    # 배열 1을 집합으로 저장(해쉬)
    arr_1 = set(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline().rstrip())
    arr_2 = list(map(int, sys.stdin.readline().split()))
    
    # 배열 2의 숫자가 1에 있는지 검사
    for num in arr_2:
        print(1 if num in arr_1 else 0)
```