let month = 7

if (month === 12 || month === 1 || month === 2) {
    console.log("Winter")
} else if (month >= 3 && month <= 5) {
    console.log("Summer")
} else if (month >= 6 && month <= 8) {
    console.log("Monsoon")
} else if (month >= 9 && month <= 11) {
    console.log("Autumn")
} else {
    console.log("Invalid month")
}

let income = 500000
let taxAmount = 0

if (income < 300000) {
    taxAmount = 0
} else if (income >= 300000 && income <= 700000) {
    taxAmount = income * 0.05
} else if (income > 700000 && income <= 1000000) {
    taxAmount = income * 0.10
} else if (income > 1000000) {
    taxAmount = income * 0.15
}
console.log("Tax amount: " + taxAmount)

let studentScore = 85

if (studentScore >= 90) {
    console.log("Outstanding")
} else if (studentScore >= 70 && studentScore <= 89) {
    console.log("Good")
} else if (studentScore >= 40 && studentScore <= 69) {
    console.log("Average")
} else if (studentScore < 40) {
    console.log("Needs Improvement")
}

let speed = 55

if (speed < 40) {
    console.log("Slow")
} else if (speed >= 40 && speed <= 80) {
    console.log("Normal")
} else if (speed > 80) {
    console.log("Fast")
}

let height = 160

if (height < 150) {
    console.log("Short")
} else if (height >= 150 && height <= 170) {
    console.log("Average")
} else if (height > 170) {
    console.log("Tall")
}