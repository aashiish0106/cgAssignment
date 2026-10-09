// 8. Predict the Output
// Without running the code, predict what each console.log will print. Explain your reasoning (especially for typeof).

// let person = { name: "Amit", age: 22 };
// let colors = ["red", "green", "blue"];
// function sayHi() {
//   return "Hi!";
// }
// let empty = null;

// console.log(typeof person);
// console.log(typeof colors);
// console.log(typeof sayHi);
// console.log(typeof empty);
// console.log(person.name);
// console.log(colors[1]);
// console.log(sayHi());

let person = { name: "Amit", age: 22 };
let colors = ["red", "green", "blue"];
function sayHi() {
  return "Hi!";
}
let empty = null;

console.log(typeof(person)); //object
console.log(typeof(colors)); //object
console.log(typeof(sayHi));  //function
console.log(typeof(empty)); //object
console.log(person.name); //Amit
console.log(colors[1]); //green
console.log(sayHi()); //Hi!

// 9. Fix the Program
// The following code has multiple errors related to objects, arrays, functions, naming rules, and best practices. Fix it so that it runs correctly.

// let 1student = { name: "Neha", Age: 19 }
// let scores = 90, 85, 88
// function greet {
//   return "Hello " + name
// }
// const maxScore = 100
// maxScore = 95
// console.log(1student.name)
// console.log(scores[0])
// console.log(greet("Neha"))

let student1 = { name: "Neha", Age: 19 }
let scores = [90, 85, 88]
function greet(name) {
  return "Hello " + name
}
let maxScore = 100
maxScore = 95
console.log(student1.name) //Neha
console.log(scores[0]) //90
console.log(greet("Neha")) //Hello Neha


// 10. Concept Questions
// Answer the following in your own words with examples:

// a) What is the main difference between an Object and an Array?
// array is a collection of data in a sequence Enclosed in square brackets Whereas Object is collection of data with Key value pairs Enclosed in curly braces



// b) Why does typeof null return "object"? Is null really an object?
// Because it was a mistake by Javascript developers No null is not really an object it was just Mistake which We can't fix now



// c) Why is it recommended to keep arrays with a single data type?
// Because generally we use Simple arrays



// d) When should you use const and when should you use let?
// When you have a constant value you should use constant when you have A value which varies You should use let

