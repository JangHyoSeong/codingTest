# [18291] 비요뜨의 징검다리 건너기

### **난이도**
골드 5
## **📝문제**
비요뜨는 지금 강 앞에 서 있다. 강 위에는 징검다리가 놓여 있다.

징검다리는 비요뜨가 있는 방향에서부터 반대 방향까지 차례로 1번, 2번, ..., N번의 번호를 가지고 있다.

비요뜨는 1번 징검다리 위에 올라갔다. 그리고 아래 두 가지 규칙을 지키며 징검다리를 건너려고 한다.

- 1 ≤ X ≤ N 인 임의의 정수 X에 대해, 현재 있는 징검다리의 번호를 i번이라고 할 때 i+X번 징검다리로 뛸 수 있다.
- N번째 징검다리를 지나쳐선 안 되고, 정확히 도착해야 한다   
비요뜨는 자신의 특기인 코딩을 살리기 위해 노트북을 켰지만, 실수로 노트북을 강에 빠뜨리고 말았다.

비요뜨를 대신해 강을 건너는 경우의 수를 구해 주자!
### **입력**
첫 번째 줄에 테스트 케이스의 수 T가 주어진다. (1 ≤ T ≤ 1000)

각 테스트 케이스는 한 줄로 구성되며, 징검다리의 개수를 의미하는 N이 주어진다. (1 ≤ N ≤ 109)
### **출력**
각 테스트 케이스에 대해, 한 줄에 하나씩 규칙을 만족하면서 징검다리를 건너는 경우의 수를 109+7로 나눈 나머지를 출력한다.
### **예제입출력**

**예제 입력1**

```
1
4
```

**예제 출력1**

```
4
```
### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
T = int(input())

def power(n):
    if n == 0:
        return 1

    if n == 1:
        return 2

    next = power(n//2) % 1000000007
    
    if n % 2:
        return next * next * 2 % 1000000007
    
    else:
        return next * next % 1000000007

for _ in range(T):
    N = int(input())

    if N <= 2:
        print(1)
        continue

    print(power(N-2))
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|31120|96|Python3|365
#### **📝해설**

**알고리즘**
```
1. 분할정복 거듭제곱
```

### **다른 풀이**

```python
import sys
input = sys.stdin.readline
MOD = int(1e9) + 7

ans = []
for _ in range(int(input())):
    n = max(2, int(input()))
    ans.append(pow(2, n-2, MOD))

print('\n'.join(map(str, ans)))
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
leehk_py|31120|40|Python3|231
#### **📝해설**

```python
T = int(input())

def power(n):
  # 거듭제곱을 위한 함수
  
    if n == 0:
        return 1

    if n == 1:
        return 2
    
    # 다음번의 숫자를 미리 계산
    next = power(n//2) % 1000000007
    
    if n % 2:
        return next * next * 2 % 1000000007
    
    else:
        return next * next % 1000000007

for _ in range(T):
    N = int(input())

    if N <= 2:
        print(1)
        continue

    print(power(N-2))
```