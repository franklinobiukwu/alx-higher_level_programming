#!/usr/bin/node

/* script that prints the addition of 2 integers
 * The first argument is the first integer
 * The second argument is the second integer
 * You have to define a function with this prototype: function add(a, b) */

function add (a, b) {
  console.log(a + b);
}

const num1 = process.argv[2];
const num2 = process.argv[3];

if (isNaN(num1) || isNaN(num2)) {
  console.log('I can help you if you provide integers');
} else {
  add(parseInt(num1), parseInt(num2));
}
