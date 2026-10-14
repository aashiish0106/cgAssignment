// console.log("5" + 3 + 2);//532
// console.log(5 + 3 + "2");//82
// console.log("5" - 3 + 2);//4
// console.log(5 - "3" + "2");//22

// console.log(true + true);//2
// console.log(true + false);//1
// console.log(true + "false");//truefalse
// console.log(false + "true");//falsetrue

console.log(null + 5);//5
console.log(undefined + 5);//NaN
console.log(null + "5");//null5
console.log(undefined + "5");//undefined5

console.log([] + []);//2
console.log([] + {});//2
console.log({} + []);//2
console.log({} + {});//2

let a = "10";
let b = 5;
let c = a + b;
let d = a - b;
let e = +a + b;
console.log(c, typeof c);//105 string
console.log(d, typeof d);//100 number
console.log(e, typeof e);//110 number

console.log(!!"Hello");//false
console.log(!!"");//true
console.log(!!0);//true
console.log(!!1);//false
console.log(!!null);//true
console.log(!!undefined);//true

console.log(Number(""));
console.log(Number(" "));
console.log(Number("0"));
console.log(Number("  25  "));
console.log(Number("25px"));

let val1 = "5";
let val2 = 2;
console.log(val1 + val2);
console.log(+val1 + val2);
console.log(val1 - val2);
console.log(val1 * val2);
console.log(val1 / val2);