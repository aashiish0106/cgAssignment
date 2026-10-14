
console.log(typeof (42));//number
console.log(typeof ("Hello"));//string
console.log(typeof (true));//boolean
console.log(typeof (undefined));//undefined

console.log(typeof (null));//obj
console.log(typeof ({}));//obj
console.log(typeof ([]));//obj

console.log(typeof (NaN));//Number
console.log(typeof (Infinity));//Number
console.log(typeof (function(){}));//Function

let price = 99.99
let message = "Welcome"
let isActive = false

console.log(typeof(price))
console.log(typeof(message))
console.log(typeof(isActive))

let value = null;
console.log(typeof (value));//obj
console.log(typeof (value === "object"));//boolean