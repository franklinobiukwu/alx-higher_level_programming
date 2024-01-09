#!/usr/bin/node

/* Write a script that prints 3 lines: (like 1-multi_languages.js)
    but by using an array of string and a loop
    * The first line: “C is fun”
    * cond line: “Python is cool”
    * The third line: “JavaScript is amazing”
    * You must use console.log(...) to print all output
    * You are not allowed to use var
    * You are not allowed to use any if/else statement
    * You can use only one console.log
    * You must use a loop (while, for, etc.) */

const arr = ['C is fun', 'Python is cool', 'JavaScript is amazing'];

// print each element of array
for (let i = 0; i < arr.length; i++) {
  console.log(arr[i]);
}
