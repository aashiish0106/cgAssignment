let age=18
let votingAge=18
console.log("Can vote ",age>=votingAge)

let temperature=32
let maxTemp=35
console.log("Is cooler ",temperature<maxTemp)

let score=90
let targetScore=85
console.log("Beat target ",score>targetScore)

console.log(10 > 5 && 5 < 10);//true
console.log("10" >= 10);//true
// "10" is coerced into the number 10, making 10 >= 10 true.

console.log(null <= undefined);//false
// undefined becomes NaN. Relational comparisons with NaN are always false.

console.log("5" < "10" && 5 > 2);//false
// "5" < "10" is false because strings are compared alphabetically, and '5' comes after '1'.

let productCost=499
let customerMoney=500
console.log("Can buy product ",customerMoney>=productCost)
console.log("Change will be left ",productCost<customerMoney)

// Explanation for "10" > "2" vs 10 > 2:
// "10" > "2" is false because when comparing two strings, JavaScript evaluates them lexicographically (alphabetically) from left to right. Since '1' comes before '2' in the dictionary order, "10" is considered smaller.
// 10 > 2 is true because both are numbers, so JavaScript evaluates them mathematically.