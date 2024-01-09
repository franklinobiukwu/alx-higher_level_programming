#!/usr/bin/node

/* Write a script that prints a square
    * The first argument is the size of the square
    * If the first argument can’t be converted to an integer,
    *   print “Missing size”
    * You must use the character X to print the square
    * You must use console.log(...) to print all output
    * You are not allowed to use var
    * You must use a loop (while, for, etc.) */

const args = process.argv.slice(2);

const square = [];

// print "Missing size" if args[0] can't be converted to integer
if (isNaN(parseInt(args[0]))) {
  console.log('Missing size');
} else {
  const size = parseInt(args[0]);
  let i = 0;

  while (i < size) {
    for (let j = 0; j < size; j++) {
      square.push('x');
    }
    if (i < size - 1) {
      square.push('\n');
    }
    i++;
  }

  console.log(square.join(''));
}
