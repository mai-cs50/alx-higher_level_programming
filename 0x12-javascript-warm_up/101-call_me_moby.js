#!/usr/bin/node
// Write a file that modifies the value of myVar to 333

exports.callMeMoby = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
