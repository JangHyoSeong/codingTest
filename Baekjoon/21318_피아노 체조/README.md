# [21318] 피아노 체조

### **난이도**
실버 1
## **📝문제**
피아노를 사랑하는 시은이는 매일 아침 피아노 체조를 한다. 시은이는 N개의 악보를 가지고 있으며, 1번부터 N번까지의 번호로 부른다. 각 악보는 1 이상 109 이하의 정수로 표현되는 난이도를 가지고 있다. 난이도를 나타내는 수가 클수록 어려운 악보이다. 1 ≤ x ≤ y ≤ N 을 만족하는 두 정수 x, y를 골라 x번부터 y번까지의 악보를 번호 순서대로 연주하는 것이 피아노 체조이다.

시은이는 피아노 체조를 할 때, 지금 연주하는 악보가 바로 다음에 연주할 악보보다 어렵다면 실수를 한다. 다시 말하자면, i(x ≤ i < y)번 악보의 난이도가 i + 1번 악보의 난이도보다 높다면 실수를 한다. 특히, 마지막으로 연주하는 y번 악보에선 절대 실수하지 않는다. 시은이는 오늘도 피아노 체조를 하기 위해 두 정수 x와 y를 골랐고, 문득 궁금한 것이 생겼다. 오늘 할 피아노 체조에서 실수하는 곡은 몇 개나 될까?
### **입력**
첫 번째 줄에 악보의 개수 N(1 ≤ N ≤ 100,000)이 주어진다.

두 번째 줄에 1번 악보부터 N번 악보까지의 난이도가 공백을 구분으로 주어진다.

세 번째 줄에 질문의 개수 Q(1 ≤ Q ≤ 100,000)이 주어진다.

다음 Q개의 줄에 각 줄마다 두 개의 정수 x, y(1 ≤ x ≤ y ≤ N)가 주어진다.
### **출력**
x번부터 y번까지의 악보를 순서대로 연주할 때, 몇 개의 악보에서 실수하게 될지 0 이상의 정수 하나로 출력한다. 각 출력은 개행으로 구분한다.
### **예제입출력**

**예제 입력1**

```
9
1 2 3 3 4 1 10 8 1
5
1 3
2 5
4 7
9 9
5 9
```

**예제 출력1**

```
0
0
1
0
3
```

**예제 입력2**

```
6
573 33283 5572 346 906 567
5
5 6
1 3
2 2
1 6
3 6
```

**예제 출력2**

```
1
1
0
3
2
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N = int(input())
arr = list(map(int, input().split()))
Q = int(input())
queries = [tuple(map(int, input().split())) for _ in range(Q)]

mistakes = [0] * (N)
for i in range(1, N):
    if arr[i-1] > arr[i]:
        mistakes[i] = mistakes[i-1] + 1
    else:
        mistakes[i] = mistakes[i-1]

for query in queries:
    a, b = query
    print(mistakes[b-1] - mistakes[a-1])
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|54212|2824|Python3|371
#### **📝해설**

**알고리즘**
```
1. 누적합
```

#### **📝해설**

```python
N = int(input())
arr = list(map(int, input().split()))
Q = int(input())
queries = [tuple(map(int, input().split())) for _ in range(Q)]

# 실수의 누적합을 구함
mistakes = [0] * (N)
for i in range(1, N):
    if arr[i-1] > arr[i]:
        mistakes[i] = mistakes[i-1] + 1
    else:
        mistakes[i] = mistakes[i-1]

# 누적합을 통해 각 쿼리마다 답을 출력
for query in queries:
    a, b = query
    print(mistakes[b-1] - mistakes[a-1])
```