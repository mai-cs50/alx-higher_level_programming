#!/usr/bin/node
// script that imports an array and computes a new array.

const { list } = require('./100-data');
console.log(list);
console.log(list.map((element, idx) => element * idx));
