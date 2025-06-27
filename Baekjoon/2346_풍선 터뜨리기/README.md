# [2346] 풍선 터뜨리기

### **난이도**
실버 3
## **📝문제**
1번부터 N번까지 N개의 풍선이 원형으로 놓여 있고. i번 풍선의 오른쪽에는 i+1번 풍선이 있고, 왼쪽에는 i-1번 풍선이 있다. 단, 1번 풍선의 왼쪽에 N번 풍선이 있고, N번 풍선의 오른쪽에 1번 풍선이 있다. 각 풍선 안에는 종이가 하나 들어있고, 종이에는 -N보다 크거나 같고, N보다 작거나 같은 정수가 하나 적혀있다. 이 풍선들을 다음과 같은 규칙으로 터뜨린다.

우선, 제일 처음에는 1번 풍선을 터뜨린다. 다음에는 풍선 안에 있는 종이를 꺼내어 그 종이에 적혀있는 값만큼 이동하여 다음 풍선을 터뜨린다. 양수가 적혀 있을 경우에는 오른쪽으로, 음수가 적혀 있을 때는 왼쪽으로 이동한다. 이동할 때에는 이미 터진 풍선은 빼고 이동한다.

예를 들어 다섯 개의 풍선 안에 차례로 3, 2, 1, -3, -1이 적혀 있었다고 하자. 이 경우 3이 적혀 있는 1번 풍선, -3이 적혀 있는 4번 풍선, -1이 적혀 있는 5번 풍선, 1이 적혀 있는 3번 풍선, 2가 적혀 있는 2번 풍선의 순서대로 터지게 된다.
### **입력**
첫째 줄에 자연수 N(1 ≤ N ≤ 1,000)이 주어진다. 다음 줄에는 차례로 각 풍선 안의 종이에 적혀 있는 수가 주어진다. 종이에 0은 적혀있지 않다.
### **출력**
첫째 줄에 터진 풍선의 번호를 차례로 나열한다.
### **예제입출력**

**예제 입력1**

```
5
3 2 1 -3 -1
```

**예제 출력1**

```
1 4 5 3 2
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from collections import deque

N = int(input())
arr = list(map(int, input().split()))

q = deque((i + 1, move) for i, move in enumerate(arr))
result = []

while q:
    idx, move = q.popleft()
    result.append(idx)

    if not q:
        break

    if move > 0:
        q.rotate(-(move - 1))
    else:
        q.rotate(-move)

print(" ".join(map(str, result)))    
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|34936|56|Python3|364
#### **📝해설**

**알고리즘**
```
1. 덱
```

### **다른 풀이**

```python
def main():
    N = int(input())  # 카드의 개수 입력 받기
    cards = list(map(int, input().split()))  # 카드 값 입력 받기
    balloons = list(range(N))  # 카드 위치를 나타내는 리스트 생성
    ind = 0  # 현재 인덱스
    result = []

    while cards:
        result.append(balloons.pop(ind) + 1)  # 해당 카드의 원래 위치 기록
        mov = cards.pop(ind)  # 현재 위치의 이동 값

        if not cards:
            break

        if mov > 0:
            ind = (ind + mov - 1) % len(cards)
        else:
            ind = (ind + mov) % len(cards)

    print(" ".join(map(str, result)))  # 결과 출력

if __name__ == "__main__":
    main()
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
dks0808|31120|28|Python3|692
#### **📝해설**

```python
from collections import deque

# 입력받기
N = int(input())
arr = list(map(int, input().split()))

# 인덱스와 풍선을 deque에 함께 저장
q = deque((i + 1, move) for i, move in enumerate(arr))
result = []

# deque를 모두 pop할때까지 반복
while q:
    idx, move = q.popleft()

    # 이번에 나온 풍선을 결과로 추가
    result.append(idx)

    # 모두 끝났다면 종료
    if not q:
        break

    # 양수인 경우
    if move > 0:

        # 오른쪽으로 회전(이미 pop을 하나 했으므로 -1)
        q.rotate(-(move - 1))

    # 음수인 경우
    else:
        # 왼쪽으로 회전
        q.rotate(-move)

print(" ".join(map(str, result)))    
```