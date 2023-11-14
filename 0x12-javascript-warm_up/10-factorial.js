#!/usr/bin/node

/* script that computes and prints a factorial
 * The first argument is integer (argument can be cast as integer)
 * used for computing the factorial
 * Factorial of NaN is 1
 * You must do it recursively
 * You must use a function */

const factorial = (num) => {
  if (num === 1) return num;

  const result = factorial(num - 1);

  return (result * num);
};

const num = process.argv[2];
if (isNaN(num)) {
  console.log('Give me integers please');
} else {
  const answer = factorial(parseInt(num));
  console.log(answer);
}
