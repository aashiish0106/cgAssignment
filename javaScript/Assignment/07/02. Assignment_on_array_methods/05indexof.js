// Create an array of 6 fruits. Find the index of a fruit that exists and one that does not exist using indexOf().
// Create an array ["A", "B", "C", "B", "D"]. Print the index of "B" using indexOf().
// Create an array of 4 student names. Check the index of your name (or any name) and print the result.
// What does indexOf() return if the element is not found?
// What will indexOf() return if the element appears more than once in the array?


let fruits=["Mangoes","Banana","Kiwi","Cherry","Apple","BlueBerry"]
console.log(fruits.indexOf("Banana"))
console.log(fruits.indexOf("Rasberry"))

let alphabets=["A", "B", "C", "B", "D"]
console.log(alphabets.indexOf("B"))

let studentNames=["Aashiish","Aashii","Unnatii","Harshii"]
console.log(studentNames.indexOf("Aashii"))

//indexof returns -1 if the element was not found

let arr=[1,2,3,4,3,4,3]
console.log(arr.indexOf(3))
//it will give the first elements index

