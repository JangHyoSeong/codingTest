# 봉인된 주문

## **📝문제 설명**
어느 날, 전설 속에 전해 내려오는 비밀 주문서가 세상에 다시 모습을 드러냈습니다. 이 주문서에는 마법 세계에서 사용되는 모든 주문이 적혀 있는데, 각 주문은 알파벳 소문자 11글자 이하로 구성되어 있습니다. 주문서에는 실제로 마법적 효과를 지니지 않는 의미 없는 주문들 즉, 알파벳 소문자 11글자 이하로 쓸 수 있는 모든 문자열이 고대의 규칙에 따라 아래와 같이 정렬되어 있습니다.

글자 수가 적은 주문부터 먼저 기록된다.
글자 수가 같다면, 사전 순서대로 기록된다.
예를 들어, 주문서의 시작 부분은 다음과 같이 구성됩니다.

- "a"→"b"→"c"→"d"→"e"→"f"→...→"z"
- →"aa"→"ab"→...→"az"→"ba"→...→"by"→"bz"→"ca"→...→"zz"
- →"aaa"→"aab"→...→"aaz"→"aba"→...→"azz"→"baa"→...→"zzz"
- →"aaaa"→...→"aazz"→"abaa"→...→"czzz"→"daaa"→...→"zzzz"
- →"aaaaa"→...  
하지만 이 주문서에는 오래전 봉인된 저주받은 주문들이 숨겨져 있었고, 이를 악용하려는 자들을 막기 위해 마법사들이 몇몇 주문을 주문서에서 삭제했습니다. 당신은 삭제가 완료된 주문서에서 n번째 주문을 찾아내야 합니다.

예를 들어, 주문서에서 "d", "e", "bb", "aa", "ae" 5개의 주문을 지웠을 때, 주문서에서 30번째 주문을 찾으려고 합니다.

- 1~3번째 주문은 "a", "b", "c" 입니다.
- "d"와 "e"는 삭제됐으므로 4~24번째 주문은 "f" ~ "z"입니다.
- "aa"는 삭제됐으므로 25~27번째 주문은 "ab", "ac", "ad"입니다.
- "ae"는 삭제됐으므로 28~30번째 주문은 "af", "ag", "ah"입니다.  
따라서 30번째 주문은 "ah"가 됩니다. 삭제된 주문 중 “bb”와 같이 n번째 주문보다 뒤에 위치해 있어서 n번째 주문을 찾는 데 영향을 주지 않는 주문도 존재할 수 있습니다.

정수 n과 삭제된 주문들을 담은 1차원 문자열 배열 bans가 매개변수로 주어질 때, 삭제가 완료된 주문서의 n번째 주문을 return 하도록 solution 함수를 완성해 주세요.
### **⚠제한사항**
- 1 ≤ n ≤ 1015
- 1 ≤ bans의 길이 ≤ 300,000
  - bans의 원소는 알파벳 소문자로만 이루어진 길이가 1 이상 11 이하인 문자열입니다.
  - bans의 원소는 중복되지 않습니다.
### **입출력 예**
n | bans | result
--|------|-------
30 | ["d", "e", "bb", "aa", "ae"] | "ah"
7388 | ["gqk", "kdn", "jxj", "jxi", "fug", "jxg", "ewq", "len", "bhc"] | "jxk"
## **🧐CODE REVIEW**

### **😫나의 오답 풀이**

### **🧾나의 풀이**

```python
def solution(n, bans):
    answer = ''
    bans.sort(key = lambda x : (len(x), x))
    for ban in bans:
        if str_to_num(ban) <= n:
            n += 1
    
    while n > 0:
        n -= 1
        answer += chr(n % 26 + ord("a"))
        n //= 26
    
    return answer[::-1]

def str_to_num(string):
    num = 0
    for i in range(len(string)-1, -1, -1):
        c = string[len(string)-i-1]
        c_to_num = ord(c) - ord("a") + 1
        num += c_to_num * (26 ** i)
    return num
```

#### **📝해설**

```python
def solution(n, bans):
    answer = ''
    # 봉인된 단어들을 길이순, 사전순으로 정렬
    bans.sort(key = lambda x : (len(x), x))

    # 만약 찾아야할 단어가 봉인된 주문보다 뒤에 있다면, 숫자를 1씩 더해서 뒤로 미룸
    for ban in bans:
        if str_to_num(ban) <= n:
            n += 1
    
    # 숫자를 다시 문자열로 되돌리는 과정
    while n > 0:
        # 1 : a ~~ 26 : z가 되어야함. 이를 위해 -1을 해줌
        # if a == 27 => "az"
        n -= 1
        
        # 문자로 변환
        answer += chr(n % 26 + ord("a"))
        n //= 26
    
    # 역순으로 출력
    return answer[::-1]

# 문자열을 숫자로 변환
def str_to_num(string):
    num = 0
    for i in range(len(string)-1, -1, -1):
        c = string[len(string)-i-1]
        c_to_num = ord(c) - ord("a") + 1
        num += c_to_num * (26 ** i)
    return num
```

## 📚참고 사이트

- **🔗문제 링크**<br/>
https://school.programmers.co.kr/learn/courses/30/lessons/389481