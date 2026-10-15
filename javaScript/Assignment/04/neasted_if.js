// 1. Check if a number is greater than 10, then check if divisible by 3[cite: 3]
let num = 12

if (num > 10) {
    if (num % 3 === 0) {
        console.log("Greater than 10 and divisible by 3")
    }
}

// 2. Check if person is 18 or older, then check voter ID[cite: 3]
let personAge = 25
let hasVoterId = true

if (personAge >= 18) {
    if (hasVoterId) {
        console.log("Can Vote")
    }
}

// 3. Check if scored 40 or more, then check if 80 or above[cite: 3]
let studentScore = 85

if (studentScore >= 40) {
    if (studentScore >= 80) {
        console.log("Passed with Distinction")
    }
}

// 4. ATM system: check PIN, then check balance[cite: 3]
let enteredPIN = 1234
let actualPIN = 1234
let accountBalance = 5000
let withdrawal = 1000

if (enteredPIN === actualPIN) {
    if (accountBalance >= withdrawal) {
        console.log("Transaction successful")
    } else {
        console.log("Insufficient balance")
    }
} else {
    console.log("Incorrect PIN")
}

// 5. Check if year is divisible by 4, then 100, then 400 for leap year[cite: 3]
let year = 2024

if (year % 4 === 0) {
    if (year % 100 === 0) {
        if (year % 400 === 0) {
            console.log("Leap year")
        } else {
            console.log("Not a leap year")
        }
    } else {
        console.log("Leap year")
    }
} else {
    console.log("Not a leap year")
}