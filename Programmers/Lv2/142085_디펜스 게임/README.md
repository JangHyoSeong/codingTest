# 문제 제목
디펜스 게임
## **📝문제 설명**
문제 설명
준호는 요즘 디펜스 게임에 푹 빠져 있습니다. 디펜스 게임은 준호가 보유한 병사 n명으로 연속되는 적의 공격을 순서대로 막는 게임입니다. 디펜스 게임은 다음과 같은 규칙으로 진행됩니다.

- 준호는 처음에 병사 n명을 가지고 있습니다.
- 매 라운드마다 enemy[i]마리의 적이 등장합니다.
- 남은 병사 중 enemy[i]명 만큼 소모하여 enemy[i]마리의 적을 막을 수 있습니다.
  - 예를 들어 남은 병사가 7명이고, 적의 수가 2마리인 경우, 현재 라운드를 막으면 7 - 2 = 5명의 병사가 남습니다.
  - 남은 병사의 수보다 현재 라운드의 적의 수가 더 많으면 게임이 종료됩니다.
- 게임에는 무적권이라는 스킬이 있으며, 무적권을 사용하면 병사의 소모없이 한 라운드의 공격을 막을 수 있습니다.
- 무적권은 최대 k번 사용할 수 있습니다.

준호는 무적권을 적절한 시기에 사용하여 최대한 많은 라운드를 진행하고 싶습니다.

준호가 처음 가지고 있는 병사의 수 n, 사용 가능한 무적권의 횟수 k, 매 라운드마다 공격해오는 적의 수가 순서대로 담긴 정수 배열 enemy가 매개변수로 주어집니다. 준호가 몇 라운드까지 막을 수 있는지 return 하도록 solution 함수를 완성해주세요.
### **⚠제한사항**
- 1 ≤ n ≤ 1,000,000,000
- 1 ≤ k ≤ 500,000
- 1 ≤ enemy의 길이 ≤ 1,000,000
- 1 ≤ enemy[i] ≤ 1,000,000
- enemy[i]에는 i + 1 라운드에서 공격해오는 적의 수가 담겨있습니다.
- 모든 라운드를 막을 수 있는 경우에는 enemy[i]의 길이를 return 해주세요.
### **입출력 예**
n | k | enemy | result
--|---|-------|-------
7 | 3 | [4, 2, 4, 5, 3, 3, 1] | 5
2 | 4 | [3, 3, 3, 3] | 4
## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from heapq import heappush, heappop

def solution(n, k, enemy):
    pq = []
    total = 0
    
    round_len = len(enemy)
    for i in range(round_len):
        heappush(pq, -enemy[i])
        total += enemy[i]
        
        if total > n:
            if k > 0:
                total += heappop(pq)
                k -= 1
            else:
                return i
    
    return round_len
```

#### **📝해설**

```python
from heapq import heappush, heappop

def solution(n, k, enemy):

    # 우선순위 큐를 통해 무적권 사용 판별
    pq = []
    total = 0
    
    round_len = len(enemy)

    # 라운드를 순회
    for i in range(round_len):

        # 우선순위 큐에 적 삽입(최대 힙)
        heappush(pq, -enemy[i])

        # 적의 수를 더함
        total += enemy[i]
        
        # 만약 적이 병사보다 많다면
        if total > n:
            # 무적권을 사용할 수 있다면
            if k > 0:

                # 가장 병사가 많았던 적에게 무적권 사용
                total += heappop(pq)
                k -= 1
            
            # 무적권을 사용할 수 없다면 종료
            else:
                return i
    
    # 게임이 끝났다면 마지막라운드를 리턴
    return round_len
```