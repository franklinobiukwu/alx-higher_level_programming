#!/usr/bin/node

/* Write a script that computes and prints a factorial
    * The first argument is integer (argument can be cast as integer)
    *   used for computing the factorial
    * Factorial of NaN is 1
    * You must do it recursively
    * You must use a function
    * You must use console.log(...) to print all output
    * You are not allowed to use */

// reursive function that computes factorial of a number
const factorial = function (num) {
  if (num > 1) {
    const fact = factorial(num - 1);
    return num * fact;
  }

  return (1);
};

// set command-line argument in constant variable
const args = process.argv.slice(2);

// type cast first argument as integer
const number = parseInt(args[0]);

// return 1 if first argument is not an integer, and factorial if an integer
if (isNaN(number)) {
  console.log(1);
} else {
  const result = factorial(number);
  console.log(result);
}
