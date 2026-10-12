let studentScore=75
let distinctionMarks=75
console.log("Gets distinction ",studentScore>=distinctionMarks)

let ticketPrice=300
let personMoney=300
console.log("Can buy ticket ",personMoney>=ticketPrice)

console.log(25 >= 25);//true
console.log(30 >= 25);//true
console.log(20 >= 25);//false

console.log("25" >= 25);//true
console.log("10" >= "2");//false
console.log(null >= 0);//true

console.log(undefined >= 0);//false
// undefined is coerced to NaN during relational comparison, and comparisons with NaN always return false.

let maxLiftCapacity=8
let currentPeopleInside=8
console.log("Lift full or overloaded ",currentPeopleInside>=maxLiftCapacity)

console.log(true >= 1);//true
// true is coerced to the number 1, making 1 >= 1 true.

console.log("" >= 0);//true
// An empty string "" is coerced to the number 0, making 0 >= 0 true.

console.log(NaN >= NaN);//false
// Any relational comparison involving NaN will always result in false.