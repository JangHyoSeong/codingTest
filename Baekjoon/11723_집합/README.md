# [11723] 집합

### **난이도**
실버 5
## **📝문제**
문제
비어있는 공집합 S가 주어졌을 때, 아래 연산을 수행하는 프로그램을 작성하시오.

- add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
- remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
- check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
- toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
- all: S를 {1, 2, ..., 20} 으로 바꾼다.
- empty: S를 공집합으로 바꾼다.
### **입력**
첫째 줄에 수행해야 하는 연산의 수 M (1 ≤ M ≤ 3,000,000)이 주어진다.

둘째 줄부터 M개의 줄에 수행해야 하는 연산이 한 줄에 하나씩 주어진다.
### **출력**
check 연산이 주어질때마다, 결과를 출력한다.
### **예제입출력**

**예제 입력1**

```
26
add 1
add 2
check 1
check 2
check 3
remove 2
check 1
check 2
toggle 3
check 1
check 2
check 3
check 4
all
check 10
check 20
toggle 10
remove 20
check 10
check 20
empty
check 1
toggle 1
check 1
toggle 1
check 1
```

**예제 출력1**

```
1
1
0
1
0
1
0
1
0
1
1
0
0
0
1
0
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
import sys

M = int(sys.stdin.readline().rstrip())

s = set()
for _ in range(M):
    data = sys.stdin.readline().rstrip()
    if data == "all":
        s = set(range(1, 21))
    
    elif data == "empty":
        s = set()
    
    else:
        op, num = data.split()

        num = int(num)
        if op == "add":
            s.add(num)
        
        elif op == "remove":
            if num in s:
                s.remove(num)
        
        elif op == "check":
            if num in s:
                print(1)
            else:
                print(0)
        
        elif op == "toggle":
            if num in s:
                s.remove(num)
            else:
                s.add(num)
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|128836|1616|PyPy3|700
#### **📝해설**

**알고리즘**
```
1. 집합
```

### **다른 풀이**

```python
def main():
	import io
	import os
	from array import array

	reader = io.BufferedReader(io.FileIO(0), 1 << 18)
	M = int(reader.readline())
	S = 0
	stdout = M * array("H", [0x0A30])
	i = 0
	for _ in range(M):
		line = reader.readline()
		L = len(line)
		match line[1]:
			case 104:
				# check
				if L == 9:
					stdout[i] |= (S >> ((line[6] - 48) * 10 + line[7] - 49)) & 1
				else:
					stdout[i] |= (S >> (line[6] - 49)) & 1
				i += 1
			case 100:
				# add
				if L == 7:
					S |= 1 << ((line[4] - 48) * 10 + line[5] - 49)
				else:
					S |= 1 << (line[4] - 49)
			case 101:
				# remove
				if L == 10:
					S &= 1048575 - (1 << ((line[7] - 48) * 10 + line[8] - 49))
				else:
					S &= 1048575 - (1 << (line[7] - 49))
			case 108:
				# all
				S = 1048575
			case 109:
				# empty
				S = 0
			case _:
				# toggle
				if L == 10:
					S ^= 1 << ((line[7] - 48) * 10 + line[8] - 49)
				else:
					S ^= 1 << (line[7] - 49)
	del stdout[i:]
	os.write(1, stdout)
	os._exit(0)


main()
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
kiwiyou|122520|212|PyPy3|992