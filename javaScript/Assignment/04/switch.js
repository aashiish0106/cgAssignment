let month = 2; // Change to test (1 - 12)

switch (month) {
  case 1:  // January
  case 3:  // March
  case 5:  // May
  case 7:  // July
  case 8:  // August
  case 10: // October
  case 12: // December
    console.log("31 days");
    break;

  case 4:  // April
  case 6:  // June
  case 9:  // September
  case 11: // November
    console.log("30 days");
    break;

  case 2:  // February
    console.log("28 days");
    break;

  default:
    console.log("Invalid month number. Please enter a value between 1 and 12.");
}


let char = 'e'; // Change to any character
let lowerChar = char.toLowerCase();

switch (lowerChar) {
  case 'a':
  case 'e':
  case 'i':
  case 'o':
  case 'u':
    console.log(`${char} is a Vowel`);
    break;

  default:
    if (lowerChar >= 'a' && lowerChar <= 'z') {
      console.log(`${char} is a Consonant`);
    } else {
      console.log("Not an alphabet character");
    }
}

let seasonNumber = 3; // Change to test (1 to 4)

switch (seasonNumber) {
  case 1:
  case 2:
    console.log("Winter");
    break;

  case 3:
  case 4:
    console.log("Summer");
    break;

  default:
    console.log("Invalid input. Enter a number between 1 and 4.");
}

let marks = 68; // Change to test

switch (true) {
  case (marks >= 75):
    console.log("Distinction");
    break;

  case (marks >= 60):
    console.log("1st class");
    break;

  case (marks >= 50):
    console.log("2nd class");
    break;

  case (marks >= 35):
    console.log("3rd class");
    break;

  case (marks >= 0 && marks < 35):
    console.log("Failed");
    break;

  default:
    console.log("Invalid marks entered.");
}

let role = "admin";    // "admin" or "user"
let action = "create"; // "create", "edit", or "delete"

switch (role) {
  case "admin":
    // Nested switch for admin actions
    switch (action) {
      case "create":
        console.log("Admin action: Record created.");
        break;
      case "edit":
        console.log("Admin action: Record updated.");
        break;
      case "delete":
        console.log("Admin action: Record deleted.");
        break;
      default:
        console.log("Admin action: Invalid or unknown action.");
    }
    break;

  case "user":
    console.log("Limited Access");
    break;

  default:
    console.log("Invalid role.");
}


// let fruit = "mango";

// switch (fruit) {
//   case "apple":
//     console.log("Apple is red");
//   case "mango":
//     console.log("Mango is yellow");
//   case "banana":
//     console.log("Banana is yellow");
//   default:
//     console.log("Unknown fruit");
// }

// Mango is yellow
// Banana is yellow
// Unknown fruit

let fruit = "mango";

switch (fruit) {
  case "apple":
    console.log("Apple is red");
    break;
  case "mango":
    console.log("Mango is yellow");
    break;
  case "banana":
    console.log("Banana is yellow");
    break;
  default:
    console.log("Unknown fruit");
}


let value = "0"; // Test with 0, "0", false, null, undefined

switch (value) {
  case 0:
    console.log("Matched: Number 0");
    break;
  case "0":
    console.log("Matched: String '0'");
    break;
  case false:
    console.log("Matched: Boolean false");
    break;
  case null:
    console.log("Matched: null");
    break;
  case undefined:
    console.log("Matched: undefined");
    break;
  default:
    console.log("Matched: Other value");
}



let num1 = 10;
let num2 = 0;
let operator = "/"; // +, -, *, /, %, **

switch (operator) {
  case "+":
    console.log(`${num1} + ${num2} = ${num1 + num2}`);
    break;

  case "-":
    console.log(`${num1} - ${num2} = ${num1 - num2}`);
    break;

  case "*":
    console.log(`${num1} * ${num2} = ${num1 * num2}`);
    break;

  case "/":
    if (num2 === 0) {
      console.log("Error: Division by zero is not allowed.");
    } else {
      console.log(`${num1} / ${num2} = ${num1 / num2}`);
    }
    break;

  case "%":
    if (num2 === 0) {
      console.log("Error: Modulo by zero is not allowed.");
    } else {
      console.log(`${num1} % ${num2} = ${num1 % num2}`);
    }
    break;

  case "**":
    console.log(`${num1} ** ${num2} = ${num1 ** num2}`);
    break;

  default:
    console.log("Error: Invalid operator.");
}


let day = 15; // Day number of the month (1–31)

switch (true) {
  case (day >= 1 && day <= 10):
    console.log("Beginning of the month");
    break;

  case (day >= 11 && day <= 20):
    console.log("Middle of the month");
    break;

  case (day >= 21 && day <= 31):
    console.log("End of the month");
    break;

  default:
    console.log("Invalid date! Please enter a day between 1 and 31.");
}



let category = "veg";       // "veg" or "non veg"
let item = "paneer tikka";  // Based on category
let size = "full";          // "half" or "full"

let price = 0;
let validOrder = true;

switch (category) {
  case "veg":
    switch (item) {
      case "paneer tikka":
        switch (size) {
          case "half": price = 120; break;
          case "full": price = 220; break;
          default: validOrder = false;
        }
        break;

      case "dal makhani":
        switch (size) {
          case "half": price = 100; break;
          case "full": price = 180; break;
          default: validOrder = false;
        }
        break;

      default:
        validOrder = false;
        console.log("Item not available in Veg menu.");
    }
    break;

  case "non veg":
    switch (item) {
      case "chicken curry":
        switch (size) {
          case "half": price = 160; break;
          case "full": price = 300; break;
          default: validOrder = false;
        }
        break;

      case "butter chicken":
        switch (size) {
          case "half": price = 180; break;
          case "full": price = 340; break;
          default: validOrder = false;
        }
        break;

      default:
        validOrder = false;
        console.log("Item not available in Non-Veg menu.");
    }
    break;

  default:
    validOrder = false;
    console.log("Invalid food category selected.");
}

if (validOrder && price > 0) {
  console.log("--- Order Summary ---");
  console.log(`Category : ${category.toUpperCase()}`);
  console.log(`Item     : ${item}`);
  console.log(`Size     : ${size}`);
  console.log(`Total    : $${price}`);
} else if (validOrder && price === 0) {
  console.log("Invalid size selected (choose 'half' or 'full').");
}