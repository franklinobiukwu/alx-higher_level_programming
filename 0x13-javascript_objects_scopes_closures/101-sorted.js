#!/usr/bin/node

/* Write a script that imports a dictionary of occurrences by user id
    *   and computes a dictionary of user ids by occurrence.
    * Your script must import dict from the file 101-data.js
    * In the new dictionary:
    * A key is a number of occurrences
    * A value is the list of user ids
    * Print the new dictionary at the end */

const dict = require('./101-data.js').dict;

const userIds = Object.keys(dict);

const occurences = Object.values(dict);

const uniqueOccurences = [...new Set(occurences)];
const newDict = {};

uniqueOccurences.forEach(occurence => {
  newDict[occurence] = [];
  for (let i = 0; i < userIds.length; i++) {
    if (occurence === occurences[i]) {
      newDict[occurence].push(userIds[i]);
    }
  }
});

console.log(newDict);
