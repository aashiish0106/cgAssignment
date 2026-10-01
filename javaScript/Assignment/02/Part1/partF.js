// 5. Symbol Uniqueness
// Create two Symbols with the same description ('id').
// Compare them using === and print the result.
// Then use both Symbols as keys in an object and retrieve the values.
// Explain why the comparison returns false.

let x=Symbol('id');
let y=Symbol('id');
console.log(x==y);

// 6. BigInt Precision
// Create a regular number with the value 9007199254740991 (Number.MAX_SAFE_INTEGER).
// Add 1, 2, and 3 to it and print the results.
// Now create the same value as a BigInt and perform the same additions.
// Print the results and explain the difference.

let num=9007199254740991;
console.log(num+1)
console.log(num+2)
console.log(num+3)

let num1=9007199254740991n;
console.log(num1+1n)
console.log(num1+2n)
console.log(num1+3n)

// 7. Choose the Correct Type
// For each description below, write the most appropriate primitive data type and give an example declaration:

// A unique identifier that is never equal to another value with the same description
// A very large integer that must keep exact precision
// A variable that has been declared but not yet given a value
// An intentional empty value