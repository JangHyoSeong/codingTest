# [1138] 한 줄로 서기

### **난이도**
실버 2
## **📝문제**
N명의 사람들은 매일 아침 한 줄로 선다. 이 사람들은 자리를 마음대로 서지 못하고 오민식의 지시대로 선다.

어느 날 사람들은 오민식이 사람들이 줄 서는 위치를 기록해 놓는다는 것을 알았다. 그리고 아침에 자기가 기록해 놓은 것과 사람들이 줄을 선 위치가 맞는지 확인한다.

사람들은 자기보다 큰 사람이 왼쪽에 몇 명 있었는지만을 기억한다. N명의 사람이 있고, 사람들의 키는 1부터 N까지 모두 다르다.

각 사람들이 기억하는 정보가 주어질 때, 줄을 어떻게 서야 하는지 출력하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 사람의 수 N이 주어진다. N은 10보다 작거나 같은 자연수이다. 둘째 줄에는 키가 1인 사람부터 차례대로 자기보다 키가 큰 사람이 왼쪽에 몇 명이 있었는지 주어진다. i번째 수는 0보다 크거나 같고, N-i보다 작거나 같다. i는 0부터 시작한다.
### **출력**
첫째 줄에 줄을 선 순서대로 키를 출력한다.
### **예제입출력**

**예제 입력1**

```
4
2 1 1 0
```

**예제 출력1**

```
4 2 1 3
```

**예제 입력2**

```
5
0 0 0 0 0
```

**예제 출력2**

```
1 2 3 4 5
```

**예제 입력3**

```
6
5 4 3 2 1 0
```

**예제 출력3**

```
6 5 4 3 2 1
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N = int(input())
arr = list(map(int, input().split()))

line = [0] * N

for i in range(N):
    count = arr[i]
    for j in range(N):
        if count == 0 and line[j] == 0:
            line[j] = i+1
            break

        elif line[j] == 0:
            count -= 1

print(" ".join(map(str, line)))
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|31120|40|Python3|300
#### **📝해설**

**알고리즘**
```
1. 그리디 알고리즘
```

### **다른 풀이**

```python
n=int(input())
arr=list(map(int,input().split()))
answer=[0]*n
for i in range(n):
    cnt=0
    for j in range(n):
        if cnt==arr[i] and answer[j]==0:
            answer[j]=i+1
            break
        elif answer[j]==0:
            cnt+=1
print(' '.join(map(str,answer)))
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
nangmancat123|31120|28|Python3|279
#### **📝해설**

```python
N = int(input())
arr = list(map(int, input().split()))

# 줄을 선 정보
line = [0] * N


for i in range(N):
    # 현재 인덱스보다 키 큰 사람의 수를 count에 저장
    count = arr[i]

    # 한번 더 순회하면서
    for j in range(N):

        # i번째 사람을 j번에 위치
        if count == 0 and line[j] == 0:
            line[j] = i+1
            break
          
        elif line[j] == 0:
            count -= 1

print(" ".join(map(str, line)))
```