#!/usr/bin/node

/*  a function that prints the number of arguments
 *  already printed and the new argument value */

let store = 0;

exports.logMe = function (item) {
	function logger () {
		console.log(`${store}: ${item}`)
		store += 1;
	}
	logger()
}
