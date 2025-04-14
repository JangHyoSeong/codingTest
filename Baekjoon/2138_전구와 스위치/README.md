# [2138] 전구와 스위치

### **난이도**
골드 4
## **📝문제**
N개의 스위치와 N개의 전구가 있다. 각각의 전구는 켜져 있는 상태와 꺼져 있는 상태 중 하나의 상태를 가진다. i(1 < i < N)번 스위치를 누르면 i-1, i, i+1의 세 개의 전구의 상태가 바뀐다. 즉, 꺼져 있는 전구는 켜지고, 켜져 있는 전구는 꺼지게 된다. 1번 스위치를 눌렀을 경우에는 1, 2번 전구의 상태가 바뀌고, N번 스위치를 눌렀을 경우에는 N-1, N번 전구의 상태가 바뀐다.

N개의 전구들의 현재 상태와 우리가 만들고자 하는 상태가 주어졌을 때, 그 상태를 만들기 위해 스위치를 최소 몇 번 누르면 되는지 알아내는 프로그램을 작성하시오.
### **입력**
첫째 줄에 자연수 N(2 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 전구들의 현재 상태를 나타내는 숫자 N개가 공백 없이 주어진다. 그 다음 줄에는 우리가 만들고자 하는 전구들의 상태를 나타내는 숫자 N개가 공백 없이 주어진다. 0은 켜져 있는 상태, 1은 꺼져 있는 상태를 의미한다.
### **출력**
첫째 줄에 답을 출력한다. 불가능한 경우에는 -1을 출력한다.
### **예제입출력**

**예제 입력1**

```
3
000
010
```

**예제 출력1**

```
3
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys

N = int(sys.stdin.readline().rstrip())
bulbs = list(map(int, sys.stdin.readline().rstrip()))
targets = list(map(int, sys.stdin.readline().rstrip()))

def toggle(bulbs, idx):
    for i in range(idx-1, idx+2):
        if 0 <= i < len(bulbs):
            bulbs[i] = (bulbs[i] + 1) % 2

def solve(N, bulbs, targets, start_from_zero):
    new_bulbs = bulbs[:]
    count = 0

    if start_from_zero:
        toggle(new_bulbs, 0)
        count += 1
    
    for i in range(1, N):
        if new_bulbs[i-1] != targets[i-1]:
            toggle(new_bulbs, i)
            count += 1

    return count if new_bulbs == targets else int(21e8)

result1 = solve(N, bulbs, targets, True)
result2 = solve(N, bulbs, targets, False)

result = min(result1, result2)
print(result if result != int(21e8) else -1)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|119484|120|PyPy3|801
#### **📝해설**

**알고리즘**
```
1. 그리디 알고리즘
```

### **다른 풀이**

```python
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    lamp1 = input().rstrip()
    lamp2 = input().rstrip()
    # state 0: !click and !need / 1: !click and need / 2: click and !need / 3: click and need
    case1_flag, case2_flag = (False, False), (False, True)
    case1_cnt = case2_cnt = 0
    for i in range(n):
        case1_cnt += case1_flag[1]
        case1_flag = (case1_flag[1], (case1_flag[0]==case1_flag[1])!=(lamp1[i]==lamp2[i]))
        case2_cnt += case2_flag[1]
        case2_flag = (case2_flag[1], (case2_flag[0]==case2_flag[1])!=(lamp1[i]==lamp2[i]))
    if case1_flag[1] and case2_flag[1]:
        print(-1)
    elif case1_flag[1]:
        print(case2_cnt)
    else:
        print(case1_cnt)

if __name__ == "__main__":
    main()
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
akdlxm39|32412|60|Python3|768
#### **📝해설**

```python
import sys

N = int(sys.stdin.readline().rstrip())
bulbs = list(map(int, sys.stdin.readline().rstrip()))
targets = list(map(int, sys.stdin.readline().rstrip()))

def toggle(bulbs, idx):
    # 인덱스를 기준으로 스위치의 상태를 바꾸는 함수
    for i in range(idx-1, idx+2):
        if 0 <= i < len(bulbs):
            bulbs[i] = (bulbs[i] + 1) % 2

def solve(N, bulbs, targets, start_from_zero):
    # 스위치를 총 몇번 바꾸는지 검사하는 함수
    # N: 리스트의 길이, bulbs: 전구 초기 상태, targets: 만들어야 하는 전구 상태, start_from_zero: 0번째 전구 스위치 조작 여부
    new_bulbs = bulbs[:]
    count = 0

    # 0번째 전구의 스위치를 조작
    if start_from_zero:
        toggle(new_bulbs, 0)
        count += 1
    
    # 1번째부터 만들어야 할 상태와 다르다면 스위치를 조작
    for i in range(1, N):
        if new_bulbs[i-1] != targets[i-1]:
            toggle(new_bulbs, i)
            count += 1

    # 리스트를 제대로 만들었다면 횟수를 리턴, 아니라면 임의의 큰 수를 리턴
    return count if new_bulbs == targets else int(21e8)

# 첫번째 스위치를 조작하거나 하지 않은 경우를 모두 검사
result1 = solve(N, bulbs, targets, True)
result2 = solve(N, bulbs, targets, False)

# 출력
result = min(result1, result2)
print(result if result != int(21e8) else -1)
```