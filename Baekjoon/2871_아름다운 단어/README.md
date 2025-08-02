# [2871] 아름다운 단어

### **난이도**
골드 2
## **📝문제**
상근이는 희원이와 놀기 위해 집에서 게임을 준비해 왔다. 한 종이에 한 글자씩 쓰여 있고, 이러한 종이 N개가 한 줄로 놓여져 있다. 두 사람 각각은 이 종이를 모아서 단어를 만들려고 한다. 각 사람은 턴을 번갈아가면서 종이 한 장을 가져가고 자기 단어의 뒤쪽에 붙인다. 상근이가 게임을 먼저 하고, 더 이상 가져갈 종이가 없으면 게임을 종료한다.

두 단어 A와 B가 있을때, A가 B보다 사전순으로 앞선다면, A는 B보다 아름답다. 두 사람이 각자 만든 단어 중에서 더 아름다운 단어를 만든 사람이 게임을 이긴다. 만약 두 사람이 같은 단어를 만들었다면 둘 다 진다.

상근이는 이 게임을 엄청나게 잘하지만, 희원이는 아직 규칙도 헷갈리는 상황이다. 따라서, 상근이는 희원이를 위해 조금 다르게 게임을 하려고 한다. 상근이는 항상 가장 오른쪽에 있는 종이를 집어간다. 희원이가 이 사실을 알고 있을 때, 희원이가 상근이를 이길 수 있는지 구하고, 만들 수 있는 가장 아름다운 단어를 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 짝수 N이 주어진다. (2 ≤ N ≤ 100 000)

둘째 줄에 종이에 적혀 있는 글자가 순서대로 주어진다. 글자는 모두 알파벳 소문자이다.
### **출력**
만약, 희원이가 이길 수 있다면 첫째 줄에 "DA"를, 없다면 "NE"를 출력한다. 둘째 줄에는 희원이가 만들 수 있는 가장 아름다운 단어를 출력한다.
### **예제입출력**

**예제 입력1**

```
2
ne
```

**예제 출력1**

```
NE
n
```

**예제 입력2**

```
4
kava
```

**예제 출력2**

```
DA
ak
```

**예제 입력3**

```
8
cokolada
```

**예제 출력3**

```
DA
acko
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys
from heapq import heappush, heappop

N = int(sys.stdin.readline().rstrip())
word = sys.stdin.readline().rstrip()

used = [False] * N
pq = []

for i in range(N):
    heappush(pq, (word[i], -i))

sang = []
hee = []

right = N-1
for turn in range(N):
    if turn % 2 == 0:
        while used[right]:
            right -= 1
        
        sang.append(word[right])
        used[right] = True
    
    else:
        while pq:
            char, idx = heappop(pq)
            if not used[-idx]:
                hee.append(char)
                used[-idx] = True
                break

            
hee_word = "".join(map(str, hee))
sang_word = "".join(map(str, sang))

print("DA" if hee_word < sang_word else "NE")
print(hee_word)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|131712|380|PyPy3|735
#### **📝해설**

**알고리즘**
```
1. 그리디 알고리즘
```

### **다른 풀이**

```python
import sys
input = sys.stdin.readline

def main():
    N = int(input())
    letters = input().strip()
    asort = sorted(range(N), key=lambda n: (letters[n],-n))
    used = [False]*N
    opt_sol = ['a']*(N>>1)
    ptr_a = N-1
    ptr_b = 0
    wins_determined = False
    wins_b = False
    for n in range(N>>1):
        while used[ptr_a]:
            ptr_a -= 1
        used[ptr_a] = True
        ch_a = letters[ptr_a]
        while used[asort[ptr_b]]:
            ptr_b += 1
        used[asort[ptr_b]] = True
        ch_b = letters[asort[ptr_b]]
        opt_sol[n] = ch_b
        if (not wins_determined) and (ch_a > ch_b):
            wins_determined = True
            wins_b = True
        elif (not wins_determined) and (ch_a < ch_b):
            wins_determined = True
    print('DA' if wins_b else 'NE')
    print(''.join(opt_sol))

if __name__ == '__main__':
    main()
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
sinwall|48072|112|Python3|878
#### **📝해설**

```python
import sys
from heapq import heappush, heappop

N = int(sys.stdin.readline().rstrip())
word = sys.stdin.readline().rstrip()

# 단어 사용 여부를 저장할 리스트
used = [False] * N

# 우선순위 큐를 통해 사전순, 인덱스 역순으로 정렬
pq = []

# 우선순위 큐에 삽입
for i in range(N):

    # 인덱스는 뒤에서부터 뽑는게 유리함.(상근이가 뒤에서부터 뽑으니까)
    heappush(pq, (word[i], -i))

sang = []
hee = []

# 상근이의 인덱스
right = N-1

# N번 반복하면서
for turn in range(N):

    # 상근이 차례일 때는
    if turn % 2 == 0:

        # 사용한 단어라면 건너뜀
        while used[right]:
            right -= 1
        
        # 사용하지 않은 단어라면 사용
        sang.append(word[right])
        used[right] = True
    
    # 희원이 차례라면
    else:

        # 우선순위 큐에서 뽑아냄
        while pq:

            # 사전순으로 가장 작고, 인덱스가 뒤쪽인 단어
            char, idx = heappop(pq)

            # 사용하지 않았던 단어라면 사용
            if not used[-idx]:
                hee.append(char)
                used[-idx] = True
                break

            # 아니라면 pop

            
hee_word = "".join(map(str, hee))
sang_word = "".join(map(str, sang))

print("DA" if hee_word < sang_word else "NE")
print(hee_word)
```