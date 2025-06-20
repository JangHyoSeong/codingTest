# [9375] 패션왕 신해빈

### **난이도**
실버 3
## **📝문제**
해빈이는 패션에 매우 민감해서 한번 입었던 옷들의 조합을 절대 다시 입지 않는다. 예를 들어 오늘 해빈이가 안경, 코트, 상의, 신발을 입었다면, 다음날은 바지를 추가로 입거나 안경대신 렌즈를 착용하거나 해야한다. 해빈이가 가진 의상들이 주어졌을때 과연 해빈이는 알몸이 아닌 상태로 며칠동안 밖에 돌아다닐 수 있을까?
### **입력**
첫째 줄에 테스트 케이스가 주어진다. 테스트 케이스는 최대 100이다.

- 각 테스트 케이스의 첫째 줄에는 해빈이가 가진 의상의 수 n(0 ≤ n ≤ 30)이 주어진다.
- 다음 n개에는 해빈이가 가진 의상의 이름과 의상의 종류가 공백으로 구분되어 주어진다. 같은 종류의 의상은 하나만 입을 수 있다.  
모든 문자열은 1이상 20이하의 알파벳 소문자로 이루어져있으며 같은 이름을 가진 의상은 존재하지 않는다.
### **출력**
각 테스트 케이스에 대해 해빈이가 알몸이 아닌 상태로 의상을 입을 수 있는 경우를 출력하시오.
### **예제입출력**

**예제 입력1**

```
2
3
hat headgear
sunglasses eyewear
turban headgear
3
mask face
sunglasses face
makeup face
```

**예제 출력1**

```
5
3
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
T = int(input())
for testcase in range(T):
    N = int(input())
    clothes_dict = {}

    type_set = set()
    for _ in range(N):
        name, clothes = input().split()
        type_set.add(clothes)
        if clothes_dict.get(clothes) is None:
            clothes_dict[clothes] = {name}
        else:
            clothes_dict[clothes].add(name)

    count = 1
    for type in type_set:
        count *= len(clothes_dict[type]) + 1
    
    print(count - 1)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|32412|48|Python3|459
#### **📝해설**

**알고리즘**
```
1. 집합
2. 조합
```

### **다른 풀이**

```python
import sys
input = lambda : sys.stdin.readline().strip()

t = int(input())
for _ in range(t):
    n = int(input())
    d={}
    for __ in range(n):
        a,b = input().split()
        if b in d:
            d[b]+=1
        else:
            d[b]=1
    k=1
    for i in d:
        k=k*(d[i]+1)
    print(k-1)
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
polaris_unreal|31120|28|Python3|309
#### **📝해설**

```python
T = int(input())
for testcase in range(T):
    N = int(input())

    # 옷 종류에 대해서 어떤 옷을 갖고 있는지 저장할 딕셔너리
    clothes_dict = {}

    # 옷의 타입이 어떤것이 있는지 저장할 set
    type_set = set()

    # 입력받기
    for _ in range(N):
        name, clothes = input().split()

        # type을 추가(중복 제거)
        type_set.add(clothes)

        # 입력받은 적이 없던 타입이라면
        if clothes_dict.get(clothes) is None:

            # set로 그 타입의 옷을 저장
            clothes_dict[clothes] = {name}

        # set에 추가
        else:
            clothes_dict[clothes].add(name)

    # 모든 타입을 검사하면서
    count = 1

    # 조합의 개수를 찾기 위해 곱함
    for type in type_set:
        count *= len(clothes_dict[type]) + 1
    
    # 옷을 아예 안입는 경우는 제외하기 위해 -1
    print(count - 1)
```