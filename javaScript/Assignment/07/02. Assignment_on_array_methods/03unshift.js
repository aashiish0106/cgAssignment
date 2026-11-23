// Start with ["CSS", "JavaScript"]. Use unshift() to add "HTML" at the beginning and print the array.
// Create an array [20, 30]. Add 5 and 10 at the beginning using unshift() and print the result.
// Create an empty array. Use unshift() to add three city names one by one and print the final array.
// Where does unshift() add the new element(s)?
// Can unshift() add more than one element at the same time? Give a short explanation.

let subject=["CSS", "JavaScript"]
subject.unshift("HTML")
console.log(subject)

let numbers=[20, 30]
numbers.unshift(10)
numbers.unshift(5)
console.log(numbers)

let arr=[]
arr.unshift("Lucknow")
arr.unshift("Gandhinagar")
arr.unshift("Kalol")
console.log(arr)

//Unshift adds the elements at the starting of the array

let arr01=[]
arr.unshift("Lucknow","Gandhinagar")
console.log(arr01)

//No Unshift do not adds more than one element at onces


