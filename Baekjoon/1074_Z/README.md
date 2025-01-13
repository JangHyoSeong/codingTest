# [1074] Z

### **난이도**
골드 5
## **📝문제**
한수는 크기가 2N × 2N인 2차원 배열을 Z모양으로 탐색하려고 한다. 예를 들어, 2×2배열을 왼쪽 위칸, 오른쪽 위칸, 왼쪽 아래칸, 오른쪽 아래칸 순서대로 방문하면 Z모양이다.

![이미지](https://u.acmicpc.net/21c73b56-5a91-43aa-b71f-9b74925c0adc/Screen%20Shot%202020-12-02%20at%208.09.46%20AM.png)

N > 1인 경우, 배열을 크기가 2N-1 × 2N-1로 4등분 한 후에 재귀적으로 순서대로 방문한다.

다음 예는 22 × 22 크기의 배열을 방문한 순서이다.

![이미지](https://u.acmicpc.net/adc7cfae-e84d-4d5c-af8e-ee011f8fff8f/Screen%20Shot%202020-12-02%20at%208.11.17%20AM.png)

N이 주어졌을 때, r행 c열을 몇 번째로 방문하는지 출력하는 프로그램을 작성하시오.

다음은 N=3일 때의 예이다.
![이미지](https://u.acmicpc.net/d3e84bb7-9424-4764-ad3a-811e7fcbd53f/Screen%20Shot%202020-12-30%20at%2010.50.47%20PM.png)

### **입력**
첫째 줄에 정수 N, r, c가 주어진다.
### **출력**
r행 c열을 몇 번째로 방문했는지 출력한다.
### **예제입출력**

**예제 입력1**

```
2 3 1
```

**예제 출력1**

```
11
```

**예제 입력2**

```
3 7 7
```

**예제 출력2**

```
63
```

**예제 입력3**

```
1 0 0
```

**예제 출력3**

```
0
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N, r, c = map(int, input().split())

result = 0
size = 2 ** (N-1)

while N > 0:

    if r < size and c < size:
        pass

    elif r < size and c >= size:
        result += size * size
        c -= size

    elif r >= size and c < size:
        result += 2 * size * size
        r -= size
    
    else:
        result += 3 * size * size
        r -= size
        c -= size

    size //= 2
    N -= 1

print(result)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|32412|44|Python3|418
#### **📝해설**

**알고리즘**
```
1. 분할 정복
```

### **다른 풀이**

```python
n, r, c = map(int, input().split())
r+=1
c+=1
n=2**n
x=0
while n>1:
    n*=0.5
    q=(1 if r<=n else 3)+(0 if c<=n else 1)
    x+=n**2*(q-1)
    r-=n if n<r else 0
    c-=n if n<c else 0
print(int(x))
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
starjh2001|30616|32|Python3|201
#### **📝해설**

```python
N, r, c = map(int, input().split())

# 초기 결과값과 크기
result = 0
size = 2 ** (N-1)

# 더 분할할 수 없을때까지 반복
while N > 0:

    # 1사분면에 존재한다면 넘어감
    if r < size and c < size:
        pass

    # 2사분면에 존재한다면
    elif r < size and c >= size:
        result += size * size
        c -= size

    # 3사분면에 존재한다면
    elif r >= size and c < size:
        result += 2 * size * size
        r -= size
    
    # 4사분면에 존재한다면
    else:
        result += 3 * size * size
        r -= size
        c -= size

    # 더 작은 단위로 넘어감
    size //= 2
    N -= 1

print(result)
```