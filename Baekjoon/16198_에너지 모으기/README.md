# [16198] 에너지 모으기

### **난이도**
실버 1
## **📝문제**
N개의 에너지 구슬이 일렬로 놓여져 있고, 에너지 구슬을 이용해서 에너지를 모으려고 한다.

i번째 에너지 구슬의 무게는 Wi이고, 에너지를 모으는 방법은 다음과 같으며, 반복해서 사용할 수 있다.

1. 에너지 구슬 하나를 고른다. 고른 에너지 구슬의 번호를 x라고 한다. 단, 첫 번째와 마지막 에너지 구슬은 고를 수 없다.
2. x번째 에너지 구슬을 제거한다.
3. Wx-1 × Wx+1의 에너지를 모을 수 있다.
4. N을 1 감소시키고, 에너지 구슬을 1번부터 N번까지로 다시 번호를 매긴다. 번호는 첫 구슬이 1번, 다음 구슬이 2번, ... 과 같이 매겨야 한다.
N과 에너지 구슬의 무게가 주어졌을 때, 모을 수 있는 에너지 양의 최댓값을 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 에너지 구슬의 개수 N(3 ≤ N ≤ 10)이 주어진다.

둘째 줄에는 에너지 구슬의 무게 W1, W2, ..., WN을 공백으로 구분해 주어진다. (1 ≤ Wi ≤ 1,000)
### **출력**
첫째 줄에 모을 수 있는 에너지의 최댓값을 출력한다.
### **예제입출력**

**예제 입력1**

```
4
1 2 3 4
```

**예제 출력1**

```
12
```

**예제 입력2**

```
5
100 2 1 3 100
```

**예제 출력2**

```
10400
```

**예제 입력3**

```
7
2 2 7 6 90 5 9
```

**예제 출력3**

```
1818
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N = int(input())
weights = list(map(int, input().split()))

def find_max(weights, energy):
    if len(weights) == 2:
        return energy
    
    max_energy = 0

    for i in range(1, len(weights) - 1):
        energy_sum  = weights[i-1] * weights[i+1]
        new_weights = weights[:i] + weights[i+1:]
        max_energy = max(max_energy, find_max(new_weights, energy + energy_sum))

    
    return max_energy

print(find_max(weights, 0))
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|32412|88|Python3|442
#### **📝해설**

**알고리즘**
```
1. 백트래킹
```

### **다른 풀이**

```python
import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
weights = list(map(int, input().split()))
dp = [[0 for _ in range(N)] for _ in range(N)]

for length in range(3, N + 1):
    for left in range(N - length + 1):
        right = left + length - 1
        for mid in range(left + 1, right):
            energy = weights[left] * weights[right]
            energy += dp[left][mid] + dp[mid][right]
            dp[left][right] = max(dp[left][right], energy)
print(dp[0][N-1])
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
yny3533|31252|40|Python3|493
#### **📝해설**

```python
N = int(input())
weights = list(map(int, input().split()))

# 재귀함수 선언 (현재 무게 리스트, 이번 탐색으로 얻은 에너지)
def find_max(weights, energy):

    # 모든 에너지를 검사했다면 리턴
    if len(weights) == 2:
        return energy
    
    # 최대 에너지 계산
    max_energy = 0

    # i번째 에너지를 빼내는 과정
    for i in range(1, len(weights) - 1):

        # 이번에 빼내면서 얻은 에너지
        energy_sum  = weights[i-1] * weights[i+1]

        # 에너지를 빼서 만든 새로운 리스트
        new_weights = weights[:i] + weights[i+1:]

        # 최대값 계산
        max_energy = max(max_energy, find_max(new_weights, energy + energy_sum))

    
    return max_energy

print(find_max(weights, 0))
```