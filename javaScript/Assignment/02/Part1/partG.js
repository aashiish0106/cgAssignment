// 8. Predict the Output
// Without running the code, predict what each console.log will print (value + type). Explain your reasoning.
let a;
let b = null;
let c = 42;
let d = "Hello";
let e = true;
let f = Symbol("key");
let g = 123n;

console.log(typeof a, a);
console.log(typeof b, b);
console.log(typeof c, c);
console.log(typeof d, d);
console.log(typeof e, e);
console.log(typeof f, f);
console.log(typeof g, g);

// 9. Fix the Code
// The following program has mistakes related to primitive types. Fix it so that it runs correctly and prints meaningful values.

// let num = 10;
// let text = Hello;
// let flag = True;
// let empty;
// let nothing = Null;
// let unique = symbol("id");
// let big = 9007199254740991;

// console.log(num, text, flag, empty, nothing, unique, big);

let num = 10;
let text = "Hello";
let flag = true;
let empty;
let nothing = null;
let unique = Symbol("id");
let big = 9007199254740991n;

console.log(num, text, flag, empty, nothing, unique, big);