// Question 1
let cubeSide = 6;
console.log(cubeSide ** 3); // Output: 216

// Question 2
let squareSide = 9;
console.log(squareSide ** 2); // Output: 81

// Question 3
console.log(5 ** 4); // Output: 625

// Question 4
let pixels = 1024;
console.log(pixels ** 2); // Output: 1048576

// Question 5
let base = 2;
let power = -1;
let result1 = base ** power;
console.log(result1); // Output: 0.5 (Equivalent to 1 / 2^1)

// Question 6
console.log(3 ** 4); // Output: 81

// Question 7
let side = 9;
console.log(side ** 2); // Output: 81

// Question 8
console.log(2 ** 5); // Output: 32
console.log(5 ** 2); // Output: 25
// Explanation: No, they are not the same. Exponentiation is not commutative.

// Question 9
console.log(2 * 3 * 2);   // Output: 512 (Exponentiation is right-associative: evaluates 3**2 first, then 2**9)
console.log((2 * 3) * 2); // Output: 64 (Parentheses force 2**3 first, then 8**2)
console.log(2 ** -3);       // Output: 0.125 (Negative exponent calculates 1 / (2**3))
