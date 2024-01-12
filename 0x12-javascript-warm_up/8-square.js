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
const size = parseInt(args[0]);

let square = [];

// print "Missing size" if args[0] can't be converted to integer
if (isNaN(parseInt(size))) {
  console.log('Missing size');
} else {
  let i = 0;

  while (i < size) {
    for (let j = 0; j < size; j++) {
      square.push('X');
    }
    console.log(square.join(''));
    square = [];
    i++;
  }
}
