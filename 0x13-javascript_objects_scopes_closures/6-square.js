#!/usr/bin/node

/* a class Square that defines a square and inherits from Square of 5-square.js
 * You must use the class notation for defining your class and extends
 * Create an instance method called charPrint(c) that prints the rectangle using the character c
 * - If c is undefined, use the character X
*/

const SquareBase = require('./5-square.js');

class Square extends SquareBase {
  charPrint (c) {
    if (c === undefined) {
      this.print();
      return;
    }
    let squ = [];
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        squ.push(c);
      }
      console.log(squ.join(''));
      squ = [];
    }
  }
}

module.exports = Square;
