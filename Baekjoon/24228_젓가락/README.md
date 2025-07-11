# [24228] 젓가락

### **난이도**
실버 5
## **📝문제**
젓가락통에 
$N$ 종류의 젓가락이 종류별로 충분히 많이 들어있다. 당신은 이 젓가락통에서 무작위로 젓가락을 뽑아서 
$R$개의 짝을 맞춰야 한다. 최악의 경우 몇 개의 젓가락을 뽑아야 하는가?
### **입력**
두 개의 정수 
$N, R$이 주어진다. 
$(1 ≤ N,R ≤ 10^{18})$ 
### **출력**
최악의 경우 뽑아야 하는 젓가락의 개수를 출력한다.
### **예제입출력**

**예제 입력1**

```
2 1
```

**예제 출력1**

```
3
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
N, R = map(int, input().split())
print(2 * R + N - 1)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|32412|36|Python3|53
#### **📝해설**

**알고리즘**
```
1. 비둘기 집 원리
```

#### **😅개선점**

1. `for i in range():` 

여기서 어쩌구 했으면 더 좋았겠다

#### **📝해설**

```python
N, R = map(int, input().split())
print(2 * R + N - 1)

'''
N-1개는 서로 다른 종류로 뽑을 수 있음
R쌍을 만들기 위해서 최소 2R개 젓가락이 필요
따라서 최악의 경우 2*R + N-1
'''
```