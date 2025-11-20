# [1749] 점수따먹기

### **난이도**
골드 4
## **📝문제**
동주는 항상 혼자 노느라 심심하다. 하지만 혼자 놀기의 고수가 된 동주는 매일매일 게임을 개발하여 혼자놀기의 진수를 우리에게 보여준다. 어느 날 동주는 새로운 게임을 개발하였다. 바로 점수 따먹기라는 게임인데 그다지 재밌어 보이지는 않는다.

동주가 개발한 게임은 이렇다. 일단 N*M 행렬을 그린 다음, 각 칸에 -10,000 이상 10,000 이하의 정수를 하나씩 쓴다. 그런 다음 그 행렬의 부분행렬을 그려 그 안에 적힌 정수의 합을 구하는 게임이다.

동주가 혼자 재밌게 놀던 중 지나가는 당신을 보고 당신을 붙잡고 게임을 하자고 한다. 귀찮은 당신은 정수의 합이 최대가 되는 부분행렬을 구하여 빨리 동주에게서 벗어나고 싶다.
### **입력**
첫째 줄에 N (1 < N < 200), M (1 < M < 200)이 주어진다. 그 다음 N개의 줄에 M개씩 행렬의 원소가 주어진다.
### **출력**
첫째 줄에 최대의 합을 출력하라.
### **예제입출력**

**예제 입력1**

```
3 5
2 3 -21 -22 -23
5 6 -22 -23 -25
-22 -23 4 10 2
```

**예제 출력1**

```
16
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N, M = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]

max_sum = int(-21e8)
for top in range(N):
    temp = [0] * M

    for bottom in range(top, N):
        
        for col in range(M):
            temp[col] += table[bottom][col]

        current_max = temp[0]
        max_ending_here = temp[0]

        for i in range(1, M):
            max_ending_here = max(temp[i], max_ending_here + temp[i])
            current_max = max(current_max, max_ending_here)
        
        max_sum = max(max_sum, current_max)

print(max_sum)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|111040|160|PyPy3|565
#### **📝해설**

**알고리즘**
```
1. 누적합
```

### **다른 풀이**

```python
import io, os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def main():
    n, m = map(int, input().split())
    rsum = []
    for _ in range(n):
        row = [0]
        for x in map(int, input().split()):
            row.append(row[-1] + x)
        rsum.append(row)
    
    mx = -400_000_000
    for b in range(1, m+1):
        for a in range(0, b):
            cur = rsum[0][b] - rsum[0][a]
            if cur > mx: mx = cur
            for i in range(1, n):
                if cur > 0: cur += rsum[i][b] - rsum[i][a]
                else: cur = rsum[i][b] - rsum[i][a]
                if cur > mx: mx = cur
    
    print(mx)
    
if __name__ == "__main__": main()
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
mhc|111284|132|PyPy3|686
#### **📝해설**

```python
N, M = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]

# 정답으로 사용될 최대 합
max_sum = int(-21e8)

# 위에서부터 한줄씩 확인
for top in range(N):
    temp = [0] * M

    # 아래에서부터 인덱스를 설정해 top, down으로 범위 설정
    for bottom in range(top, N):
        
        # 세로 한줄씩 확인
        for col in range(M):

            # 현재 누적합
            temp[col] += table[bottom][col]

        # 이번 줄에서 최대합을 구함
        current_max = temp[0]
        max_ending_here = temp[0]

        # 하나씩 확인하면서 어느때 최대 합인지 구함
        for i in range(1, M):
            max_ending_here = max(temp[i], max_ending_here + temp[i])
            current_max = max(current_max, max_ending_here)
        
        max_sum = max(max_sum, current_max)

print(max_sum)
```