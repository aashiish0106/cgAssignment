// 11. Predict the Hoisting Behavior
// Without running the code, predict the output of each console.log() and identify which lines cause errors. Explain your answer using the rules of hoisting for var, let, and const.

console.log(a);//undefined
console.log(b);//Cannot access 'b' before initializat
ion
console.log(c);//ReferenceError: Cannot access 'c' before initializat
ion

var a = 10;
let b = 20;
const c = 30;


// 12. Fix the Hoisting Errors
// The following program contains errors related to hoisting. Fix the code so that it runs correctly without any errors. Make sure your solution follows the rules of hoisting for var, let, and const (you may reorder declarations/assignments or change keywords only where necessary to make it work properly).

// console.log(x);
// console.log(y);
// console.log(z);

// var x = "Hello";
// let y = "World";
// const z = "!";

// console.log(x + " " + y + z);


var x = "Hello";
let y = "World";
const z = "!";

console.log(x);
console.log(y);
console.log(z);

console.log(x + " " + y + z);