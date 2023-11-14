#!/usr/bin/node

/* script that prints a square
 * The first argument is the size of the square
 * If the first argument can’t be converted to an integer,
 * print “Missing size”
 * You must use the character X to print the square */

const size = process.argv[2];
let arr = [];

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    for (let j = 0; j < size; j++) {
      arr.push('x');
    }
    console.log(arr.join(''));
    arr = [];
  }
}
