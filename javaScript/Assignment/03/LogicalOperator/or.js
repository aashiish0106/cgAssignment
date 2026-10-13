let passwordCorrect=true
let otpValid=false
let isLogin=passwordCorrect||otpValid
console.log("Login Allowed: ",isLogin)

let isMember=false
let hasCoupon=true
let isDiscount=isMember||hasCoupon
console.log("Discount Applies: ",isDiscount)

let age=16
let isValidAge=age>18
let height=150
let isValidHeight=height>155
console.log("Entry Allowed: ",isValidAge||isValidHeight)

let emailGiven = true
let phoneGiven = false
console.log("Is form valid? ",emailGiven||phoneGiven)

let score=900
let validScore=score>1000
let timeBound=true
console.log("Next level: ",validScore||timeBound)

// let a = 0;
// let b = false;
// let c = "";
// let d = null;
// let e = 42;
// let result = a || b || c || d || e;
// console.log(result);//42

// let x = "Hello" || 0;
// let y = 0 || "Hi";
// console.log(x, y);//Hello Hi

// let a = 10;
// let b = 20;
// let result = (a < 5) || (b > 15);
// console.log(result);//true

// let val = 5;
// let condition = val || (val = 0);
// console.log(condition);//5
// console.log(val);//5

let x = "" || 0 || false || null || undefined || "OK";
console.log(x);//OK
