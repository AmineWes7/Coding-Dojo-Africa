// Problem 1
const cars = ['Tesla', 'Mercedes', 'Honda'];
const [randomCar] = cars;
const [, otherRandomCar] = cars;

// randomCar: "Tesla"
// otherRandomCar: "Mercedes"

console.log(randomCar); // Tesla
console.log(otherRandomCar); // Mercedes
// 3. Answering any questions associated with the problem block here.
// The first element "Tesla" is assigned to randomCar, and the second element "Mercedes" is assigned to otherRandomCar.

// Problem 2
const employee = {
    employeeName: 'Elon',
    age: 47,
    company: 'Tesla'
};
const { employeeName: otherName } = employee;

// otherName: "Elon"

console.log(otherName); // Elon
console.log(employeeName); // ReferenceError: employeeName is not defined


// Problem 3
const person = {
    name: 'Phil Smith',
    age: 47,
    height: '6 feet'
};
const password = '12345';
const { password: hashedPassword } = person;  

// password: "12345"
// hashedPassword: undefined

console.log(password); // 12345
console.log(hashedPassword); // undefined


// Problem 4
const numbers = [8, 2, 3, 5, 6, 1, 67, 12, 2];
const [, first] = numbers;
const [,,, second] = numbers;
const [,,,,,,,, third] = numbers;

// first: 2
// second: 12
// third: undefined

console.log(first === second); // false
console.log(first === third); // false

// Problem 5
const lastTest = {
    key: 'value',
    secondKey: [1, 5, 1, 8, 3, 3]
};
const { key } = lastTest;
const { secondKey } = lastTest;
const [, willThisWork] = secondKey;
// key: "value"
// secondKey: [1, 5, 1, 8, 3, 3]
// willThisWork: 5

console.log(key); // value
console.log(secondKey); // [1, 5, 1, 8, 3, 3]
console.log(secondKey[0]); // 1
console.log(willThisWork); // 5


// Problem 6
var beatles = ['Paul', 'George', 'John', 'Ringo'];
function printNames(names) {
  function actuallyPrintingNames() {
    for (var index = 0; index < names.length; index++) {
      var name = names[index];
      console.log(name + ' was found at index ' + index);
    }
    console.log('name and index after loop is ' + name + ':' + index);
  }
  actuallyPrintingNames();
}
printNames(beatles);

// Paul was found at index 0
// George was found at index 1
// John was found at index 2
// Ringo was found at index 3
// name and index after loop is Ringo: 4

