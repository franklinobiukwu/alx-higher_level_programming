#!/usr/bin/node

/* a function that returns the number of occurrences in a list */

exports.nbOccurences = function (list, searchElement) {
  let sum = 0;
  list.forEach((item) => {
    sum += (item === searchElement ? 1 : 0);
  });
  return sum;
};
