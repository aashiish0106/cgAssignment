// 1. Classify the Types
// Declare one variable of each of the following types and print both the value and its type using typeof:

// A whole number
// A decimal number
// A piece of text
// A true/false value
// 2. Undefined vs Null

let num=1;
console.log(typeof(num),num)

let pI=3.14;
console.log(typeof(pI),pI)

let name="Aashiish"
console.log(typeof(name),name)

let isStudent=true
console.log(typeof(isStudent),isStudent)

// 2. Undefined vs Null
// Declare two variables:

// a using let without assigning any value
// b and intentionally assign null to it
// Print both variables and their typeof results. Explain the difference between undefined and null.

let work;
console.log(work);

let force=null;
console.log(force)

// 3. Number Special Values
// Create variables for the following and print each value along with its type:

// Positive Infinity
// Negative Infinity
// Not-a-Number (NaN)
// A large number written with scientific notation (e.g., 2.5e3)
// A number written with underscores for readability (e.g., 1_000_000)

// 1. Positive Infinity
let positiveInfinity = Infinity;
console.log(positiveInfinity,typeof(positiveInfinity));

// 2. Negative Infinity
let negativeInfinity = -Infinity;
console.log(negativeInfinity,typeof(negativeInfinity));

// 3. Not-a-Number (NaN)
let notANumber = NaN;
console.log(notANumber,typeof(notANumber));

// 4. A large number written with scientific notation
let scientificNum = 2.5e3;
console.log(scientificNum,typeof(scientificNum));
// 5. A number written with underscores for readability
let readableNum = 1_000_000;
console.log(readableNum,typeof(readableNum));


// 4. String Styles
// Create three string variables using:

// Single quotes
// Double quotes
// Template literals (backticks) that include another variable
// Print all three strings.

// 1. String using single quotes
let singleQuoteStr = 'Hello using single quotes!';
console.log(singleQuoteStr);

// 2. String using double quotes
let doubleQuoteStr = "Hello using double quotes!";
console.log(doubleQuoteStr);

// 3. Template literals (backticks) including another variable
let sub = "JavaScript";
let templateLiteralStr = `Hello, this template literal includes the variable: ${sub}!`;
console.log(templateLiteralStr);