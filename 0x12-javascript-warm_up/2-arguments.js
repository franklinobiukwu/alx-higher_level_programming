#!/usr/bin/node

/*  Script that prints a message depending of the number of arguments passed:
    *  If no arguments are passed to the script, print “No argument”
    *  If only one argument is passed to the script, print “Argument found”
    *  Otherwise, print “Arguments found”
    *  You must use console.log(...) to print all output
    *  You are not allowed to use var */

/* set the command-line argument array in variable */
const cmdArgArray = process.argv;

/* extract the arguments excluding the first two elements
    * which are node and the script filename */
const selectedCmdArray = cmdArgArray.slice(2);

/* print "No argument" if no argument is passed
    * print “Argument found” if only one argument is passed
    * else print "Arguments found" */
if (selectedCmdArray.length === 0) {
  console.log('No argument');
} else if (selectedCmdArray.length === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
