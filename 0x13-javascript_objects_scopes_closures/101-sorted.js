#!/usr/bin/node

/*  a script that imports a dictionary of occurrences by
 *  user id and computes a dictionary of user ids by occurrence */

const dict = require('./101-data').dict;

const entries = Object.entries(dict);
const newDict = {};

entries.forEach((item) => {
  const occurrence = item[1];

  if (!newDict[occurrence]) {
    newDict[occurrence] = [item[0]];
  } else {
    newDict[occurrence].push(item[0]);
  }
});

console.log(newDict);
