let fs = require('fs')
let input = fs.readFileSync('/dev/stdin').toString().split(' ')
// 백준에서 입출력 받는 법

// i는 5 4 3 2 1 이 되도록 순회
for (let i=input; i>0; i--){
    // 공백을 출력하는 for문
    // 5, 4 5, 3 4 5, 2 3 4 5, 이런 식으로 반복됨
    for(let j=i; j<input; j++){
        // 줄바꿈을 하지 않고 출력
        process.stdout.write(' ')
    }
    // *을 출력하는 for문
    // 9 7 5 3 1번 반복
    for(let j=i*2-1; j>0 ; j--){
        process.stdout.write('*')
    }
    console.log('')
}

// 아래도 동일한 방식
for (let i=2; i<=input ; i++){
    for(let j=i; j<input; j++){
        process.stdout.write(' ')
    }
    for(let j=i*2-1; j>0 ; j--){
        process.stdout.write('*')
    }
    console.log('')
}