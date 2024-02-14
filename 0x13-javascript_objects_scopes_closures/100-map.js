#!/usr/bin/node
// script that imports an array and computes a new array.

const lists = require('./100-data').list;
console.log(lists);
const mappedlist = lists.map(function (e, index) {
  return (e * index);
});
console.log(mappedlist);
