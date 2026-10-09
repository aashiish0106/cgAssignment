// 1. Create an Object
// Create an object named student with the following properties:

// name → "Riya"
// age → 18
// isEnrolled → true
// Print the entire object and then print each property individually.


let student={
    name : "Riya",
    age : 18,
    isEnrolled : true
}

console.log(student)
console.log(student.name)
console.log(student.age)
console.log(student.isEnrolled)

// 2. Work with Arrays
// Create two arrays:

// scores containing only numbers: 85, 92, 78, 90
// mixedData containing different types: a number, a string, a boolean, and null
// Print both arrays. Also print the first and last element of the scores array using index.

let scores=[85,92,78,90]
let mixedData=[10,"Messi",true,null]

console.log(scores)
console.log(mixedData)

console.log(scores[(scores.length)-1])
console.log(scores[0])


// 3. Declare and Call a Function
// Write a function named calculateArea that takes two parameters (length and width) and returns the area of a rectangle.
// Call the function twice with different values and print the results.

function calculateArea(length,width){
    return length*width
}

console.log(calculateArea(5,6))
console.log(calculateArea(10,20))

// 4. Check Types with typeof
// Create variables of the following types and print both the value and its type using typeof:

// A number
// A string
// A boolean
// null
// An object
// An array
// A function
// Observe and note any surprising results (especially with null and arrays).


let num=100
console.log(typeof(num))

let name1="Unna"
console.log(typeof(name1))

let isStudent=true
console.log(typeof(isStudent))

let marks=null
console.log(typeof(marks))



console.log(typeof(student))
console.log(typeof(scores))
console.log(typeof(calculateArea))


