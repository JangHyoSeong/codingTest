# [14658] 하늘에서 별똥별이 빗발친다

### **난이도**
골드 3
## **📝문제**
“오빠! 나 얼마만큼 사랑해?”

“널 위해서라면 저기 저 하늘의 별이라도 따다 줄 수 있어. 지금 따줄까?”

“에이, 거짓말!”

“정말이야. 한 번 봐봐!”

욱제는 하늘을 발로 차버렸다. 그랬더니 정말 별이 떨어졌다. 그런데, 정말로 별이 지구로 떨어지기 시작했다. 욱제는 지구를 지키는 정의의 용사가 되기로 결심했다.

“자기야, 나 세계를 지키고 올게. 꼭 돌아올 테니 조금만 기다려줘.”

지구의 파괴를 막기 위해서는 지표면에 떨어지는 별똥별의 수를 최소화해야 한다. 욱제는 커다란 네모난 L*L 크기의 트램펄린을 준비했다. 별똥별이 어디로 떨어질지는 이미 알고 있기 때문에, 욱제는 이 트램펄린으로 최대한 많은 별똥별을 우주로 튕겨낼 계획이다. 하지만 학교 예산으로 트램펄린을 구매하는 욱제는 이 긴급한 와중에도 예산 심의 통과를 기다리느라 바쁘다!

욱제를 도와 세계를 구하자. 최대한 많은 별똥별을 튕겨내도록 트램펄린을 배치했을 때, 지구에는 몇 개의 별똥별이 부딪히게 될까? (별똥별이 떨어지는 위치는 겹치지 않으며 별똥별은 트램펄린의 모서리에 부딪혀도 튕겨나간다!) 트램펄린은 비스듬하게 배치 할 수 없다.
### **입력**
첫째 줄에 네 정수 N, M, L, K가 주어진다. (1 ≤ N, M ≤ 500,000, 1 ≤ L ≤ 100,000, 1 ≤ K ≤ 100) N은 별똥별이 떨어지는 구역의 가로길이, M은 세로길이, L은 트램펄린의 한 변의 길이, K는 별똥별의 수를 뜻한다. 이후 K개의 줄에 걸쳐 별똥별이 떨어지는 위치의 좌표 (x, y)가 주어진다. (0 ≤ x ≤ N, 0 ≤ y ≤ M)
### **출력**
욱제가 트램펄린으로 최대한 많은 별똥별을 튕겨낼 때, 지구에 부딪히는 별똥별의 개수를 출력한다.
### **예제입출력**

**예제 입력1**

```
12 10 4 7
2 4
7 3
3 1
5 6
4 7
12 10
8 6
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

N, M, L, K = map(int, sys.stdin.readline().rstrip().split())
meteors = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(K)]

max_count = 0
for i in range(K):
    for j in range(K):
        x1 = meteors[i][0]
        y1 = meteors[j][1]

        count = 0

        for x, y in meteors:
            if x1 <= x <= x1 + L and y1 <= y <= y1 +L:
                count += 1

        max_count = max(max_count, count)

print(K - max_count)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|32412|212|Python3|463
#### **📝해설**

**알고리즘**
```
1. 브루트포스 알고리즘
```

### **다른 풀이**

```python
import sys
input = sys.stdin.readline

N, M, L, K = map(int, input().split())
answer= 0
stars = []
for _ in range(K):
    x, y = map(int, input().split())
    stars.append([x, y])

stars.sort()

for x, y in stars: # x 기준
    x1 = x
    x2 = x + L

    target_stars_y = sorted([y for x, y in stars if (x1 <= x <= x2)])

    left = 0

    for right in range(len(target_stars_y)):
        
        while True:
            if (target_stars_y[right] - target_stars_y[left] <= L):
                break
            left += 1

        if (answer < right - left + 1):
            answer = right - left + 1

print(K - answer)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
qkreodnjs97|31120|32|Python3|621
#### **📝해설**

```python
import sys

N, M, L, K = map(int, sys.stdin.readline().rstrip().split())
meteors = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(K)]

max_count = 0

# 모든 별들의 x, y를 기준으로(트램펄린의 왼쪽 아래 꼭지점)
for i in range(K):
    for j in range(K):
        x1 = meteors[i][0]
        y1 = meteors[j][1]

        count = 0

        # 다른 별들이 포함되는지 검사
        for x, y in meteors:
            if x1 <= x <= x1 + L and y1 <= y <= y1 +L:
                count += 1

        max_count = max(max_count, count)

print(K - max_count)
```