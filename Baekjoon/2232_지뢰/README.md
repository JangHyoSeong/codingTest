# [2232] 지뢰

### **난이도**
실버 2
## **📝문제**
일직선상에 N개의 지뢰가 같은 간격으로 매설되어 있다. 각각의 지뢰는 충격 강도 Pi가 있어서, Pi를 초과하는 힘을 가하면 Pi만큼의 힘을 발휘하며 터지게 된다. 어떤 지뢰가 터지게 되면, 그 지뢰의 좌우에 있는 지뢰에 힘을 발휘하게 된다. 예를 들어 다음과 같이 지뢰가 매설된 경우를 보자.

1 2 5 4 3 3 6 6 2

첫 번째의 지뢰를 터트리게 되면 두 번째 지뢰에 1만큼의 힘을 발휘하게 된다. 만약 세 번째의 지뢰를 터뜨리게 되면 2, 4번째 지뢰에 5만큼의 힘을 발휘하게 된다. 따라서 2, 4번째 지뢰도 연쇄 반응을 일으키며 터지고, 다시 1번 지뢰에 2만큼의 힘을, 5번 지뢰에 4만큼의 힘을 발휘하여 연쇄 반응을 일으킨다. 그 후에는 6번 지뢰에 3만큼의 힘을 가하게 되고, 이는 3을 초과하는 힘이 아니기 때문에 연쇄 반응이 멈추게 된다. 정리하면, 세 번째의 지뢰를 직접 터트리고 나면 1~5번 지뢰가 모두 터지게 된다. 다음으로 7, 8번 지뢰를 각각 터트리면 모든 지뢰를 터트릴 수 있다.

지뢰를 직접 터트리는 것은 위험하기 때문에, 당신은 최소의 개수의 지뢰를 직접 터트려서 모든 지뢰를 터트리려 한다. 위의 예에서는 세 개의 지뢰를 직접 터트리면 연쇄 반응에 의해서 모든 지뢰를 터트릴 수 있다.

각 지뢰에 대한 정보가 주어졌을 때, 최소 개수의 지뢰를 직접 터트려서 모든 지뢰를 터트리고자 할 때, 직접 터트려야 하는 지뢰들을 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 N이 주어진다. 다음 N개의 지뢰는 차례대로 각 지뢰의 충격 강도 Pi가 주어진다.
### **출력**
직접 터트려야 하는 지뢰의 번호를 오름차순으로 출력한다.
### **예제입출력**

**예제 입력1**

```
9
1
2
5
4
3
3
6
6
2
```

**예제 출력1**

```
3
7
8
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N = int(input())

mine = [0]

for i in range(N)
    mine.append(int(input()))

mine.append(0)

for i in range(1, N+1):
    if mine[i] >= mine[i-1] and mine[i] >= mine[i+1]:
        print(i)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|32576|2032|Python3|190
#### **📝해설**

**알고리즘**
```
1. 그리디 알고리즘
```

### **다른 풀이**

```python
N = int(input())

mine = []
for _ in range(N):
    mine.append(int(input()))
    

result = []

for i in range(N):
    mine_max_idx = 0
    boom_list = []
    
    for j in range(N):
        if mine[mine_max_idx] < mine[j]:
            mine_max_idx = j
    
    if mine[mine_max_idx] == -1:
        break
    
    result.append(mine_max_idx+1)
    boom_list.append(mine_max_idx)
    left_idx = mine_max_idx - 1
    right_idx = mine_max_idx + 1
    
    while left_idx >= 0:
        if mine[left_idx] == -1:
            break
        if mine[left_idx] < mine[left_idx+1]:
            boom_list.append(left_idx)
            left_idx -= 1
        else:
            break

    while right_idx < N:
        if mine[right_idx] == -1:
            break
        if mine[right_idx] < mine[right_idx-1]:
            boom_list.append(right_idx)
            right_idx += 1
        else:
            break
    
    
    for idx in boom_list:
        mine[idx] = -1


result.sort()
for idx in result:
    print(idx)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
wkdgytmd200|114808|7140|PyPy3|1001
#### **📝해설**

```python
```

### **🔖정리**

1. 배운점