# [1043] 거짓말

### **난이도**
골드 4
## **📝문제**
지민이는 파티에 가서 이야기 하는 것을 좋아한다. 파티에 갈 때마다, 지민이는 지민이가 가장 좋아하는 이야기를 한다. 지민이는 그 이야기를 말할 때, 있는 그대로 진실로 말하거나 엄청나게 과장해서 말한다. 당연히 과장해서 이야기하는 것이 훨씬 더 재미있기 때문에, 되도록이면 과장해서 이야기하려고 한다. 하지만, 지민이는 거짓말쟁이로 알려지기는 싫어한다. 문제는 몇몇 사람들은 그 이야기의 진실을 안다는 것이다. 따라서 이런 사람들이 파티에 왔을 때는, 지민이는 진실을 이야기할 수 밖에 없다. 당연히, 어떤 사람이 어떤 파티에서는 진실을 듣고, 또다른 파티에서는 과장된 이야기를 들었을 때도 지민이는 거짓말쟁이로 알려지게 된다. 지민이는 이런 일을 모두 피해야 한다.

사람의 수 N이 주어진다. 그리고 그 이야기의 진실을 아는 사람이 주어진다. 그리고 각 파티에 오는 사람들의 번호가 주어진다. 지민이는 모든 파티에 참가해야 한다. 이때, 지민이가 거짓말쟁이로 알려지지 않으면서, 과장된 이야기를 할 수 있는 파티 개수의 최댓값을 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 사람의 수 N과 파티의 수 M이 주어진다.

둘째 줄에는 이야기의 진실을 아는 사람의 수와 번호가 주어진다. 진실을 아는 사람의 수가 먼저 주어지고 그 개수만큼 사람들의 번호가 주어진다. 사람들의 번호는 1부터 N까지의 수로 주어진다.

셋째 줄부터 M개의 줄에는 각 파티마다 오는 사람의 수와 번호가 같은 방식으로 주어진다.

N, M은 50 이하의 자연수이고, 진실을 아는 사람의 수는 0 이상 50 이하의 정수, 각 파티마다 오는 사람의 수는 1 이상 50 이하의 정수이다.
### **출력**
첫째 줄에 문제의 정답을 출력한다.
### **예제입출력**

**예제 입력1**

```
4 3
0
2 1 2
1 3
3 2 3 4
```

**예제 출력1**

```
3
```

**예제 입력2**

```
4 1
1 1
4 1 2 3 4
```

**예제 출력2**

```
0
```

**예제 입력3**

```
4 5
1 1
1 1
1 2
1 3
1 4
2 4 1
```

**예제 출력3**

```
2
```

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N, M = map(int, input().split())
truth_num, *truth = map(int, input().split())

parties = [list(map(int, input().split())) for _ in range(M)]

representive = [i for i in range(N+1)]

def find_set(x):
    if representive[x] == x:
        return x

    return find_set(representive[x])

def union(x, y):

    x = find_set(x)
    y = find_set(y)
    

    if x != y:
        if y in truth:
            representive[x] = y
        else:
            representive[y] = x

    return

for party in parties:
    party_people = party[0]

    for i in range(1, party_people):
        union(party[i], party[i+1])

result = 0

for party in parties:
    party_people = party[0]
    for i in range(1, party_people+1):
        if find_set(party[i]) in truth:
            break
    else:
        result += 1

print(result)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|31120|44|Python3|806
#### **📝해설**

**알고리즘**
```
1. union find
```

### **다른 풀이**

```python
import sys
input = sys.stdin.readline


mens,party =list(map(int,input().split()))
cnt =0

story = set(input().split()[1:])
rounge = []
for i in range(party):
    rounge.append(set(input().split()[1:]))
    
for _ in range(party):
    for j in rounge:
        if j & story:#합집합
            story = story.union(j)

for j in rounge:
    if j & story:
        continue
    cnt +=1
print(cnt)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
kdg123|30616|36|Python3|394
#### **📝해설**

```python
N, M = map(int, input().split())

# 진실을 아는 사람과, 그 사람들을 따로 저장
truth_num, *truth = map(int, input().split())

parties = [list(map(int, input().split())) for _ in range(M)]

# union-find를 위한 리스트 선언. 각 인덱스의 값은 그 집합에서 진실을 아는 사람
representive = [i for i in range(N+1)]

def find_set(x):
    # union find의 대표자를 찾는 함수

    # 대표자가 본인이라면 리턴, 아니라면 대표자의 인덱스로 이동해서 그 값을 리턴
    if representive[x] == x:
        return x

    return find_set(representive[x])

def union(x, y):
    # unionfind에서 원소를 추가하는 과정
    x = find_set(x)
    y = find_set(y)
    
    # x, y의 대표자가 같지 않은 경우 (다른 집합인 경우)
    if x != y:
        # y가 진실을 안다면, y가 대표자
        if y in truth:
            representive[x] = y
        
        # x가 진실을 안다면, x가 대표자
        else:
            representive[y] = x

    return

# 모든 파티를 순회하면서
for party in parties:
    party_people = party[0]

    # 그 파티의 참석자들을 union find로 합쳐줌
    for i in range(1, party_people):
        union(party[i], party[i+1])

# 정답으로 사용할 변수
result = 0

# 다시 파티를 순회하면서
for party in parties:
    party_people = party[0]

    # 현재 파티의 참석자중에, 그 참석자의 집합에서 진실을 아는 사람이 있다면
    # break
    for i in range(1, party_people+1):
        if find_set(party[i]) in truth:
            break

    # 집합에서 진실을 아는 사람이 아무도 없다면 +1
    else:
        result += 1

print(result)
```