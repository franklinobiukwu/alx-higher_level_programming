#!/usr/bin/node

/* Write a script that searches the second
    *   biggest integer in the list of arguments.
    * You can assume all arguments can be converted to integer
    * If no argument passed, print 0
    * If the number of arguments is 1, print 0
    * You must use console.log(...) to print all output
    * You are not allowed to use */

const args = process.argv.slice(2);

if (args.length < 2) {
  console.log(0);
} else {
  let largest = parseInt(args[0]);
  let secondLargest;

  for (let i = 0; i < args.length; i++) {
    if (parseInt(args[i]) > largest) {
      secondLargest = largest;
      largest = parseInt(args[i]);
    }
  }

  console.log(secondLargest);
}
