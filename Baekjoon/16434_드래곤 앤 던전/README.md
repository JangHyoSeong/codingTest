# [16434] 드래곤 앤 던전

### **난이도**
골드 4
## **📝문제**
용사는 공주를 구하기 위해 무시무시한 용이 있는 던전으로 향하기로 하였습니다. 우선 용사는 용사 자신과 던전을 분석하였습니다.

용사에게는 세 종류의 능력치가 있습니다. 

HMaxHP : 용사의 최대 생명력입니다. 이 값은 1이상이어야 하며 던전에 들어간 이후로 변하지 않습니다.
HCurHP : 현재 용사의 생명력입니다. 던전에 들어가기 전 이 값은 용사의 최대 생명력 HMaxHP와 같습니다. 이 값은 HMaxHP보다 커질 수 없습니다.
HATK : 용사의 공격력입니다.
던전은 총 N개의 방으로 이루어져 있고 i번째 방을 통해서만 i+1번째 방으로 이동 할 수 있습니다. 방에는 포션이 있거나 몬스터가 있는데 몬스터가 있을 경우 몬스터를 쓰러트려야지 다음방으로 이동 할 수 있습니다. N번째 방에는 공주와 용이 있고, 용을 무찌르면 공주를 구할 수 있습니다.

몬스터가 있는 방에 올 경우 다음과 같이 전투가 진행됩니다.

용사의 공격력 HATK만큼 몬스터의 생명력을 깎습니다.
몬스터의 생명력이 0 이하이면 전투가 종료되고 용사는 다음 방으로 이동합니다.
몬스터의 공격력만큼 용사의 생명력 HCurHP를 깎습니다.
용사의 생명력이 0 이하이면 전투가 종료되고 용사는 사망합니다.
다시 1부터 진행합니다.
포션이 있는 방에 올 경우 포션을 마셔서 현재 용사의 생명력 HCurHP가 일정량 회복되고 공격력 HATK도 일정량만큼 증가됩니다. 회복된 생명력이 최대 생명력 HMaxHP보다 큰 경우 용사의 현재 생명력 HCurHP가 최대 생명력 HMaxHP와 같아집니다.

용사는 던전으로 향하기 전에 만반의 준비를 하고 있습니다. 용사는 수련을 하면 최대 생명력 HMaxHP를 늘릴 수 있는데 얼마나 수련해야 할지 고민입니다.

용사는 N번 방에 있는 용을 쓰러트리기 위한 최소의 HMaxHP를 여러분이 계산해주면 좋겠다고 합니다.
### **입력**
첫 번째 줄에 방의 개수 N (1 ≤ N  ≤ 123,456) 과 용사의 초기 공격력 HATK (1 ≤ HATK  ≤ 1,000,000) 가 주어집니다.

i+1번째 줄엔 i번째 방의 정보를 나타내는 세개의 정수 ti, ai, hi (ti ∈ {1, 2}, 1 ≤ ai, hi  ≤ 1,000,000) 가 주어집니다. 

ti가 1인 경우 공격력이 ai이고 생명력이 hi인 몬스터가 있음을 나타내고, ti가 2인 경우 용사의 공격력 HATK를 ai만큼 증가시켜주고 용사의 현재 생명력 HCurHP를 hi만큼 회복시켜주는 포션이 있음을 나타냅니다.
### **출력**

### **예제입출력**

**예제 입력1**

```
3 3
1 1 20
2 3 10
1 3 100
```

**예제 출력1**

```
49
```

**예제 입력2**

```
1 1
1 1000000 1000000
```

**예제 출력2**

```
999999000001
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N, atk = map(int, input().split())
rooms = [list(map(int, input().split())) for _ in range(N)]

now_hp = 0
min_hp = 0

for room in rooms:
    if room[0] == 1:
        count = room[2] // atk
        rest = room[2] % atk

        if rest:
            atk_count = count
        else:
            atk_count = count-1

        now_hp -= (atk_count) * room[1]
        min_hp = min(now_hp, 0, min_hp)
        
    else:
        now_hp = min(room[2]+now_hp, 0)
        atk += room[1]

print(-min_hp+1)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|123568|224|PyPy3|494
#### **📝해설**

**알고리즘**
```
1. 구현
```

### **다른 풀이**

```python
import sys
input = sys.stdin.readline

N, Ha = map(int, input().split()) # N : 방의 개수, Ha : 용사 초기 공격력

dmg = 0
DMG = 0
for _ in range(N):
    t, a, h = map(int, input().split()) # t = 1: 몬스터, t = 2: 포션
    if t == 1: # 공격력 a, 생명력 h인 몬스터
        k = (h // Ha)
        if h % Ha:
            k += 1
        dmg += (k - 1) * a
        DMG = max(DMG, dmg)

    else: # 공격력Ha를 a만큼, 생명력Hc를 h만큼 회복 시켜 주는 포션
        Ha += a
        dmg = max(0, dmg - h)

print(DMG+1)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
hyem|110592|140|PyPy3|550
#### **📝해설**

```python
N, atk = map(int, input().split())
rooms = [list(map(int, input().split())) for _ in range(N)]

# 현재체력, 필요한 최소체력
now_hp = 0
min_hp = 0

# 방을 순회하면서
for room in rooms:

  # 전투방이라면
    if room[0] == 1:

      # 공격 횟수를 구함
        count = room[2] // atk
        rest = room[2] % atk

        # 나머지가 있다면, 몬스터의 공격횟수는 몫
        if rest:
            atk_count = count

        # 나머지가 없이 딱맞아떨어진다면, 몬스터의 공격횟수는 몫-1
        else:
            atk_count = count-1

        # 현재 체력을 깎음 (음수)
        now_hp -= (atk_count) * room[1]

        # 필요한 최소체력을 갱신함
        min_hp = min(now_hp, 0, min_hp)
    
    # 회복방이라면
    else:
      # 체력을 0까지 회복시킴
        now_hp = min(room[2]+now_hp, 0)
        atk += room[1]

print(-min_hp+1)
```