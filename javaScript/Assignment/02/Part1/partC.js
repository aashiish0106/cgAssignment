// 9. Predict and Explain Without running the code, predict the output of each console.log() and identify which lines cause errors. Explain your answer using the rules of scope, re-assignment, and variable declaration.

var x = 10;

if (true) {
    var x = 20;
    let y = 30;
    const z = 40;
}

console.log(x);
console.log(y); //this will raise an error
console.log(z);


// 10. Fix the Program The following program contains multiple errors. Fix the code so that it runs correctly. Make sure your solution follows the rules for initialization, re-declaration, re-assignment, and scope.

// const name;

// let age = 20;
// let age = 25;

// if (true) {
//     var city = "Delhi";
//     let country = "India";
// }

// console.log(country);

// const score = 50;
// score = 80;

const name="Aashiish";

let age = 20;
age = 25;

if (true) {
    var city = "Delhi";
    let country = "India";
    console.log(country);
}



let score = 50;
score = 80;

