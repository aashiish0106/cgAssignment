let userName="Admin"
let password=1234
console.log(userName&&password)

let isLoggedIn=true
let hasPermission=true
console.log("Can acess: ",isLoggedIn&&hasPermission)

let isStock=true
let stockPrice=800

console.log("Can bought: ",stockPrice<1000&&isStock)

let studentMark=75
let studentAttendence=80
let passingMarks=studentMark>65
let passingAttendence=studentAttendence>70

console.log("Is student pass? ",passingAttendence&&passingMarks)

let isWeekend = true
let isHoliday = false
console.log("Party? ",isHoliday&&isWeekend)

// let a = 0;
// let b = 10;
// let result = a && b;
// console.log(result);//0

// let x = 5;
// let y = 10;
// let result = (x > 3 && y) || 0;
// console.log(result);//10

// let p = "Hello";
// let q = "";
// let r = "World";
// let result = p && q && r;
// console.log(result);//""

// let val = 5;
// let condition = val && (val = 0);
// console.log(condition);//0
// console.log(val);//0

// let x = 10;
// let y = 20;
// let result = (x && y) && (x > y);
// console.log(result);//false
