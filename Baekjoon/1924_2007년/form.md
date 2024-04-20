# [1924] 2007년

### **난이도**
브론즈 1
## **📝문제**
오늘은 2007년 1월 1일 월요일이다. 그렇다면 2007년 x월 y일은 무슨 요일일까? 이를 알아내는 프로그램을 작성하시오.
### **입력**
첫째 줄에 빈 칸을 사이에 두고 x(1 ≤ x ≤ 12)와 y(1 ≤ y ≤ 31)이 주어진다. 참고로 2007년에는 1, 3, 5, 7, 8, 10, 12월은 31일까지, 4, 6, 9, 11월은 30일까지, 2월은 28일까지 있다.
### **출력**
첫째 줄에 x월 y일이 무슨 요일인지에 따라 SUN, MON, TUE, WED, THU, FRI, SAT중 하나를 출력한다.
### **예제입출력**

**예제 입력1**

```
1 1
```

**예제 출력1**

```
MON
```

**예제 입력2**

```
3 14
```

**예제 출력2**

```
WED
```

**예제 입력3**

```
9 2
```

**예제 출력3**

```
SUN
```


## **🧐CODE REVIEW**

### **🧾나의 풀이**

```js
let fs = require('fs')
let input = fs.readFileSync('/dev/stdin').toString().split(' ')
// let input = fs.readFileSync('input.txt').toString().split(' ')

let date = 0
const month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for (let i=0; i<input[0]; i++){
    date += month[i]
}
date += Number(input[1])

const day = date % 7

const week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
console.log(week[day])
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|9328|128|node.js|422