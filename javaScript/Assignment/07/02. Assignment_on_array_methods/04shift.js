// Create an array of 4 city names. Remove the first city using shift() and print the remaining array and the removed city.
// Create [10, 20, 30, 40]. Call shift() twice and print the final array and both removed values.
// Start with ["Apple", "Banana", "Mango"]. Remove the first element and store it in a variable. Print the variable and the array.
// How is shift() different from pop()?
// What does shift() return?


let city=["Lucknow","Kalol","Gandhinagar","Jaipur"]
console.log(city.shift())
console.log(city)

let numbers=[10, 20, 30, 40]
console.log(numbers.shift())
console.log(numbers.shift())
console.log(numbers)

let fruits=["Apple", "Banana", "Mango"]
let removedElement=fruits.shift()
console.log(removedElement)
console.log(fruits)

//shift removes from the startings and pop removes from the end

//shift retursns the removed element 

