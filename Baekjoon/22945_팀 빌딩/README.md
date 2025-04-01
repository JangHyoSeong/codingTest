# [22945] 팀 빌딩

### **난이도**
골드 4
## **📝문제**
개발자 $N$명이 팀 빌딩을 위해 한 줄로 서있다.

하나의 팀을 만들기 위해서는 개발자 2명이 반드시 모여야 한다.

개발자 A와 개발자 B가 팀을 만들 때 팀의 능력치는 아래와 같이 계산이 된다.

- (개발자 A와 개발자 B 사이에 존재하는 다른 개발자 수) × min(개발자 A의 능력치, 개발자 B의 능력치)  
예를 들어, 4명의 개발자가 존재할 때, 각 개발자의 능력치를 1 4 2 5라고 하자. 이때 능력치가 1인 개발자와 능력치가 5인 개발자가 한 팀을 이뤘다고 가정하자. 그러면 이 팀의 능력치는 $2×min(1, 5) = 2$가 된다.

팀 빌딩에서 나올 수 있는 팀 중 능력치의 최대값을 구해보자.
### **입력**
첫 번째 줄에 개발자의 수 $N$이 주어진다.

두 번째 줄에는 $N$의 개발자의 각 능력치 $x_{i}$가 공백으로 구분되어 주어진다.

 
- $2 ≤ N ≤ 100,000$ 
- $1 ≤ x_i ≤ 10,000$, $x_i$는 정수
### **출력**
팀의 능력치 최댓값을 출력한다.
### **예제입출력**

**예제 입력1**

```
4
1 4 2 5
```

**예제 출력1**

```
4
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys

N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

left, right = 0, N-1

max_status = 0

while left < right:
    gap = right - left - 1
    max_status = max(max_status, min(arr[left], arr[right]) * gap)

    if arr[left] < arr[right]:
        left += 1
    else:
        right -= 1

print(max_status)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|42168|108|Python3|361
#### **📝해설**

**알고리즘**
```
1. 투 포인터
```

### **다른 풀이**

```python
# https://www.acmicpc.net/problem/22945
"""
투포인터
"""
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    left, right = 0, n - 1

    result = 0
    while left < right:
        a, b = arr[left], arr[right]
        
        result = max(result, (right - left - 1) * min(a, b))

        if a <= b:
            left += 1
        else:
            right -= 1
    print(result)


if __name__ == "__main__":
    main()
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
hogandi001|42168|76|Python3|508
#### **📝해설**

```python
import sys

# 입력
N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

# 투 포인터 인덱스
left, right = 0, N-1

# 최대 능력치
max_status = 0

# 투포인터가 겹칠때까지 반복
while left < right:

    # 두 개발자 사이의 개발자
    gap = right - left - 1

    # 최대 능력치를 갱신
    max_status = max(max_status, min(arr[left], arr[right]) * gap)

    # 능력치가 작은 쪽의 인덱스를 옮김
    if arr[left] < arr[right]:
        left += 1
    else:
        right -= 1
# 출력
print(max_status)
```