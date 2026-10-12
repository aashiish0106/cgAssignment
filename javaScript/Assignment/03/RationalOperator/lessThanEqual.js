let speedLimit=60
let vehicleSpeed=60
console.log("Within limit ",vehicleSpeed<=speedLimit)

let studentScore=39
let maxFailMarks=39 
console.log("Has failed ",studentScore<=maxFailMarks)

console.log(15 <= 20);//true
console.log(20 <= 15);//false
console.log(15 <= 15);//true

console.log("15" <= 20);//true
console.log("30" <= "5");//true
console.log(null <= 0);//true

console.log(undefined <= 0);//false
// undefined is coerced to NaN during relational comparison, and comparisons with NaN always return false.

let bagCapacity=10
let currentBooks=10
console.log("Can add more ",currentBooks<=bagCapacity-1)

console.log(false <= 0);//true
// false is coerced to the number 0, making 0 <= 0 true.

console.log("" <= 0);//true
// An empty string "" is coerced to the number 0, making 0 <= 0 true.

console.log(NaN <= 5);//false
// Any relational comparison involving NaN will always result in false.