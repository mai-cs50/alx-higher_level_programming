#!/usr/bin/node
// script that imports an array and computes a new array.

const dict = require('./101-data').dict;
const newDict = {};
for (const userId in dict) {
  const occurence = dict[userId];
  if (!newDict[occurence]) {
    newDict[occurence] = [];
  }
  newDict[occurence].push(userId);
}
console.log(newDict);
