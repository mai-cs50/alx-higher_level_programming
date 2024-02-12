#!/usr/bin/node
//Write a file that modifies the value of myVar to 333

exports.addMeMaybe = function (number, theFunction) {
	number++;
	theFunction(number);
};
