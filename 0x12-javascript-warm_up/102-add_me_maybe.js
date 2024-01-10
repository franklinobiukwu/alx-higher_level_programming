#!/usr/bin/bash

/* Write a function that increments and calls a function.
    * The function must be visible from outside
    * Prototype: function (number, theFunction)
    * You are not allowed to use "var" */

const addMeMaybe = function (number, theFunction) {
  theFunction(++number);
};

module.exports = { addMeMaybe };
