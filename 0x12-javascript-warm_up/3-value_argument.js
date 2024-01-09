#!/usr/bin/node

/* Write a script that prints the first argument passed to it:
    * If no arguments are passed to the script, print “No argument”
    * You must use console.log(...) to print all output
    * You are not allowed to use var
    * You are not allowed to use length */

const { argv } = require('node:process');

const scriptArgs = argv;

const passedArgs = scriptArgs.slice(2);

// print "No argument" if no arguments are passed to the script
if (passedArgs[0] == null) {
  console.log('No argument');
} else {
  console.log(passedArgs[0]);
}
