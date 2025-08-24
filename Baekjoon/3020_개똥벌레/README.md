# [3020] 개똥벌레

### **난이도**
골드 5
## **📝문제**
개똥벌레 한 마리가 장애물(석순과 종유석)로 가득찬 동굴에 들어갔다. 동굴의 길이는 N미터이고, 높이는 H미터이다. (N은 짝수) 첫 번째 장애물은 항상 석순이고, 그 다음에는 종유석과 석순이 번갈아가면서 등장한다.

아래 그림은 길이가 14미터이고 높이가 5미터인 동굴이다. (예제 그림)

![이미지](https://upload.acmicpc.net/c6fd496d-ccf5-4f9d-a06e-32b121fc6a82/-/preview/)

이 개똥벌레는 장애물을 피하지 않는다. 자신이 지나갈 구간을 정한 다음 일직선으로 지나가면서 만나는 모든 장애물을 파괴한다.

위의 그림에서 4번째 구간으로 개똥벌레가 날아간다면 파괴해야하는 장애물의 수는 총 여덟개이다. (4번째 구간은 길이가 3인 석순과 길이가 4인 석순의 중간지점을 말한다)

![이미지](https://upload.acmicpc.net/bfcbb94f-0e15-4ff9-b2ef-43e07c7ee503/-/preview/)

하지만, 첫 번째 구간이나 다섯 번째 구간으로 날아간다면 개똥벌레는 장애물 일곱개만 파괴하면 된다.

동굴의 크기와 높이, 모든 장애물의 크기가 주어진다. 이때, 개똥벌레가 파괴해야하는 장애물의 최솟값과 그러한 구간이 총 몇 개 있는지 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 N과 H가 주어진다. N은 항상 짝수이다. (2 ≤ N ≤ 200,000, 2 ≤ H ≤ 500,000)

다음 N개 줄에는 장애물의 크기가 순서대로 주어진다. 장애물의 크기는 H보다 작은 양수이다.
### **출력**
첫째 줄에 개똥벌레가 파괴해야 하는 장애물의 최솟값과 그러한 구간의 수를 공백으로 구분하여 출력한다.
### **예제입출력**

**예제 입력1**

```
6 7
1
5
3
3
5
1
```

**예제 출력1**

```
2 3
```

**예제 입력2**

```
14 5
1
3
4
2
2
4
3
4
3
3
3
2
3
3
```

**예제 출력2**

```
7 2
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys

N, H = map(int, sys.stdin.readline().rstrip().split())

bot = [0] * (H + 2)
top = [0] * (H + 2)

for i in range(N):
    x = int(sys.stdin.readline().rstrip())
    if i % 2 == 0:
        bot[x] += 1
    
    else:
        top[x] += 1

for h in range(H, 0, -1):
    bot[h] += bot[h + 1]
    top[h] += top[h + 1]

crashes = [bot[h] + top[H-h+1] for h in range(1, H+1)]
m = min(crashes)
print(m, crashes.count(m))
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|91400|404|Python3|421
#### **📝해설**

**알고리즘**
```
1. 누적 합
```

### **다른 풀이**

```python
import sys

input = sys.stdin.readline

def solution():
    N, H = map(int, input().split())
    stones = [int(input()) for _ in range(N)]
    cnt_list = [0]*(H+1)
    for i in range(0, N, 2):
        cnt_list[H-stones[i]] += 1
        cnt_list[stones[i+1]] -= 1
    cnt = 0
    min_stone = current = N//2
    for i in range(1, H+1):
        current += cnt_list[i]
        if current < min_stone:
            min_stone = current
            cnt = 1
        elif current == min_stone:
            cnt += 1
    print(min_stone, cnt)

solution()
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
pen2402|44048|136|Python3|542
#### **📝해설**

```python
import sys

N, H = map(int, sys.stdin.readline().rstrip().split())

# 석순, 종유석이 해당 높이에 존재하는 개수
bot = [0] * (H + 2)
top = [0] * (H + 2)

# 입력받기
for i in range(N):
    x = int(sys.stdin.readline().rstrip())

    # 석순
    if i % 2 == 0:
        bot[x] += 1
    
    # 종유석
    else:
        top[x] += 1

# 해당 높이에 존재하는 종유석, 석순의 개수를 누적합으로 구함(부딪힐 횟수)
for h in range(H, 0, -1):
    bot[h] += bot[h + 1]
    top[h] += top[h + 1]

# 종유석, 석순을 합해서 부딪히는 횟수를 구함
crashes = [bot[h] + top[H-h+1] for h in range(1, H+1)]

# 최소로 부딪힐 때
m = min(crashes)

# 최소로 부딪힐 때와 최소값의 갯수
print(m, crashes.count(m))
```