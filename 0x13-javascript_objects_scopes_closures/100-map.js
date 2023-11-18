#!/usr/bin/node

/* a script that imports an array and computes a new array */

const arr = require('./100-data').list;

const newArr = arr.map((item, idx) => item * idx);

console.log(arr);
console.log(newArr);
