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