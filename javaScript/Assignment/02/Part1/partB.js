// 5. Choose the Correct Keyword Create the following variables using the most appropriate keyword:

// studentName — the value will not change
// marks — the value may change
// schoolName — the value will not change
// Assign values to all three variables. Change marks and print all variables.

const studentName='Aashiish'
let marks=100
const schoolName="KV"

console.log(marks)

marks=90

console.log(studentName)
console.log(marks)
console.log(studentName)

// 6. Understand Scope Write a program where var, let, and const variables are declared inside an if block. Try to access all three variables outside the block. Observe and identify which variables can be accessed.

if(true){
    var a=10
    let b=20
    const c=30
}
console.log(a)
console.log(b)
console.log(c)

// 7. Test Re-declaration Declare a variable named user using var and declare it again with a different value. Then perform the same experiment using let. Observe what happens and identify which declaration allows re-declaration.

var user=1;
var user=2;

let user=1;
let user=2;

// 8. Test Re-assignment Create three variables using var, let, and const. Assign an initial value to each. Try to change the value of all three variables. Observe which variables allow re-assignment and which one produces an error.

var a=1;
a=2

let b=2;
b=3;

const c=3;
c=4;


