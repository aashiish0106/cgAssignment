// Create an array of 5 numbers. Use pop() twice and print the modified array and the two removed values.
// Create an array ["Red", "Blue", "Green"]. Remove the last element using pop() and print both the array and the removed element.
// Start with [100, 200, 300, 400]. Call pop() once and store the returned value in a variable. Print the variable and the array.
// What does pop() return?
// What happens if you call pop() on an empty array?

let numbers=[1,2,3,4,5]
console.log(numbers.pop())
console.log(numbers.pop())
console.log(numbers)

let color=["Red", "Blue", "Green"]
console.log(color.pop())
console.log(color)

let arr=[100, 200, 300, 400]
let removedValue=arr.pop()
console.log(arr)
console.log(removedValue)

// pop returns the the end value

let arr01=[]
console.log(arr01.pop())
console.log(arr01)