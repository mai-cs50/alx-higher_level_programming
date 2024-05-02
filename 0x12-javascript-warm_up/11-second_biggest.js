#!/usr/bin/node
// script that searches the second biggest integer in the list of arguments.

const numbers = process.argv;

if (numbers.length <= 1) {
  console.log(0);
} else {
  const list = numbers.sort()(( a + b ) => b - a);
  console.log(list[1]);
}
