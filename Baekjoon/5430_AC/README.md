# [5430] AC

### **난이도**
골드 5
## **📝문제**
선영이는 주말에 할 일이 없어서 새로운 언어 AC를 만들었다. AC는 정수 배열에 연산을 하기 위해 만든 언어이다. 이 언어에는 두 가지 함수 R(뒤집기)과 D(버리기)가 있다.

함수 R은 배열에 있는 수의 순서를 뒤집는 함수이고, D는 첫 번째 수를 버리는 함수이다. 배열이 비어있는데 D를 사용한 경우에는 에러가 발생한다.

함수는 조합해서 한 번에 사용할 수 있다. 예를 들어, "AB"는 A를 수행한 다음에 바로 이어서 B를 수행하는 함수이다. 예를 들어, "RDD"는 배열을 뒤집은 다음 처음 두 수를 버리는 함수이다.

배열의 초기값과 수행할 함수가 주어졌을 때, 최종 결과를 구하는 프로그램을 작성하시오.
### **입력**
첫째 줄에 테스트 케이스의 개수 T가 주어진다. T는 최대 100이다.

각 테스트 케이스의 첫째 줄에는 수행할 함수 p가 주어진다. p의 길이는 1보다 크거나 같고, 100,000보다 작거나 같다.

다음 줄에는 배열에 들어있는 수의 개수 n이 주어진다. (0 ≤ n ≤ 100,000)

다음 줄에는 [x1,...,xn]과 같은 형태로 배열에 들어있는 정수가 주어진다. (1 ≤ xi ≤ 100)

전체 테스트 케이스에 주어지는 p의 길이의 합과 n의 합은 70만을 넘지 않는다.
### **출력**
각 테스트 케이스에 대해서, 입력으로 주어진 정수 배열에 함수를 수행한 결과를 출력한다. 만약, 에러가 발생한 경우에는 error를 출력한다.
### **예제입출력**

**예제 입력1**

```
4
RDD
4
[1,2,3,4]
DD
1
[42]
RRD
6
[1,1,2,3,5,8]
D
0
[]
```

**예제 출력1**

```
[2,1]
error
[1,2,3,5,8]
error
```

### **출처**

## **🧐CODE REVIEW**

### **🧾나의 풀이**

```python
from collections import deque

T = int(input())

for testcase in range(T):
    operations = input()
    N = int(input())
    temp_string = input()

    if N == 0:
        if 'D' in operations:
            print('error')
        else:
            print('[]')
        continue

    temp_string = temp_string[1:-1]
    
    dq = deque(map(int, temp_string.split(",")))

    reverse = False
    for operation in operations:
        if operation == 'R':
            reverse = not reverse

        else:
            if dq:
                if reverse:
                    dq.pop()
                else:
                    dq.popleft()
            else:
                print('error')
                break
                
    else:
        dq = list(dq)
        if reverse:
            dq.reverse()
        print(f'[{",".join(map(str, dq))}]')
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|39320|236|Python3|838
#### **📝해설**

**알고리즘**
```
1. 덱
2. 문자열
```

### **다른 풀이**

```java
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        int T = 0;
        int in = System.in.read();
        while (in > 32) {
            T = (T << 3) + (T << 1) + (in & 15);
            in = System.in.read();
        }
        
        if (T == 0)
            return;
        
        final byte[] error = {'e','r','r','o','r','\n'};
        
        int[] sa = new int[100000];
        int[] la = new int[100000];
        byte[] buf = new byte[2000000];
        byte[] out = new byte[2000000];
        System.in.read(buf, 0, buf.length);
        int idx = -1;
        int oi = 0;
        
        while (--T != -1) {
            int count = 0;
            int pStart = idx + 1;
            while (buf[++idx] > 32)
                if (buf[idx] == 'D')
                    ++count;
            int pEnd = idx;
            
            int n = 0;
            while (buf[++idx] > 32)
                n = (n << 3) + (n << 1) + (buf[idx] & 15);
            
            ++idx;
            for (int i = 0; i < n; i++) {
                sa[i] = idx + 1;
                while (buf[++idx] != ',' && buf[idx] != ']');
                la[i] = idx - sa[i];
            }
            ++idx;
            
            if (n == 0)
                ++idx;
            
            if (count > n) {
                System.arraycopy(error, 0, out, oi, 6);
                oi += 6;
                continue;
            }
            
            if (count == n) {
                out[oi] = '[';
                out[oi + 1] = ']';
                out[oi + 2] = '\n';
                oi += 3;
                continue;
            }
            
            boolean reversed = false;
            int front = 0;
            int back = n - 1;
            for (int i = pStart; i < pEnd; i++) {
                if (buf[i] == 'R')
                    reversed = !reversed;
                else {
                    if (reversed)
                        back--;
                    else
                        front++;
                }
            }
            
            out[oi++] = '[';
            if (reversed) {
                for (int i = back; i >= front;) {
                    System.arraycopy(buf, sa[i], out, oi, la[i]);
                    out[oi + la[i]] = ',';
                    oi += la[i--] + 1;
                }
            } else {
                for (int i = front; i <= back;) {
                    System.arraycopy(buf, sa[i], out, oi, la[i]);
                    out[oi + la[i]] = ',';
                    oi += la[i++] + 1;
                }
            }
            out[oi - 1] = ']';
            out[oi++] = '\n';
        }
        
        System.out.write(out, 0, oi);
    }
}
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
rudev|21612|184|Java8|2746
#### **📝해설**

```python
from collections import deque

T = int(input())

for testcase in range(T):
    # 입력
    operations = input()
    N = int(input())

    # 일단 문자열로 받음
    temp_string = input()

    # N이 0인경우 D가 하나라도 있으면 에러
    if N == 0:
        if 'D' in operations:
            print('error')
        else:
            # D가 없다면 빈 리스트 출력
            print('[]')
        continue
    
    # 문자열을 파싱하기 위해 맨앞과 맨 뒤 []를 슬라이싱
    temp_string = temp_string[1:-1]
    
    # 문자열을 ,로 파싱하고, 정수형으로 변환하여 deque에 저장
    dq = deque(map(int, temp_string.split(",")))

    # 뒤집힘 여부를 저장할 변수
    reverse = False

    # 문자열을 순회하면서
    for operation in operations:

        # R이라면 뒤집힘을 구현
        if operation == 'R':
            reverse = not reverse

        # D라면 숫자를 빼줌
        else:
            # 아직 deque에 숫자가 남아있다면
            if dq:

                # 뒤집힌 경우 뒤에서 뺌
                if reverse:
                    dq.pop()

                # 뒤집히지 않았다면 앞에서 뺌
                else:
                    dq.popleft()
            
            # deque이 비었다면 에러출력. 종료
            else:
                print('error')
                break

    # 종료되지 않았다면, deque을 출력
    else:

        # 리스트로 변환한 후
        dq = list(dq)

        # 뒤집혔다면 리스트를 뒤집어줌
        if reverse:
            dq.reverse()

        # 주어진 형식에 맞게 출력
        print(f'[{",".join(map(str, dq))}]')
```