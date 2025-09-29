# [15824] 너 봄에는 캡사이신이 맛있단다

### **난이도**
골드 2
## **📝문제**
주헌이는 매운맛을 좋아한다. 정확히는, 매운맛을 먹음으로써 느낄 수 있는 고통에서 희열을 느끼는 진정한 '즐기는 자'다.

'스코빌 지수'란 고추류가 가진 매운맛의 원인인 캡사이신의 농도를 수치화 한 단위이다. 주헌이가 느끼는 매운 정도는 굉장히 독특한데, 먹고 있는 메뉴의 절대 수치가 아닌 음식과의 상대수치에 기반한다. 예를 들어 [5, 2, 8]의 스코빌 지수를 가진 음식을 먹을 때 주헌이가 느끼는 매운 정도는 가장 높은 수치인 8과 가장 낮은 수치인 2의 차이인 6만큼의 매운맛을 느낀다. 이처럼 메뉴들의 스코빌 지수가 있을 때 그 최댓값과 최솟값의 차이를 "주헌고통지수"라고 정의한다.

![이미지](https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/15824/1.png)

그림1. 고추처럼 보이지만 문제와는 무관합니다. 

최근 주헌이에게 좋아하는 매운맛 전문점이 생겼다. 메뉴가 아주 다양한 이 음식점은 모든 메뉴의 스코빌 지수를 명시한 메뉴판을 제공한다. 주헌이의 목표는 이 음식점의 모든 음식 조합을 먹어보는 것이다. 하지만 주헌이는 까다로워서 한 번 먹어본 조합은 다시 먹지 않는다.

이 음식점의 모든 조합을 먹어 볼 때 주헌이가 즐길 수 있는 주헌고통지수의 합을 구해보자.
### **입력**
첫 줄에 메뉴의 총 개수 N이 주어진다. 두 번째 줄에는 N개의 메뉴의 스코빌 지수가 주어진다. 모든 스코빌 지수는 0보다 크거나 같고 231-1보다 작거나 같은 정수이다.
### **출력**
한 줄에 모든 조합의 주헌고통지수 합을 1,000,000,007로 나눈 나머지를 출력한다.
### **예제입출력**

**예제 입력1**

```
3
5 2 8
```

**예제 출력1**

```
18
```

**예제 입력2**

```
6
1 4 5 5 6 10
```

**예제 출력2**

```
307
```
### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys

MOD = 10**9 + 7

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

pow2 = [1] * N
for i in range(1, N):
    pow2[i] = pow2[i - 1] * 2 % MOD

result = 0
for i in range(N):
    max_count = pow2[i]
    min_count = pow2[N-1-i]
    contribution = (max_count - min_count) * arr[i] % MOD
    result = (result + contribution) % MOD

print(result)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|162004|224|PyPy3|393
#### **📝해설**

**알고리즘**
```
1. 조합
2. 수학
```

### **다른 풀이**

```python
import io, os, sys


def main():
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    n = int(input())
    arr = sorted(map(int, input().split()))

    result = 0
    p = 1
    for a, b in zip(arr, reversed(arr)):
        result = (result + (a - b) * p) % 1000000007
        p = (p * 2) % 1000000007

    print(result)


if __name__ == "__main__":
    sys.exit(main())

```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
20210805|162916|188|PyPy3|386
#### **📝해설**

```python
import sys

MOD = 10**9 + 7

# 입력받은 후 오름차순 정렬
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

# 2의 거듭제곱을 미리 계산(메모이제이션)
pow2 = [1] * N
for i in range(1, N):
    pow2[i] = pow2[i - 1] * 2 % MOD

# 결과
result = 0

# 작은 수 부터 확인하면서
for i in range(N):

    # arr[i]가 최대값이 되게 할 때 부분 집합의 수
    max_count = pow2[i]

    # arr[i]가 최솟값이 될 때 부분 집합의 개수
    min_count = pow2[N-1-i]

    # (최대값으로 등장한 횟수 - 최소값으로 등장한 횟수) * 해당 숫자
    contribution = (max_count - min_count) * arr[i] % MOD
    result = (result + contribution) % MOD

print(result)
```

### **🔖정리**

1. 처음에 i, j가 최솟값, 최대값으로 정해둔 뒤 사이의 원소들의 부분집합의 개수를 구하는 방식으로 구했다 -> 시간초과
2. 결국 최적화를 통해 NlogN으로 구할 수 있었음.