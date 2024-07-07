# [30805] 사전 순 최대 공통 부분

### **난이도**
골드4
## **📝문제**
어떤 수열이 다른 수열의 부분 수열이라는 것은 다음을 의미합니다.

- 해당 수열의 원소들이 다른 수열 내에서 순서대로 등장합니다.
- 예를 들어, 
$\{1,1,5\}$는 $\{3,\underline{\color{blue} 1} ,4,\underline{\color{blue} 1} ,\underline{\color{blue} 5} ,9\}$의 부분 수열이지만, $\{1,5,1\}$의 부분 수열은 아닙니다.  

또한, 어떤 수열이 다른 수열보다 사전 순으로 나중이라는 것은 다음을 의미합니다.

- 두 수열 중 첫 번째 수가 큰 쪽은 사전 순으로 나중입니다.
- 두 수열의 첫 번째 수가 같다면, 첫 번째 수를 빼고 두 수열을 다시 비교했을 때 사전 순으로 나중인 쪽이 사전 순으로 나중입니다.
- 길이가 $0$인 수열과 다른 수열을 비교하면, 다른 수열이 사전 순으로 나중입니다.
 
양의 정수로 이루어진 길이가 $N$인 수열 $\{A_1,\cdots ,A_N\}$이 주어집니다. 마찬가지로 양의 정수로 이루어진 길이가 $M$인 수열 $\{B_1,\cdots ,B_M\}$이 주어집니다.

수열 $A$와 수열 $B$가 공통으로 갖는 부분 수열들 중 사전 순으로 가장 나중인 것을 구하세요.
### **입력**
첫 줄에 수열 $A$의 길이 $N$이 주어집니다. $(1 \le N \le 100)$ 

둘째 줄에 $N$개의 양의 정수 $A_1,A_2,\cdots,A_N$이 주어집니다. $(1 \le A_i \le 100)$ 

셋째 줄에 수열 $B$의 길이 $M$이 주어집니다. $(1 \le M \le 100)$ 

넷째 줄에 $M$개의 양의 정수 $B_1,B_2,\cdots,B_M$이 주어집니다. $(1 \le B_i \le 100)$ 
### **출력**
$A$와 $B$의 공통 부분 수열 중 사전 순으로 가장 나중인 수열의 크기 $K$를 출력하세요.

$K \ne 0$이라면, 다음 줄에 $K$개의 수를 공백으로 구분해 출력하세요. $i$번째 수는 $A$와 $B$의 공통 부분 수열 중 사전 순으로 가장 나중인 수열의 $i$번째 수입니다.
### **예제입출력**

**예제 입력1**

```
4
1 9 7 3
5
1 8 7 5 3
```

**예제 출력1**

```
2
7 3
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

flag = True
ans = []

while True:
    while True:
        if len(a) == 0 or len(b) == 0:
            flag = False
            break
        max_a = max(a)
        a_idx = a.index(max_a)
        max_b = max(b)
        b_idx = b.index(max_b)
        if max_a == max_b:
            break
        elif max_a > max_b:
            a.pop(a_idx)
        else:
            b.pop(b_idx)
    
    if not flag:
        break
    
    ans.append(max_a)
    
    a = a[a_idx+1:]
    b = b[b_idx+1:]

if ans:
    print(len(ans))
    print(" ".join(map(str, ans)))
else:
    print(0)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|31120|40|Python3|817
#### **📝해설**

**알고리즘**
```
1. 그리디 알고리즘
```

### **다른 풀이**

```python
input()
A = list(map(int, input().split()))
input()
B = list(map(int, input().split()))
mx = max(max(B), max(B))

res = []
for i in range(mx, 0, -1):
    while 1:
        if i not in A or i not in B:
            break
        res.append(i)
        A = A[A.index(i)+1:]
        B = B[B.index(i)+1:]

print(len(res))
print(*res, sep=' ')
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
laksj113|31120|40|Python3|335