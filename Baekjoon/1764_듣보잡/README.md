# [1764] 듣보잡

### **난이도**
실버 4
## **📝문제**
김진영이 듣도 못한 사람의 명단과, 보도 못한 사람의 명단이 주어질 때, 듣도 보도 못한 사람의 명단을 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 듣도 못한 사람의 수 N, 보도 못한 사람의 수 M이 주어진다. 이어서 둘째 줄부터 N개의 줄에 걸쳐 듣도 못한 사람의 이름과, N+2째 줄부터 보도 못한 사람의 이름이 순서대로 주어진다. 이름은 띄어쓰기 없이 알파벳 소문자로만 이루어지며, 그 길이는 20 이하이다. N, M은 500,000 이하의 자연수이다.

듣도 못한 사람의 명단에는 중복되는 이름이 없으며, 보도 못한 사람의 명단도 마찬가지이다.
### **출력**
듣보잡의 수와 그 명단을 사전순으로 출력한다.
### **예제입출력**

**예제 입력1**

```
3 4
ohhenrie
charlie
baesangwook
obama
baesangwook
ohhenrie
clinton
```

**예제 출력1**

```
2
baesangwook
ohhenrie
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys

input = sys.stdin.readline
N, M = map(int, input().split())

a = {input().strip() for _ in range(N)}
b = {input().strip() for _ in range(M)}

result = sorted(a & b)

print(len(result))
print(*result, sep='\n')
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|44192|80|Python3|221
#### **📝해설**

**알고리즘**
```
1. 집합
```

### **다른 풀이**

```python
import os

arr = sorted(os.read(0, os.fstat(0).st_size).split()[2:])
result = [a for a, b in zip(arr, arr[1:]) if a == b]
os.write(1, b"%d\n" % len(result) + b"\n".join(result))
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
20210805|40000|44|Python3|178
#### **📝해설**

```python
import sys

input = sys.stdin.readline
N, M = map(int, input().split())

# set로 입력받음
a = {input().strip() for _ in range(N)}
b = {input().strip() for _ in range(M)}

# 두 집합의 교집합을 정렬
result = sorted(a & b)

# 출력
print(len(result))
print(*result, sep='\n')
```