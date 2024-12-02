// Problem 1: Check if user is older than 18
const checkAge = age => age > 18 ? "You are good to go!" : "Sorry! You must be 18 or older!";
console.log(checkAge(20)); // Output: You are good to go!
console.log(checkAge(16)); // Output: Sorry! You must be 18 or older!

// Problem 2: Check if it is raining
const isRaining = raining => raining ? "Get your rain jacket!" : "No rain on today's forecast!";
console.log(isRaining(true)); // Output: Get your rain jacket!
console.log(isRaining(false)); // Output: No rain on today's forecast!

// Problem 3: Check if a number is even
const isEven = num => num % 2 === 0 ? "That's an even number!" : "That's an odd number!";
console.log(isEven(4)); // Output: That's an even number!
console.log(isEven(5)); // Output: That's an odd number!

// Problem 4: Compare two numbers
const compareNumbers = (num1, num2) => num1 > num2 ? `${num1} is more than ${num2}!` : `${num1} is less than ${num2}!`;
console.log(compareNumbers(10, 5)); // Output: 10 is more than 5!
console.log(compareNumbers(3, 7)); // Output: 3 is less than 7!

// Ninja Challenge: Implicit returns
const checkAgeNinja = age => age > 18 ? "You are good to go!" : "Sorry! You must be 18 or older!";
const isRainingNinja = raining => raining ? "Get your rain jacket!" : "No rain on today's forecast!";
const isEvenNinja = num => num % 2 === 0 ? "That's an even number!" : "That's an odd number!";
const compareNumbersNinja = (num1, num2) => num1 > num2 ? `${num1} is more than ${num2}!` : `${num1} is less than ${num2}!`;