# [9082] 지뢰찾기

### **난이도**
골드 4
## **📝문제**
지뢰찾기 게임은 2×N 배열에 숨겨져 있는 지뢰를 찾는 게임이다. 지뢰 주위에 쓰여 있는 숫자들로 지뢰를 찾을 수 있는데, 한 블록에 쓰여진 숫자는 그 블록 주위에 지뢰가 몇 개 있는지를 나타낸다. 지뢰가 확실히 있는 위치를 *, 숨겨진 블록을 #으로 표시한다. 첫째 줄에는 숫자만 나타나고 둘째 줄에는 *와 #만 나타나는데, 지뢰는 둘째 줄에만 있다.

```
12110
##*##
```
위의 그림 2×5 배열에는 지뢰가 2개가 있다는 것을 알 수 있다. 숨겨진 블록 중 첫 번째 블록에 지뢰가 숨겨져 있고, 나머지 하나는 두 번째 줄의 가운데에 있다.

2×N 배열이 주어지면 주어진 배열에 있는 모든 지뢰의 개수(*까지 포함)를 찾는 프로그램을 작성하시오.
### **입력**
입력의 첫 줄에는 테스트 케이스의 개수 T(1 ≤ T ≤ 10)가 주어진다. 각 테스트 케이스는 첫 줄에 배열의 크기 N(1 ≤ N ≤ 100)이 주어지고, 그 다음 두 줄에 걸쳐서 배열이 주어진다. 첫 줄에는 항상 숫자만이 나타나며 이 숫자들 사이에 공백은 없으며, 둘째 줄에 주어지는 입력들 사이에도 공백은 없다. 그리고 이 숫자들은 올바른 값만이 입력으로 들어온다(지뢰의 위치에 대해 불가능한 값은 입력으로 주지 않는다).
### **출력**
각 테스트 케이스에 대해서 주어진 배열에 있는 모든 지뢰의 수를 한 줄에 하나씩 출력한다. 지뢰의 수가 여럿이 될 수 있으면 가능한 지뢰의 수 중 최댓값을 출력한다.
### **예제입출력**

**예제 입력1**

```
2
5
11122
####*
5
23321
#####
```

**예제 출력1**

```
3
4
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
T = int(input())
for testcase in range(T):
    N = int(input())
    graph = []
    graph.append([int(c) for c in input().strip()])
    graph.append([c for c in input().strip()])

    result = 0

    for i in range(N):
        if graph[1][i] == '*':
            result += 1
            if i > 0:
                graph[0][i - 1] -= 1
            graph[0][i] -= 1
            if i < N - 1:
                graph[0][i + 1] -= 1

    if graph[1][0] == '#' and graph[0][0] != 0 and graph[0][1] != 0:
        result += 1
        graph[0][0] -= 1
        graph[0][1] -= 1

    for i in range(1, N - 1):
        if graph[1][i] == '#':
            if graph[0][i - 1] >= 1 and graph[0][i] >= 1 and graph[0][i + 1] >= 1:
                result += 1
                graph[0][i - 1] -= 1
                graph[0][i] -= 1
                graph[0][i + 1] -= 1

    if graph[1][N - 1] == '#' and graph[0][N - 1] != 0 and graph[0][N - 2] != 0:
        result += 1
        graph[0][N - 1] -= 1
        graph[0][N - 2] -= 1

    print(result)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|31120|28|Python3|1023
#### **📝해설**

**알고리즘**
```
1. 그리디 알고리즘
```

### **다른 풀이**

```python
from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    n = int(input())
    array = list(map(int, input().rstrip()))
    mine = input().rstrip()

    answer = 0
    for i in range (n) :
        if i == 0:
            if array[0] != 0 and array[1] != 0:
                array[0] -= 1
                array[1] -= 1
                answer += 1
        elif i == n - 1:
            if array[i] != 0 and array[i - 1] != 0:
                array[i - 1] -= 1
                array[i - 2] -= 1
                answer += 1
        else:
            if array[i - 1] != 0 and array[i] != 0 and array[i + 1] != 0:
                array[i - 1] -= 1
                array[i] -= 1
                array[i + 1] -= 1
                answer += 1
    print(answer)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
peh4622|31120|28|Python3|770