# [2446] 별 찍기 - 9

### **난이도**
브론즈 3
## **📝문제**
예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.
### **입력**
첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
### **출력**
첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력한다.
### **예제입출력**

**예제 입력1**

```
5
```

**예제 출력1**

```
*********
 *******
  *****
   ***
    *
   ***
  *****
 *******
*********
```
## **🧐CODE REVIEW**

### **🧾나의 풀이**

```js
let fs = require('fs')
let input = fs.readFileSync('/dev/stdin').toString().split(' ')

for (let i=input; i>0; i--){
    for(let j=i; j<input; j++){
        process.stdout.write(' ')
    }
    for(let j=i*2-1; j>0 ; j--){
        process.stdout.write('*')
    }

    console.log('')
}

for (let i=2; i<=input ; i++){
    for(let j=i; j<input; j++){
        process.stdout.write(' ')
    }
    for(let j=i*2-1; j>0 ; j--){
        process.stdout.write('*')
    }
    console.log('')
}
```

결과	| 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B)
:----:|:-----:|:-----:|:-----:|:--------:
정답|14196|1600|node.js|483
#### **📝해설**

### **다른 풀이**

```python
var line = require("fs").readFileSync("/dev/stdin", "utf8");
//var line = require("fs").readFileSync("./test.txt", "utf8");

var T = parseInt(line.trim());

for (var i = 0; i < T; i++) {
  var star = "";
  for (var j = 0; j < i; j++) {
    star += " ";
  }
  for (var k = T; k > i; k--) {
    star += "*";
  }
  for (var k = T; k > i + 1; k--) {
    star += "*";
  }
  console.log(star);
}
for (var i = T - 2; i > -1; i--) {
  var star = "";
  for (var j = 0; j < i; j++) {
    star += " ";
  }
  for (var k = T; k > i; k--) {
    star += "*";
  }
  for (var k = T; k > i + 1; k--) {
    star += "*";
  }
  console.log(star);
}
```

아이디 | 메모리(KB) |	시간(ms) |	언어 |	코드 길이(B) 
:-----:|:-----:|:-----:|:----:|:--------:
ibs06|720568|60|node.js|628
#### **📝해설**

```js
```

### **🔖정리**

1. 배운점