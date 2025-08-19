# [4781] 사탕 가게

### **난이도**
골드 4
## **📝문제**
상근이는 선영이와 걸어가다가 사탕 가게를 지나가게 되었다. 갑자기 상근이는 선영이에게 사탕이 얼마나 건강에 안 좋은지 설명하기 시작했다. 선영이는 매우 짜증이 났고, 상근이에게 누가 더 건강이 안 좋아질 수 있는지 내기를 하자고 했다. 상근이는 내기를 그 즉시 받아들였다.

두 사람은 같은 돈을 가지고 가게에 들어가서 사탕을 산다. 이때, 구매한 사탕의 칼로리가 더 큰 사람이 내기에서 이기게 된다.

상근이는 잠시 화장실에 갔다온다고 핑계를 댄 뒤에, 노트북을 열고 사탕 가게의 시스템을 해킹하기 시작했다. 이 시스템에는 현재 사탕 가게에 있는 사탕의 가격과 칼로리가 모두 등재되어 있다. 각 사탕의 개수는 매우 많기 때문에, 원하는 만큼 사탕을 구매할 수 있다. 또, 사탕은 쪼갤 수 없기 때문에, 일부만 구매할 수 없다.

사탕 가게에 있는 모든 사탕의 가격과 칼로리가 주어졌을 때, 어떻게 하면 칼로리의 합이 가장 크게 되는지를 구하는 프로그램을 작성하시오.
### **입력**
각 테스트 케이스의 첫째 줄에는 가게에 있는 사탕 종류의 수 n과 상근이가 가지고 있는 돈의 양 m이 주어진다. (1 ≤ n ≤ 5,000, 0.01 ≤ m ≤ 100.00) m은 항상 소수점 둘째자리까지 주어진다.

다음 n개 줄에는 각 사탕의 칼로리 c와 가격 p가 주어진다. (1 ≤ c ≤ 5,000, 0.01 ≤ p ≤ 100.00) c는 항상 정수, p는 항상 소수점 둘째자리이다.

입력의 마지막 줄에는 '0 0.00'이 주어진다.
### **출력**
각 테스트 케이스에 대해서, 상근이가 돈 m을 가지고 구매할 수 있는 가장 높은 칼로리를 출력한다.
### **예제입출력**

**예제 입력1**

```
2 8.00
700 7.00
199 2.00
3 8.00
700 7.00
299 3.00
499 5.00
0 0.00
```

**예제 출력1**

```
796
798
```
### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
while True:
    N, M = input().split()
    N = int(N)
    M = float(M)

    if N == 0 and M == 0.00:
        break

    M = int(M * 100 + 0.5)
    candies = []
    for _ in range(N):
        c, p = input().split()
        c = int(c)
        p = float(p)
        p = int(p * 100 + 0.5)
        candies.append((p, c))

    dp = [0] * (M + 1)

    for p, c in candies:
        for money in range(p, M + 1):
            dp[money] = max(dp[money], dp[money - p] + c)

    print(dp[M])
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|112140|1632|PyPy3|479
#### **📝해설**

**알고리즘**
```
1. 배낭 문제
```

### **다른 풀이**

```python
import io, os, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
print = sys.stdout.write

def main():
    while True:
        n, m = input().split()
        if n == b'0': break
        n, m = int(n), int(float(m)*100+.5)
        cp = sorted([(int(c), int(float(p)*100+.5)) for c, p in (input().split() for _ in range(n))], key=lambda x: (x[1], -x[0]))
        cand = [cp[0]]
        for i in range(1, n):
            if cp[i][1] != cp[i-1][1] and cand[-1][0] < cp[i][0]: cand.append(cp[i])
        dp = [0]*(m+1)
        for c, p in cand:
            for j in range(p, m+1):
                dp[j] = max(dp[j], dp[j-p]+c)

        print(f'{max(dp)}\n')

if __name__ == "__main__": main()
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
mhc|112676|148|PyPy3|702
#### **📝해설**

```python
while True:
    N, M = input().split()
    N = int(N)
    M = float(M)

    if N == 0 and M == 0.00:
        break
    
    # 소수가 항상 둘째자리까지니, 이걸 정수로 변환
    # 부동소수점 고려
    M = int(M * 100 + 0.5)
    candies = []

    # 사탕 입력받기
    for _ in range(N):
        c, p = input().split()
        c = int(c)
        p = float(p)
        p = int(p * 100 + 0.5)
        candies.append((p, c))

    # dp배열 선언
    dp = [0] * (M + 1)

    # 배낭문제
    for p, c in candies:
        for money in range(p, M + 1):
            dp[money] = max(dp[money], dp[money - p] + c)

    print(dp[M])
```