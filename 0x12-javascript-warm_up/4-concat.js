#!/usr/bin/node

/* Write a script that prints two arguments passed to it,
    in the following format: “ is ”
    * You must use console.log(...) to print all output
    * You are not allowed to use  */

const passedArgument = process.argv.slice(2);

console.log(`${passedArgument[0]} is ${passedArgument[1]}`);
