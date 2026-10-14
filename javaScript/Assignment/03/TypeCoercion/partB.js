console.log("10" - 5);//5
console.log("10" + 5);//105
console.log("10" * 2);//20
console.log("10" / 2);//5

console.log("5" - "2");//3
console.log("5" + "2");//52
console.log("5" * "2");//10
console.log("5" / "2");//2.5

console.log(Number("123"));//123
console.log(Number("123abc"));//NaN
console.log(Number(true));//1
console.log(Number(false));//0
console.log(Number(null));//0
console.log(Number(undefined));//NaN

console.log(Boolean(0));//false
console.log(Boolean(""));//false
console.log(Boolean("0"));//true
console.log(Boolean([]));//true
console.log(Boolean({}));//true
console.log(Boolean(null));//false

console.log(String(100));//100
console.log(String(true));//true
console.log(String(null));//null
console.log(String(undefined));//undefined
console.log(100 + "");//100