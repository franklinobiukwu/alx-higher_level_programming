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
  let largest;
  let secondLargest;

  // set first integer as largest variable
  for (let i = 0; i < args.length; i++) {
    if (isNaN(parseInt(args[i]))) {
      continue;
    }
    largest = parseInt(args[i]);
    secondLargest = parseInt(args[i + 1]);
    break;
  }

  // determine second largest integer in list of args
  for (let i = 0; i < args.length; i++) {
    if (parseInt(args[i]) > largest) {
      secondLargest = largest;
      largest = parseInt(args[i]);
    } else if (parseInt(args[i + 1]) > secondLargest) {
      secondLargest = parseInt(args[i + 1]);
    }
  }

  console.log(secondLargest);
}
