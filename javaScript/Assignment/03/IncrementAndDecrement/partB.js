let x=5
let y=x++
console.log("Value of x ",x)
console.log("Value of y ",y)
// The values are different because x++ is a post-increment operator. It assigns the original value of x (which is 5) to y first, and then increases x to 6.

let a=5
let b=++a
console.log("Value of a ",a)
console.log("Value of b ",b)
// The difference here is that ++a is a pre-increment operator. It increases the value of a to 6 first, and then assigns that new, updated value to b. Both end up as 6.

let lives=3
let previousLives=lives--
console.log("Remaining lives ",lives)
console.log("Previous lives ",previousLives)

let attempts=0
let currentAttempts=++attempts
console.log("Total attempts ",attempts)
console.log("Current attempts ",currentAttempts)

let points=100
points++
points--
console.log("Final points ",points)