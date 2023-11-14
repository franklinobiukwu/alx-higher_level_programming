#!/usr/bin/node

/* script that searches the second biggest integer in the list of arguments
 * You can assume all arguments can be converted to integer
 * If no argument passed, print 0
 * If the number of arguments is 1, print 0
 * You must use console.log(...) to print all output
 * You are not allowed to use var */

if (process.argv.length < 3 || process.argv.length === 3) {
  console.log(0);
} else {
  /* set the arguments in a new array */
  const list = process.argv.slice(2);

  /* set initial maximum to be first argument */
  let max = parseInt(list[0]);

  /* set the maximum number */
  for (let i = 0; list[i]; i++) {
    if (parseInt(list[i]) > max) max = (parseInt(list[i]));
  }
  /* print the maximum number */
  console.log(max);
}
